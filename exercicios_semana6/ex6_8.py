"""Exercício 6.8 - Número de dígitos"""


def contar_digitos(texto):
    total = 0
    for c in texto:
        if (
            c == "0"
            or c == "1"
            or c == "2"
            or c == "3"
            or c == "4"
            or c == "5"
            or c == "6"
            or c == "7"
            or c == "8"
            or c == "9"
        ):
            # if c in list("0123456789"):
            # if c.isdigit():
            total += 1
    return total


print(contar_digitos("j90s1mkj34"))  # 5
print(contar_digitos("01216640"))  # 8
print(contar_digitos("iwexlk"))  # 0
