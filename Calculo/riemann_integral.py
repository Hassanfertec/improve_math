import numpy as np

def f(x):
    return x**2  # Função exemplo, você pode alterar para a função desejada

def integral_riemann(a, b, n):
    dx = (b - a) / n
    x = np.linspace(a, b, n)
    y = f(x)
    area = np.sum(y * dx)
    return area

# Exemplo de uso
a = 0  # Limite inferior
b = 1  # Limite superior
n = 1000  # Número de subintervalos

resultado = integral_riemann(a, b, n)
print(f"A integral de Riemann da função no intervalo de {a} a {b} é aproximadamente {resultado}")
