"""Exercício 7.1 - Existência de duplicados (1)"""


# Usando count
def tem_duplicados1(x):
    for elem in x:
        if x.count(elem) > 1:
            return True
    return False


# Sem usar count
# def tem_duplicados1(x):
#     for i in range(len(x)):
#         for j in range(i + 1, len(x)):
#             if x[i] == x[j]:
#                 return True
#     return False


print(tem_duplicados1([10, 2, -3, 7, 11, 10]))  # True
print(tem_duplicados1(["UFABC", 2, True, 3.0, "ufabc"]))  # False
print(tem_duplicados1([10, 2, -3, 7, 11, 3]))  # False
print(tem_duplicados1([True, 1]))  # True
print(tem_duplicados1([3, 3.0]))  # True
