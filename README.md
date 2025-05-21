# Método de Newton para Sistemas Não Lineares

Este projeto implementa o **método de Newton-Raphson multivariado** para resolver sistemas de equações não lineares com duas ou mais variáveis, utilizando a biblioteca **SymPy** para manipulação simbólica e numérica.



## 🎯 Objetivo

Resolver numericamente sistemas de equações não lineares da forma:

$$
F(x) = 0
$$

Onde:

- **F(x)** é um vetor de funções não lineares;

- O método aplica derivadas parciais (Jacobiana) e resolve sistemas lineares iterativamente.


## 📖 Como Funciona o Método

A cada iteração, o método executa:

$$
J(x_k) \cdot \Delta x = -F(x_k) \\
x_{k+1} = x_k + \Delta x
$$

Onde:

- $J(x^k)$ é a Jacobiana no ponto atual;

- $\Delta x$ é a correção do sistema linear;

- $x^k$ é a estimativa atual da solução.

O processo é repetido até que:

- $|F(x^k)|_\infty < \varepsilon_1$

- $|x^{k+1} - x^k|_\infty < \varepsilon_2$


## 🔄 Pseudocódigo - Método de Newton

Dados x₀, ε₁ e ε₂ > 0

Passo 1: Calcular F(xᵏ) e J(xᵏ)

Passo 2: Se ||F(xᵏ)||∞ < ε₁ então x* = xᵏ. Pare 

Caso contrário:

Passo 3: Obtenha Sᵏ, solução do sistema linear: J(xᵏ) · Sᵏ = -F(xᵏ)

Passo 4: Calcule xᵏ⁺¹ = xᵏ + Sᵏ

Passo 5: Se ||xᵏ⁺¹ - xᵏ||∞ < ε₂ então x* = xᵏ⁺¹ Pare

Passo 6: k = k + 1. Volte ao Passo 1


## 🧠 Equações de Exemplo

```python
vet_eqs = [
    "3*x + cos(y*z) - 1/2",
    "x^2 - 81*(y+0.1)**2 + sin(z) + 1.06",
    "e**(-x*y) + 20z + (10*pi - 3)/3"
]
```


## 🔢 Entradas

- x_inicial: vetor com a estimativa inicial para as variáveis;

- condicao_parada: valor limite para critério de convergência (ε);

- vet_eqs: lista com strings representando equações;

- vet_vars: lista com variáveis simbólicas (por exemplo, [x, y, z]).


## ⚙️ Estrutura do Código

- `parse_funcoes(vet_eqs)` Transforma as equações em objetos sympy.Expr

- `lambdifica(vet_expr, vars)` Converte as expressões em funções avaliáveis

- `trasforma_jacobiana(...)` Monta a matriz Jacobiana simbolicamente

- `calc_jacobiana(...)` Avalia numericamente a Jacobiana com um x_k

- `calc_funcoes(...)` Avalia numericamente F(x_k)

- `calc_sistema_linear(...)` Resolve J(x_k)·S^k = -F(x_k) usando o SymPy

- `atualiza_xk(...)` Atualiza a estimativa da solução

- `calc_Newton(...)` Função principal que controla o laço de iteração


## 💡 Exemplo de Execução
Nos trechos abaixo altera conforme as suas funções:

```python
x, y, z = symbols('x y z')  # transforma x, y e z em instâncias
vet_vars = [x, y, z]  # adicione ao vetor

vet_eqs = [  # adicione as funções ao vetor
    "3*x + cos(y*z) - 1/2",
    "x^2 - 81*(y+0.1)**2 + sin(z) + 1.06 ",
    "e**(-x*y) + 20z + (10*pi - 3)/3 "
]

condicao_parada = 10**-8  # adicione a condição de parada
x_inicial = [0.1, 0.1, -0.1]  # vetor inicial
```


## 🧾 Saída Esperada

- Funções utilizadas no cálculo para verificação do usuário.

- Critério de parada: ||F(x_k)||∞ < ε₁  e  ||x^{k+1} - x^k||∞ < ε

- Número de iterações até a convergência

- Valores finais das variáveis x, y, z;


## 🧰 Requisitos

- Python 3.8+

- Biblioteca SymPy

    ```python
    pip install sympy
    ```


## 📂 Como executar

1. Compile o código com um compilador python:
   ```bash
   python3 trabalho.py  
   ```
2. Ou copie o código do arquivo "trabalho.py" no [Google Colab](https://colab.research.google.com)


## 👨‍🏫 Envolvidos

- Professor: Jarbas Ferrari
- Estudantes: [Lucas Mamacedo](https://github.com/lucasomac0) e [Rian Valcanaia](https://github.com/RianValcanaia)


## 📅 Curso

- Universidade: Universidade do Estado de Santa Catarina (UDESC)
- Disciplina: Análise Numérica
- Semestre: 4º 


## 📄 Arquivo-fonte

O código completo do projeto está disponível no GitHub:  
[https://github.com/RianValcanaia/TC2_ANN_Metodo_de_Newton](https://github.com/RianValcanaia/TC2_ANN_Metodo_de_Newton)