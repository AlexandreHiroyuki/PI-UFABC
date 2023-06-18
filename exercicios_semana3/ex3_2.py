"""Exercício 3.2 - Laço aninhado"""

n = int(input("Número de linhas: "))
m = int(input("Número de colunas: "))

for i in range(n):
    for j in range(m):
        print("*" if i % 2 == 0 else "#", end="")
    print()
