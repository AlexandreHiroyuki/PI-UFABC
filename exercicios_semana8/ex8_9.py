"""Exercício 8.9 - Linha e coluna igual (versão 2: fora de ordem)"""

def linha_coluna_igual2(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if sorted(mat[i]) == sorted([mat[k][j] for k in range(len(mat))]):
                return True
    return False

print(linha_coluna_igual2([[ 9, -8,  3],
       [-8, -1,  21],
       [ 3,  7,  9]]))