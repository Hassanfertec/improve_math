# Importando as bibliotecas necessárias
from sklearn.linear_model import LinearRegression
import numpy as np

# Criando dados de exemplo
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Variável independente
y = np.array([2, 3, 4, 5, 6])  # Variável dependente

# Inicializando o modelo de regressão linear
modelo = LinearRegression()

# Ajustando o modelo aos dados
modelo.fit(X, y)

# Imprimindo os coeficientes da regressão
print('Intercepto:', modelo.intercept_)
print('Coeficiente:', modelo.coef_[0])

# Fazendo previsões com o modelo
X_novo = np.array([6, 7, 8]).reshape(-1, 1)
y_pred = modelo.predict(X_novo)
print('Previsões:', y_pred)
