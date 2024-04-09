class EspacoMetrico:
    def __init__(self, pontos, metrica):
        self.pontos = pontos
        self.metrica = metrica

    def distancia(self, ponto1, ponto2):
        return self.metrica(ponto1, ponto2)

# Exemplo de uso:
def metrica_euclidiana(ponto1, ponto2):
    return ((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)**0.5

pontos = [(1, 2), (3, 4), (5, 6)]
espaco = EspacoMetrico(pontos, metrica_euclidiana)
print(espaco.distancia((1, 2), (3, 4)))
