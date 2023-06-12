"""Exercício 2.3 - Ano bissexto"""

ano = int(input("Qual é o ano? "))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")
