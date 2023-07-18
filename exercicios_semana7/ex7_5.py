"""Exercício 7.5 - Sorteio"""

import random


def sorteio(apostas):
    total = 0
    while len(apostas) > 0:
        s = random.randrange(1000)
        total += 1
        if s in apostas:
            apostas.remove(s)
    return total


s1, s2 = 0, 0
n = 10000
for _ in range(n):
    s1 += sorteio({0})
    s2 += sorteio({0, 1})

print("Média para sorteio({0}) é ", s1 / n)
print("Média para sorteio({0, 1}) é ", s2 / n)
