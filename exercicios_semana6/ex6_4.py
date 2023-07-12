"""Exercício 6.4 - Números próximos"""


def proximos(valor, margem, lista):
    total = 0
    for elem in lista:
        if elem >= valor - margem and elem <= valor + margem:
            total += 1
    return total

    # Outras condicionais válidas:
    # if abs(elem - valor) <= margem:
    # if valor - margem <= elem <= valor + margem:


print(proximos(2, 1, [3, 2, 1, 1, 4, 5, 2, -2]))
