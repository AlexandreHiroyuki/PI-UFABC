"""Exercício 1.4 - Ano de nascimento"""

nome = input("Qual é o seu nome? ")
# Obs: Idade supondo que o usuário já fez aniversário neste ano
idade = int(input("Qual é a sua idade? "))

print(f"{nome}, você nasceu no ano {2023 - idade}.")
