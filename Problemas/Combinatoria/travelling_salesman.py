import numpy as np
from itertools import combinations

def TSP(G):
    # Número de cidades
    n = len(G)

    # Dicionário para guardar os custos dos subproblemas
    C = {}

    # Inicialização do dicionário com as distâncias da cidade 0 para todas as outras
    for k in range(1, n):
        C[(1 << k, k)] = (G[k][0], [0, k])

    # Iteração sobre todos os subconjuntos de cidades
    for _ in range(2, n):
        for subset_size in combinations(range(1, n), _):
            bits = 0
            for bit in subset_size:
                bits |= 1 << bit

            # Iteração sobre todas as cidades no subconjunto atual
            for k in subset_size:
                prev = bits & ~(1 << k)
                res = []

                # Iteração sobre todas as cidades que podem ser visitadas a partir da cidade k
                for m in subset_size:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + G[m][k], C[(prev, m)][1] + [k]))
                C[(bits, k)] = min(res)

    # Encontrar o caminho mínimo que retorna à cidade 0
    bits = (2**n - 1) - 1
    return min([(C[(bits, k)][0] + G[0][k], C[(bits, k)][1] + [0]) for k in range(1, n)])

# Exemplo de uso
G = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
print(TSP(G))
