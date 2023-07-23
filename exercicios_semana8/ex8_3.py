"""Exercício 8.3 - Matriz identidade"""

def matriz_identidade(n):
    matriz = [[0]*n for _ in range(n)]
    for i in range(n):
        matriz[i][i] = 1
    return matriz

print(matriz_identidade(4))
print(matriz_identidade(1))