import numpy as np
import matplotlib.pyplot as plt

# Número de iterações
N = 1000

# Parâmetro do mapa de Bernoulli
r = 2.0

# Condição inicial
x = 0.1

# Lista para armazenar a trajetória
trajetoria = []

# Iterar o mapa de Bernoulli
for _ in range(N):
    # Aplicar o mapa de Bernoulli
    x = r * x % 1.0

    # Armazenar a posição atual
    trajetoria.append(x)

# Plotar a trajetória
plt.figure(figsize=(10,6))
plt.plot(trajetoria)
plt.title('Trajetória do Mapa de Bernoulli')
plt.xlabel('Iterações')
plt.ylabel('x')
plt.grid(True)
plt.show()
