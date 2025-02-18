# Método de Newton-Raphson
Repositório destinado para o armazenamento do código do Trabalho sobre o Método de Newton-Raphson

## Objetivo Geral

Compreender a lógica do Método de Newton-Raphson para encontrar zeros de funções e implementar computacionalmente a fórmula associada.

## Divisão do Trabalho

O trabalho foi estruturado em 3 partes.

### 1. Programação do Cálculo da Derivada

Implementar computacionalmente o cálculo da derivada de uma função utilizando uma das definições formais por limite:

- **Derivada Avançada:**  
  $f'(x) = \frac{f(x+h) - f(x)}{h}$

- **Derivada Recuada:**  
  $f'(x) = \frac{f(x) - f(x-h)}{h}$

- **Derivada Centrada:**  
  $f'(x) = \frac{f(x+h) - f(x-h)}{2h}$

Validar o código com funções simples (ex.: $f(x) = x^2$).

### 2. Implementação do Método de Newton-Raphson

Programar o algoritmo iterativo do método, que utiliza a fórmula:

$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$

Garantir critérios de parada adequados (ex.: tolerância de erro, número máximo de iterações).

### 3. Resolução de Problemas

#### Teste Inicial:
Encontrar as raízes de $f(x) = x^2 - 4$ para validar o método.

#### Desafios:
- **Problema 1:** Resolver $x^2 = 2x$ (encontrar todas as soluções reais).
- **Problema 2:** Encontrar as 3 primeiras raízes positivas de $tan(x) = \frac{1}{x}$.
