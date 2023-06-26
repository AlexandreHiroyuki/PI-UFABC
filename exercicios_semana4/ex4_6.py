"""Exercício 4.6 - Tabuleiro de xadrez"""


def xadrez(n):
    for i in range(n):
        for j in range(n):
            print("#" if (i + j) % 2 else "-", end="")
        print()


xadrez(8)
