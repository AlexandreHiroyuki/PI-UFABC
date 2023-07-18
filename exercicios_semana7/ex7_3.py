"""Exercício 7.3 - Quantidade de duplicados"""


def contar_duplicados(x):
    y = set(x)
    total = 0
    for elem in y:
        if x.count(elem) > 1:
            total += 1
    return total


print(contar_duplicados([10]))  # 0
print(contar_duplicados([10, 10, 10, 10]))  # 1
print(contar_duplicados([10, 2, 2, 7, 10, 10]))  # 2
print(contar_duplicados(["UFABC", 2, True, 3.0, "ufabc"]))  # 0
