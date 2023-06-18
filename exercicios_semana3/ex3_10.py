"""Exercício 3.10 - Triângulo de Pascal"""

n = int(input("Número de linhas: "))


for i in range(1, n + 1):
    p = 1
    print("1 ", end="")
    for j in range(1, i):
        p = (p * (i - j)) // j
        print(f"{p} ", end="")
    print()
