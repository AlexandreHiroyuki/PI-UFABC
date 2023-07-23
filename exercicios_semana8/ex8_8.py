"""Exercício 8.8 - Linha e coluna igual (versão 1)"""

def linha_coluna_igual1(mat):
    for i in range(len(mat)):
      for j in range(len(mat)):
        for k in range(len(mat[i])):
            if mat[i][k] == mat[k][j]:
                return True
    return False

print(linha_coluna_igual1([[ 9, -8,  3],
       [-8, -1,  21],
       [ 3,  7,  9]]))