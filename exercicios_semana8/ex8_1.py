"""Exercício 8.1 - Verificando se m é uma matriz"""

def verifica_matriz(m):
    tamanho = len(m[0])
    for i in m:
        if (len(i) != tamanho):
            return False
    return True

print(verifica_matriz([[3, 2], [-3, 4]]))
print(verifica_matriz([[3, 2], [-3, 4], [5, 0]]))
print(verifica_matriz([[1], [2], [3]]))
print(verifica_matriz([[1, 2, 3]]))
print(verifica_matriz([[3, 2], [-3, 4], [5]]))