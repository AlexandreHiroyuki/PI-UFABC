"""Exercício 6.10 - Distância de Hamming entre sequências de DNA"""


def hamming_dna(a, b):
    if len(a) != len(b):
        return -1
    dist = 0
    for i in range(len(a)):
        ca = a[i]
        cb = b[i]
        if ca not in "CAGT" or cb not in "CAGT":
            return -1
        if ca != cb:
            dist += 1
    return dist


# Usando zip
def hamming_dna2(a, b):
    if len(a) != len(b):
        return -1
    dist = 0
    for ca, cb in zip(a, b):
        if ca not in "CAGT" or cb not in "CAGT":
            return -1
        if ca != cb:
            dist += 1
    return dist


print(hamming_dna("CTAGGT", "CTAGGT"))  # 0
print(hamming_dna("AGTGAT", "CTAGGT"))  # 4
print(hamming_dna("AGTGA", "CTAGGT"))  # -1
print(hamming_dna("AGTGAX", "CTAGGT"))  # -1

