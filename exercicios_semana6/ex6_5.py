"""Exercício 6.5 - Histograma"""


def histograma(v):
    hist = [0] * len(v)
    for elem in v:
        hist[elem] += 1
    return hist


print(histograma([3, 5, 5, 5, 4, 5, 2, 2, 7, 7, 0, 9, 9, 9]))
