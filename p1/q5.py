"""Padrão matricial"""


def matriz(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = max(i, j)
            print(f"{x:02} ", end="")
        print()

