from sympy import symbols, diff, lambdify, pi, E
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

def calc_Newton(x_inicial, condicao_parada, funcoes, jacobiana):
    x = x_inicial.copy()
    res_F = calc_funcoes(funcoes, x)
    res_J = calc_jacobiana(jacobiana, x)
    print("F(x^k): ")
    print(res_F)
    print("J(x^k): ")
    print(res_J)

    # while(norma_infinita(res_F) > condicao_parada):
        # Passo 3 Obtenha S^k, solução do sistema linear J(x^k)*S^k = -F(x^k)

    
# main 
## Funcoes

''' Eqs para usar ao entregar o trabalho
x, y, z = symbols('x y z')
vet_vars = [x, y, z]

vet_eqs = [
    "3*x + cos(x*y) - 1/2",
    "x^2 - 81(x+0.1)^2 + sin(z) + 1.06 ",
    "e^(-xy) + 20z + (10pi - 3)/3 "
]

condicao_parada = 10**-9
x_inicial = [0.1, 0.1, -0.1]

'''
# Eqs para testes, conteudo da aula
x, y = symbols('x y')
vet_vars = [x, y]

vet_eqs = [
    "x + y -3",
    "x^2 + y**2 -9"
]

condicao_parada = 10**-2
x_inicial = [1, 5]

# funcoes com lambdify
funcoes = transforma_funcoes(vet_eqs, vet_vars)
jacobiana = trasforma_jacobiana(vet_eqs, vet_vars)

calc_Newton(x_inicial, condicao_parada, funcoes, jacobiana)