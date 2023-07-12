"""Exercício 6.12 - ISBN"""


def isbn(codigo):
    codigo = codigo.replace("-", "")
    mul = 10
    soma = 0
    for c in codigo:
        n = 10 if c == "X" else int(c)
        soma += n * mul
        mul -= 1
    return soma % 11 == 0


print(isbn("3-598-21508-8"))  # True
print(isbn("3598215088"))  # True
print(isbn("3-598-21507-X"))  # True
print(isbn("359821507-X"))  # True
print(isbn("4-1031-45622-9"))  # False
