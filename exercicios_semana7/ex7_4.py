"""Exercício 7.4 - Enumerar duplicados"""


def enumerar_duplicados(x):
    y = set(x)
    duplicados = set()
    for elem in y:
        if x.count(elem) > 1:
            duplicados.add(elem)
    return duplicados


print(enumerar_duplicados([10]))  # set()
print(enumerar_duplicados([10, 10, 10, 10]))  # {10}
print(enumerar_duplicados([10, 2, 2, 7, 10, 10]))  # {10, 2}
print(enumerar_duplicados(["UFABC", 2, True, 3.0, "ufabc"]))  # set()
