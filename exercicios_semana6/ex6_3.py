"""Exercício 6.3 - Número de ocorrências"""


def ocorrencias(valor, lista):
    total = 0
    for elem in lista:
        if valor == elem:
            total += 1
    return total


print(ocorrencias(5, [2, 5, -1, 5, 5, 4, 4]))
