"""Exercício 6.1 - Média de notas"""

n = int(input("Digite o número de notas: "))
notas = []

# Lê as notas
for _ in range(n):
    nota = int(input())
    notas += [nota]

# Calcula a média
soma = 0
for elem in notas:
    soma += elem
media = soma / len(notas)  # media = sum(notas) / len(notas)

# Mostra o resultado
print("Lista:", notas)
print("Média:", media)
