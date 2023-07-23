"""Exercício 8.6 - Quadrado mágico"""

def somar_linhas(mat):
    lista_de_soma = []
    for i in mat:
        soma_da_linha = sum(i)
    lista_de_soma.append(soma_da_linha)
    return lista_de_soma

def somar_colunas(mat):
    lista_de_soma = [0] * len(mat[0])
    for i in mat:
        for indice, j in enumerate(i):
            lista_de_soma[indice] += j
    return lista_de_soma

def somar_diagonais(mat):
    diag_principal = diag_secundaria = 0
    for i in range(len(mat)):
        diag_principal += mat[i][i]
        diag_secundaria += mat[i][len(mat) - 1 - i]
    return [diag_principal, diag_secundaria]


def quadrado_magico(mat):
    numero_magico = sum(mat[0]) # soma_de_uma_linha
    soma_da_linhas = somar_linhas(mat)
    somas_das_colunas = somar_colunas(mat)
    somas_das_diagonais = somar_diagonais(mat)

    todas_as_somas = soma_da_linhas + somas_das_colunas + somas_das_diagonais
    for i in todas_as_somas:
        if (i != numero_magico):
            return False
    return True

print(quadrado_magico([[2, 7, 6],
[9, 5, 1],
[4, 3, 8]]))