"""Exercício 8.5 - Soma das colunas da matriz"""

def somar_colunas(mat):
    lista_de_soma = [0] * len(mat[0])
    for i in mat:
        for indice, j in enumerate(i):
            lista_de_soma[indice] += j
    return lista_de_soma

print(somar_colunas([[10, 5, -2],
[ 7, -1, 21],
[61, 42, 0],
[ 9, 2, -1]]))