import sympy as sp

def taylor(funcao, ponto, ordem):
    x = sp.symbols('x')
    f = sp.sympify(funcao)
    serie = sp.series(f, x, ponto, ordem).removeO()
    return serie

# Exemplo de uso:
funcao = 'sin(x)'
ponto = 0
ordem = 6
print(taylor(funcao, ponto, ordem))
