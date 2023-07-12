"""Exercício 6.6 - Ordenação"""


def ordenado(v):
    res = []
    while len(v) > 0:
        menor = min(v)
        v.remove(menor)
        res += [menor]
    return res


print(ordenado([3, -2, 0, 9, 4, 5, 3, 1, 8, 20, -50, 6]))
