"""Exercício 3.7 - Fatorial"""


def fatorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


print(fatorial(4))
