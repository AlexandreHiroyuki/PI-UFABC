"""Exercício 3.4 - Potência usando multiplicações"""

b = float(input("Digite a base: "))
n = int(input("Digite o expoente: "))

res = 1

for i in range(n):
    res *= b

print(f"{b}^{n} = {res}")
