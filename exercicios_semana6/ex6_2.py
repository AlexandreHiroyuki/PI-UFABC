"""Exercício 6.2 - Classificação por média"""


def classificar_notas(v):
    res = []
    media = sum(v) / len(v)
    for elem in v:
        if elem < media:
            res += ["abaixo"]
        else:
            res += ["acima"]
    return res


print(classificar_notas([7, 8, 4, 10, 9]))
