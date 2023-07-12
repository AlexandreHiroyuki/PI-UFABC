"""Exercício 6.11 - Isograma"""


# Solução usando histograma com ord()
def isograma(texto):
    texto = texto.replace(" ", "")
    texto = texto.replace("-", "")
    histograma = [0] * 255
    for c in texto:
        indice = ord(c)
        if histograma[indice] > 0:
            return False
        histograma[indice] += 1
    return True


# Solução usando apenas o operador in
# def isograma(texto):
#     letras_visitadas = ""
#     for c in texto:
#         if c in " -":
#             continue
#         if c in letras_visitadas:
#             return False
#         letras_visitadas += c
#     return True

# Solução sem o operador in e sem histograma
# def isograma(texto):
#     n = len(texto)
#     for i in range(n):
#         c = texto[i]
#         if c == " " or c == "-":
#             continue
#         for j in range(i + 1, n):
#             if c == texto[j]:
#                 return False
#     return True


print(isograma("UFABC"))  # True
print(isograma("abacate"))  # False
print(isograma("hoje fui mal"))  # True
print(isograma("vê-lo-ias"))  # True

