"""Exercício 8.7 - Índice do maior elemento da matriz"""

def indice_do_maximo(mat):
  max_n = mat[0][0]
  x = y = 0
  for indice_i ,i in enumerate(mat):
    for indice_j, j in enumerate(i):
      if (j > max_n):
        max_n = j
        x = indice_i
        y = indice_j
  return x, y

print(indice_do_maximo([[10, 5, -2],
[ 7, -1, 21],
[61, 42, 0],
[ 9, 2, -1]]))