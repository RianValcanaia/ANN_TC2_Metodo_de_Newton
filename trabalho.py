from sympy import symbols, diff, lambdify, pi, E, Matrix, solve_linear_system
from sympy.parsing.sympy_parser import parse_expr

def norma_infinita(vet):  # devolve o maior valor absoluto do vetor
    return max(abs(val) for val in vet)

def parse_funcoes(vet_eqs):  # transforma as string em expressões do sympy
    local_dict = {'e': E, 'pi': pi}  # dicionário utilizado para alterar constantes
    vet_expr = []
    print("F(x): {")
    for eq in vet_eqs:
        expr = parse_expr(eq, transformations='all', local_dict=local_dict)  # transforma cada string equação em expressão
        vet_expr.append(expr)  # adiciona ao vetor
        print("    ", expr,"= 0")  # printa a expressão no formato sympy.Expr para verificação do usuário
    print("}\n")
    return vet_expr  

def lambdifica(vet_expr, vet_vars):  # labdifica as funções fazendo com que seja possível jogar variáveis nas expressões
    return [lambdify(vet_vars, expr, modules='math') for expr in vet_expr]  # retorna um vetor de expressões lambdificadas

def trasforma_jacobiana(vet_eqs_expr, vet_vars):  # recebe o vetor de sympy.Expr e o vetor de variáveis e devolve uma matriz com equações de derivadas parciais em cada linha
    J = []
    for eq in vet_eqs_expr:  # para cada equação deriva em relação a uma variável
        linha = []
        for var in vet_vars:
            derivada = diff(eq, var)  # deriva equação em relação a var 
            func = lambdify(vet_vars, derivada, modules='math')  # lambdifica essa equação
            linha.append(func)  # adiciona a função na linha
        J.append(linha)  # adiciona a linha na matriz
    return J

def calc_jacobiana(jacobiana, vet_x):  # devolve uma matriz aplicando vet_x na matriz jacobiana
    vet_res = []
    for linha in jacobiana: 
        nova_linha = []
        for func in linha:
            nova_linha.append(float(func(*vet_x)))  #  para cada derivada aplica as variáveis e adiciona na nova_linha
        vet_res.append(nova_linha)  # adiciona nova_linha na matriz
    return vet_res  # retorna uma matriz com vet_x aplicado em cada derivada

def calc_funcoes(funcoes, vet_x):  # devolve um vetor onde foi aplicado vet_x no vetor de funções
    vet_res = []
    for f in funcoes: vet_res.append(float(f(*vet_x)))
    return vet_res

def calc_sistema_linear(funcoes, jacobiana, x_inicial, vet_vars):
    x = x_inicial.copy() # cria uma copia do vetor inicial de x
    jacobiana_calculo = calc_jacobiana(jacobiana, x) # deixa a matriz jacobiana com valores numericos para usar em calculos
    funcoes_calculo = calc_funcoes(funcoes, x) # deixa as funcoes com valores numericos para usar em calculos
    
    for i in range(len(funcoes_calculo)):
        jacobiana_calculo[i].append(-1*funcoes_calculo[i]) # adiciona ao final de todas as linhas da matriz jacobiana o valor de -F(x). O valor é negativo conforme passado em aula para montar o sistema linear
        # essa adição dos valores de F ao final de cada linha da matriz jacobiana serve para montar a matriz na forma aumentada, com a ultima coluna sendo a coluna de termos independentes
        # isto é vantajoso pois o SymPy possui uma subrotina de solução de sistemas lineares no formato de matriz aumentada, que será usado logo em seguida nesta função 
    sistema_linear = Matrix(jacobiana_calculo) # transforma a matriz jacobiana aumentada em uma matriz reconhecida pelo SymPy para que possam ser chamadas subrotinas 
    res_sistema = solve_linear_system(sistema_linear, *vet_vars) # aqui está a subrotina do SymPy que resolve o sistema linear representado por uma matriz aumentada. 
    # para a subrotina funcionar voce deve passar a matriz aumentada e as variaveis do sistema
    res_sistema_numerico = [res_sistema[var] for var in vet_vars] # a subrotina de solução de sistema linear do SymPy retorna uma lista que contém o resultado e qual variável está atrelada àquele resultado 
    # para conseguir trabalhar de forma mais rápida e simples com os resultados, nós criamos um vetor apenas com os valores numéricos ordenados pela ordem de variáveis (x, y)
    return res_sistema_numerico

def atualiza_xk(x_anterior, res_sistema):
    return [x_anterior[i] + res_sistema[i] for i in range(len(x_anterior))]
    # rotina criada para atualizar o valor de x^k para o código na função calc_Newton ficar mais legível
    

def calc_Newton(x_inicial, condicao_parada, funcoes, jacobiana, vet_vars):
    x_atual = x_inicial.copy() # cria uma cópia do valor de x_inicial 
    res_F = calc_funcoes(funcoes, x_atual) # calcula os valores numéricos das funções 
    max_iteracoes = 15 # numero maximo de iterações caso não convirja
    i = 0 # contador simples

    while((norma_infinita(res_F) > condicao_parada) and i < max_iteracoes): # enquanto a norma infinita das funções for maior que a condição de parada E o contador for menor que o nº max de iterações
        res_sistema = calc_sistema_linear(funcoes, jacobiana, x_atual, vet_vars) # resolve o sistema linear
        x_novo = atualiza_xk(x_atual, res_sistema) # atualiza o x_novo

        if (norma_infinita(res_sistema) < condicao_parada): break # se a norma infinita da solução do sistema for menor que epsilon retorna o x_atual

        x_atual = x_novo 
        res_F = calc_funcoes(funcoes, x_atual) # recalcula as funções com o valor de x atualizado
        i+=1 # incrementa o contador de iterações

    print("Critério ||F(X^k)|| <", condicao_parada, "e ||X^k - X^(k+1)|| <", condicao_parada)
    print("Número de iterações: ", i)
    for i in range(len(vet_vars)): print(vet_vars[i], "=", x_atual[i])
    return x_atual



# ====================== MAIN ======================
x, y, z = symbols('x y z')  # cria variáveis simbólicas que serão usadas para definiz expressões matemáticas simbólicas
vet_vars = [x, y, z]  # adiciona ao vetor essas variáveiz simbólicas

# vetor de equações em strings, é possível transformar as expressões sem ter o símbolo de multiplicação, mas é recomendado utilizar. O mesmo para ** que é reconhecido ^.
vet_eqs = [  
    "3*x + cos(y*z) - 1/2",
    "x^2 - 81*(y+0.1)**2 + sin(z) + 1.06 ",
    "e**(-x*y) + 20z + (10*pi - 3)/3 "
]

condicao_parada = 10**-8 
x_inicial = [0.1, 0.1, -0.1]

vet_eqs_expr = parse_funcoes(vet_eqs)  # transforma as equações em expressões simbólicas
funcoes = lambdifica(vet_eqs_expr, vet_vars)  # labdifica as expreções
jacobiana = trasforma_jacobiana(vet_eqs_expr, vet_vars)  # faz a matriz jacobiana lambdificada

# calcula o vetor solução utilizando método de newton
calc_Newton(x_inicial, condicao_parada, funcoes, jacobiana, vet_vars)
