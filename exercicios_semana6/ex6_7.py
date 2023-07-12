"""Exercício 6.7 - Removendo caracteres"""


def remove_caractere(texto, caractere):
    res = ""
    for c in texto:
        if c != caractere:
            res += c
    return res


print(remove_caractere("papagaio", "a"))
print(remove_caractere("computador", "i"))
