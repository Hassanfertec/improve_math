# Importando a biblioteca sympy
import sympy as sp

# Definindo a função para calcular a expansão de Taylor
def taylor(funcao, ponto, ordem):
    # Criando um símbolo para x
    x = sp.symbols('x')
    
    # Convertendo a string da função em uma expressão sympy
    f = sp.sympify(funcao)
    
    # Calculando a série de Taylor da função até a ordem especificada
    serie = sp.series(f, x, ponto, ordem).removeO()
    
    # Retornando a série de Taylor
    return serie

# Exemplo de uso:
# Definindo a função como 'sin(x)'
funcao = 'sin(x)'

# Definindo o ponto como 0
ponto = 0

# Definindo a ordem como 6
ordem = 6

# Calculando e imprimindo a série de Taylor da função sin(x) em torno do ponto x=0 até a sexta ordem
print(taylor(funcao, ponto, ordem))
