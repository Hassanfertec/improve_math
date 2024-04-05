import numpy as np
import matplotlib.pyplot as plt

# Número de passos
N = 1000

# Passos aleatórios
passos = np.random.choice([-1, 1], size=N)

# Posição após cada passo
posicao = np.cumsum(passos)

# Plot
plt.figure(figsize=(10,6))
plt.plot(posicao)
plt.title('Passeio Aleatório Unidimensional')
plt.xlabel('Passos')
plt.ylabel('Posição')
plt.grid(True)
plt.show()
