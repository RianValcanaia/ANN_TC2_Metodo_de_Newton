from sympy import symbols, diff, lambdify, pi, E, Matrix, solve_linear_system
from sympy.parsing.sympy_parser import parse_expr

'''
Algoritimo - Método de Newton (pseudocódigo)

Dados x0, epson1 e epson2 > 0
Passo 1: Calcular F(x^k) e J(x^k)
passo 2: Se || F(x^k) || norma infinita < epson1, então x*=x^k
e pare;
caso contrario:
Passo 3 Obtenha S^k, solução do sistema linear J(x^k)*S^k = -F(x^k)
Passo 4 FAÇA: x^k+1 = x^k + s^k
passo 5 Se || x^k+1 - x^k || norma infinita < epson2, faça x* = x^k+1
e pare;
caso contrario:
passo 6 k = k + 1
	volte ao passo 1

'''


def norma_infinita(vet):  # devolve o maior valor absoluto do vetor
    max_abs = max(vet, key=abs)
    return max_abs

def transforma_funcoes(vet_eqs, vet_vars):  # recebe o vetor de equaçõess e o vetor de variáveis e devolve um vetor com funções lambdificada
    local_dict = {'e': E, 'pi': pi}  # dicionário que altera caracteres de string para constantes, ps: adicionar mais caso não funcionar em futuros testes
    vet_func = []
    for eq in vet_eqs:
        expr = parse_expr(eq, transformations="all", local_dict=local_dict)  # faz a transformação de string para expressão usando todos os tipos de transformações e o dicionário local
        f = lambdify(vet_vars, expr)  # lambdifica as expressões
        vet_func.append(f)
    return vet_func

def trasforma_jacobiana(vet_eqs, vet_vars):  # recebe o vetor de equaçõess e o vetor de variáveis e devolve uma matriz com equações de derivadas parciais em cada linha
    J = []
    for eq in vet_eqs:
        linha = []
        for var in vet_vars:
            derivada = diff(eq, var)
            func = lambdify(vet_vars, derivada)
            linha.append(func)
        J.append(linha)
    return J

def calc_jacobiana(jacobiana, vet_x):  # devolve uma matriz de resposta aplicando vet_x na matriz jacobiana
    vet_res = []
    for linha in jacobiana:
        nova_linha = []
        for func in linha:
            nova_linha.append(float(func(*vet_x)))
        vet_res.append(nova_linha)
    return vet_res

def calc_funcoes(funcoes, vet_x):  # devolve um vetor onde foi aplicado vet_x no vetor de funcoes
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
    print(jacobiana_calculo)
    sistema_linear = Matrix(jacobiana_calculo) # transforma a matriz jacobiana aumentada em uma matriz reconhecida pelo SymPy para que possam ser chamadas subrotinas 
    res_sistema = solve_linear_system(sistema_linear, *vet_vars) # aqui está a subrotina do SymPy que resolve o sistema linear representado por uma matriz aumentada. 
    # para a subrotina funcionar voce deve passar a matriz aumentada e as variaveis do sistema
    res_sistema_numerico = [res_sistema[var] for var in vet_vars] # a subrotina de solução de sistema linear do SymPy retorna uma lista que contém o resultado e qual variável está atrelada àquele resultado 
    # para conseguir trabalhar de forma mais rápida e simples com os resultados, nós criamos um vetor apenas com os valores numéricos ordenados pela ordem de variáveis (x, y)
    print("Solucao sistema: ")
    print(res_sistema_numerico)
    return res_sistema_numerico

def atualiza_xk(x_anterior, res_sistema):
    x_atual = x_anterior.copy()
    for i in range(len(x_atual)):
        x_atual[i] = x_anterior[i] + res_sistema[i]
    return x_atual
    


def calc_Newton(x_inicial, condicao_parada, funcoes, jacobiana, vet_vars):
    res_F = calc_funcoes(funcoes, x_inicial)
    res_J = calc_jacobiana(jacobiana, x_inicial)
    x_atual = x_inicial.copy()
    x_anterior = [a + 1 for a in x_inicial]
    max_iteracoes = 15
    i = 0

    while((norma_infinita(res_F) > condicao_parada) and i < max_iteracoes):
        res_sistema = calc_sistema_linear(funcoes, jacobiana, x_atual, vet_vars)
        x_anterior = x_atual.copy()
        x_atual = atualiza_xk(x_atual, res_sistema)
        res_F = calc_funcoes(funcoes, x_atual)
        res_J = calc_jacobiana(jacobiana, x_atual)
        vetor_diferenca = [a - b for a, b in zip(x_atual, x_anterior)]
        i = i + 1
        #if(norma_infinita(vetor_diferenca) < condicao_parada):
        #   return x_atual

    print("numero iteracoes:")
    print(i)
    print("Solução geral: ")
    print(x_atual)
    return x_atual



# main
## Funcoes

#Eqs para usar ao entregar o trabalho
x, y, z = symbols('x y z')
vet_vars = [x, y, z]

vet_eqs = [
    "3*x + cos(x*y) - 1/2",
    "x^2 - 81(x+0.1)^2 + sin(z) + 1.06 ",
    "e^(-xy) + 20z + (10pi - 3)/3 "
]

condicao_parada = 10**-9
x_inicial = [0.1, 0.1, -0.1]


# Eqs para testes, conteudo da aula
'''x, y = symbols('x y')
vet_vars = [x, y]

vet_eqs = [
    "x + y -3",
    "x^2 + y**2 -9"
]'''

condicao_parada = 0.01 # 10**-2
x_inicial = [1, 5]

# funcoes com lambdify
funcoes = transforma_funcoes(vet_eqs, vet_vars)
jacobiana = trasforma_jacobiana(vet_eqs, vet_vars)
#calc_sistema_linear(funcoes, jacobiana, x_inicial, vet_vars)
calc_Newton(x_inicial, condicao_parada, funcoes, jacobiana, vet_vars)
