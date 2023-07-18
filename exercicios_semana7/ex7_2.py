"""Exercício 7.2 - Existência de duplicados (2)"""


def tem_duplicados2(x):
    return len(set(x)) < len(x)


print(tem_duplicados2([10, 2, -3, 7, 11, 10]))  # True
print(tem_duplicados2(["UFABC", 2, True, 3.0, "ufabc"]))  # False
print(tem_duplicados2([10, 2, -3, 7, 11, 3]))  # False
print(tem_duplicados2([True, 1]))  # True
print(tem_duplicados2([3, 3.0]))  # True
