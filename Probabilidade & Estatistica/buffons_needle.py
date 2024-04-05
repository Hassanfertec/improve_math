import random
import math

def buffon_needle_simulation(num_needles, needle_length, gap_width):
    """
    Simula o problema da agulha de Buffon e calcula a probabilidade.

    Args:
        num_needles (int): Número de agulhas a serem simuladas.
        needle_length (float): Comprimento da agulha.
        gap_width (float): Largura da lacuna entre as linhas paralelas.

    Returns:
        float: Probabilidade estimada.
    """
    intersected_needles = 0

    for _ in range(num_needles):
        # Gere aleatoriamente o ponto médio da agulha
        midpoint_x = random.uniform(0, gap_width / 2)
        # Gere aleatoriamente o ângulo da agulha (em radianos)
        angle = random.uniform(0, math.pi / 2)

        # Calcule os pontos finais da agulha
        x1 = midpoint_x - (needle_length / 2) * math.cos(angle)
        x2 = midpoint_x + (needle_length / 2) * math.cos(angle)

        # Verifique se a agulha cruza as linhas
        if x1 < 0 or x2 > gap_width:
            intersected_needles += 1

    # Calcule a probabilidade estimada
    probability = intersected_needles / num_needles
    return probability

# Parâmetros para a simulação
num_needles = 100000
needle_length = 1.0
gap_width = 2.0

# Execute a simulação
probabilidade_estimada = buffon_needle_simulation(num_needles, needle_length, gap_width)

# Imprima o resultado
print(f"Probabilidade estimada usando {num_needles} agulhas: {probabilidade_estimada:.6f}")
