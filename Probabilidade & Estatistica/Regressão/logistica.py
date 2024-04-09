# Importando as bibliotecas necessárias
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carregando o conjunto de dados iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializando o modelo de regressão logística
modelo = LogisticRegression()

# Ajustando o modelo aos dados de treinamento
modelo.fit(X_train, y_train)

# Fazendo previsões com o modelo nos dados de teste
y_pred = modelo.predict(X_test)

# Calculando a acurácia do modelo
acuracia = accuracy_score(y_test, y_pred)
print('Acurácia do modelo:', acuracia)
