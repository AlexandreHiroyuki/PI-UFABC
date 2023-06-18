"""Exercício 3.5 - Potência com expoente negativo"""

b = float(input("Digite a base: "))
n = int(input("Digite o expoente: "))

res = 1
termo = b if n >= 0 else 1 / b

for i in range(abs(n)):
    res *= termo

print(f"{b}^{n} = {res}")
