"""Exercício 1.3 - Média de notas"""

nota1 = float(input("Digite a nota 1 (de 0 a 10): "))
nota2 = float(input("Digite a nota 2 (de 0 a 10): "))
epsilon = float(input("Digite o epsilon (de 0 a 0.5): "))

media = nota1 * 0.4 + nota2 * 0.6 + epsilon

# Não permite notas maiores que 10
media = min(media, 10)

print(f"A média é {media}")
