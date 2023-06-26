"""Exercício 4.7 - Tabuleiro de xadrez 2"""


def xadrez2(n, x):
    for i in range(n * x):
        for j in range(n * x):
            print("#" if ((i // x + j // x)) % 2 else "-", end="")
        print()


xadrez2(3, 5)
