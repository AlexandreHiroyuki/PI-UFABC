"""Exercício 8.2 - Tamanho da matriz"""

def tamanho_matriz(mat):
    num_linhas = len(mat)
    num_colunas = len(mat[0])
    return num_linhas, num_colunas

l, c = tamanho_matriz([[3, 2], [-3, 4], [5,0]])
print("Número de linhas:", l) # 3
print("Número de colunas:", c) # 2