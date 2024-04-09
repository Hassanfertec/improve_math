def determinant_sarrus(matrix):
    """
    Calcula o determinante de uma matriz 3x3 usando o método de Sarrus.
    """
    if len(matrix) != 3 or len(matrix[0]) != 3:
        raise ValueError("A matriz deve ser 3x3 para usar o método de Sarrus.")
    
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    
    det = (a * e * i) + (b * f * g) + (c * d * h)
    det -= (c * e * g) + (a * f * h) + (b * d * i)
    
    return det

# Exemplo de matriz
matrix_sarrus = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calcula o determinante usando o método de Sarrus
determinante_sarrus = determinant_sarrus(matrix_sarrus)

# Imprime o resultado
print(f"O determinante da matriz usando o método de Sarrus é: {determinante_sarrus}")
