"""Exercício 6.9 - Cartão de crédito"""


def luhn(num_cartao):
    num_cartao = num_cartao.replace(" ", "")
    num_cartao = [int(c) for c in num_cartao]
    for i in range(0, len(num_cartao), 2):
        n = num_cartao[i] * 2
        num_cartao[i] = n - 9 if n > 9 else n
    return sum(num_cartao) % 10 == 0


print(luhn("4539 3195 0343 6467"))  # True
print(luhn("8273 1232 7352 0569"))  # False

