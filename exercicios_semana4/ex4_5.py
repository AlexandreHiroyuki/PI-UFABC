"""Exercício 4.5 - Máximo divisor comum"""


def mdc(a, b):
    x = max(a, b)
    y = min(a, b)
    resto = x % y
    while resto > 0:
        x = y
        y = resto
        resto = x % y
    return y


print(mdc(30, 30))  # 30
print(mdc(320, 210))  # 10
print(mdc(90, 25))  # 5
print(mdc(73, 29))  # 1
