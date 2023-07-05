"""Sequência cíclica 4321"""


def sequencia(n):
    c = 4
    for _ in range(n):
        print(f"{c} ", end="")
        c -= 1
        if c == 0:
            c = 4
    print()


# Usando módulo
def sequencia2(n):
    for i in range(n):
        print(f"{4 - i % 4} ", end="")
    print()

