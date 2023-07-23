"""Exercício 8.4 - Soma das linhas da matriz"""

def somar_linhas(mat):
    lista_de_soma = []
    for i in mat:
        soma_da_linha = 0
        for j in i:
            soma_da_linha += j
        lista_de_soma.append(soma_da_linha)
    return lista_de_soma

print(somar_linhas([[10, 5, -2],
[ 7, -1, 21],
[61, 42, 0],
[ 9, 2, -1]]))