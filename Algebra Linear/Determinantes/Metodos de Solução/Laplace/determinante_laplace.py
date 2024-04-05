def minor(matrix, row, col):
    """
    Calcula o menor de uma matriz removendo a linha e coluna especificadas.
    """
    return [row[:col] + row[col+1:] for row in (matrix[:row] + matrix[row+1:])]

def determinant_laplace(matrix):
    """
    Calcula o determinante de uma matriz usando a expansão de Laplace.
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for col in range(n):
            det += ((-1) ** col) * matrix[0][col] * determinant_laplace(minor(matrix, 0, col))
        return det

# Exemplo de matriz
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calcula o determinante usando a expansão de Laplace
determinante = determinant_laplace(matrix)

# Imprime o resultado
print(f"O determinante da matriz é: {determinante}")
