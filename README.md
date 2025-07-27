<div align="center" id="topo">

<img src="https://media.giphy.com/media/iIqmM5tTjmpOB9mpbn/giphy.gif" width="200px" alt="Gif animado"/>

# <code><strong>Método de Newton para Sistemas Não Lineares</strong></code>

<em>Este projeto implementa o **método de Newton-Raphson multivariado** para resolver sistemas de equações não lineares com duas ou mais variáveis, utilizando a biblioteca **SymPy** para manipulação simbólica e numérica.
</em>

[![Python Usage](https://img.shields.io/badge/Python-100%25-blue?style=for-the-badge\&logo=python)]()
[![Status](https://img.shields.io/badge/Status-Concluído-green?style=for-the-badge)]()
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Visite%20meu%20perfil-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/rian-carlos-valcanaia-b2b487168/)

</div>

## Índice

- [🎯 Objetivos](#-objetivos)
- [📖 Como Funciona o Método](#-como-funciona-o-método)
    - [🔄 Pseudocódigo - Método de Newton](#-pseudocódigo---método-de-newton)
    - [🧠 Equações de Exemplo](#-equações-de-exemplo)
- [📥 Entradas do sistema](#-entradas-do-sistema)
- [🧰 Funcionalidades](#-funcionalidades)
- [📊 Exemplo de Execução](#-exemplo-de-execução)
- [🧾 Saída Esperada](-saída-esperada)
- [🧰 Requisitos](-requisitos)
- [📂 Como executar](#-como-executar)
- [👨‍🏫 Envolvidos](#-envolvidos)
- [📅 Curso](#-curso)
- [📄 Código-fonte](#-código-fonte)

## 🎯 Objetivos

Resolver numericamente sistemas de equações não lineares da forma:

$$
F(x) = 0
$$

Onde:

- **F(x)** é um vetor de funções não lineares;

- O método aplica derivadas parciais (Jacobiana) e resolve sistemas lineares iterativamente.

[⬆ Voltar ao topo](#topo)

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

[⬆ Voltar ao topo](#topo)

## 🔄 Pseudocódigo - Método de Newton

Dados x₀, ε₁ e ε₂ > 0

Passo 1: Calcular F(xᵏ) e J(xᵏ)

Passo 2: Se ||F(xᵏ)||∞ < ε₁ então x* = xᵏ. Pare 

Caso contrário:

Passo 3: Obtenha Sᵏ, solução do sistema linear: J(xᵏ) · Sᵏ = -F(xᵏ)

Passo 4: Calcule xᵏ⁺¹ = xᵏ + Sᵏ

Passo 5: Se ||xᵏ⁺¹ - xᵏ||∞ < ε₂ então x* = xᵏ⁺¹ Pare

Passo 6: k = k + 1. Volte ao Passo 1

[⬆ Voltar ao topo](#topo)

## 🧠 Equações de Exemplo

```python
vet_eqs = [
    "3*x + cos(y*z) - 1/2",
    "x^2 - 81*(y+0.1)**2 + sin(z) + 1.06",
    "e**(-x*y) + 20z + (10*pi - 3)/3"
]
```

[⬆ Voltar ao topo](#topo)

## 📥 Entradas do sistema

- x_inicial: vetor com a estimativa inicial para as variáveis;

- condicao_parada: valor limite para critério de convergência (ε);

- vet_eqs: lista com strings representando equações;

- vet_vars: lista com variáveis simbólicas (por exemplo, [x, y, z]).

[⬆ Voltar ao topo](#topo)

## 🧰 Funcionalidades

- `parse_funcoes(vet_eqs)` Transforma as equações em objetos sympy.Expr

- `lambdifica(vet_expr, vars)` Converte as expressões em funções avaliáveis

- `trasforma_jacobiana(...)` Monta a matriz Jacobiana simbolicamente

- `calc_jacobiana(...)` Avalia numericamente a Jacobiana com um x_k

- `calc_funcoes(...)` Avalia numericamente F(x_k)

- `calc_sistema_linear(...)` Resolve J(x_k)·S^k = -F(x_k) usando o SymPy

- `atualiza_xk(...)` Atualiza a estimativa da solução

- `calc_Newton(...)` Função principal que controla o laço de iteração

[⬆ Voltar ao topo](#topo)

## 📊 Exemplo de Execução
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

[⬆ Voltar ao topo](#topo)

## 🧾 Saída Esperada

- Funções utilizadas no cálculo para verificação do usuário.

- Critério de parada: ||F(x_k)||∞ < ε₁  e  ||x^{k+1} - x^k||∞ < ε

- Número de iterações até a convergência

- Valores finais das variáveis x, y, z;

[⬆ Voltar ao topo](#topo)

## 🧰 Requisitos

- Python 3.8+

- Biblioteca SymPy

    ```python
    pip install sympy
    ```
    
[⬆ Voltar ao topo](#topo)

## 📂 Como executar

1. Compile o código com um compilador python:
   ```bash
   python3 trabalho.py  
   ```
2. Ou copie o código do arquivo "trabalho.py" no [Google Colab](https://colab.research.google.com)

[⬆ Voltar ao topo](#topo)

## 👨‍🏫 Envolvidos

- Professor: Jarbas Ferrari
- Estudantes:
    - [Lucas Mamacedo](https://github.com/lucasomac0)
    -  [Rian Valcanaia](https://github.com/RianValcanaia)

[⬆ Voltar ao topo](#topo)

## 📅 Curso

- Universidade: Universidade do Estado de Santa Catarina (UDESC)
- Disciplina: Análise Numérica
- Semestre: 4º 

[⬆ Voltar ao topo](#topo)

## 📄 Código-fonte

🔗 [https://github.com/RianValcanaia/TC2_ANN_Metodo_de_Newton](https://github.com/RianValcanaia/TC2_ANN_Metodo_de_Newton)

[⬆ Voltar ao topo](#topo)
