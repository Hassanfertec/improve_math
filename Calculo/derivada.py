import sympy as sp

def calcular_derivada(funcao, ponto):
    x = sp.symbols('x')
    f = sp.sympify(funcao)
    derivada = sp.diff(f, x)
    resultado = derivada.subs(x, ponto)
    return resultado

# Exemplo de uso:
funcao = 'x**2'
ponto = 2
print(calcular_derivada(funcao, ponto))
