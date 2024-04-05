import math

# Função para calcular combinação
def combinacao(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

# Função para calcular arranjo
def arranjo(n, r):
    return math.factorial(n) / math.factorial(n - r)

# Função para calcular permutação
def permutacao(n):
    return math.factorial(n)

n = 5
r = 3

print(f"Combinação de {n} elementos tomados {r} a {r} é: {combinacao(n, r)}")
print(f"Arranjo de {n} elementos tomados {r} a {r} é: {arranjo(n, r)}")
print(f"Permutação de {n} elementos é: {permutacao(n)}")
