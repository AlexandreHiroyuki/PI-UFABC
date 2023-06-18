"""Exercício 3.9 - Coeficiente binomial"""


def fatorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def binomial(n, k):
    prod = 1
    for i in range(n, n - k + 1 - 1, -1):
        prod *= i
    return prod // fatorial(k)


print(binomial(60, 6))


# for n in range(7):
#     for k in range(n + 1):
#         print(f"{binomial(n, k):g}", " ", end="")
#     print()
