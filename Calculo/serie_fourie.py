import numpy as np
from scipy import integrate

# Definindo a função
def f(x):
    return np.sin(x)

# Definindo os coeficientes da série de Fourier
def a(n, L):
    return integrate.quad(lambda x: f(x)*np.cos(np.pi*n*x/L), -L, L)[0] / L

def b(n, L):
    return integrate.quad(lambda x: f(x)*np.sin(np.pi*n*x/L), -L, L)[0] / L

# Definindo a série de Fourier
def Sf(x, N, L):
    a0 = a(0, L) / 2
    return a0 + sum([(a(n, L)*np.cos(n*np.pi*x/L) + b(n, L)*np.sin(n*np.pi*x/L)) for n in range(1, N+1)])

# Exemplo de uso:
x = np.linspace(-np.pi, np.pi, 1000)
y = Sf(x, 10, np.pi)

print(y)
