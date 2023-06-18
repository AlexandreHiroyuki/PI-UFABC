"""Exercício 3.8 - Número de Euler"""

n = int(input("Digite o n: "))

e = 1
den = 1
for i in range(1, n + 1):
    den *= i
    e += 1 / den

print(e)
