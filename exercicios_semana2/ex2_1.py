"""Exercício 2.1 - Maioridade e voto obrigatório"""

idade = int(input("Qual é a sua idade? "))

if idade < 18:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")

if idade < 16:
    print("Você ainda não pode votar.")
elif idade < 18 or idade >= 70:
    print("Seu voto é facultativo.")
else:
    print("Seu voto é obrigatório.")
