"""Exercício 2.8 - Dígitos ímpares em um número de até 3 dígitos"""

n = int(input("Digite um número inteiro de até 3 dígitos: "))

impares = 0
digito1 = n % 10
digito2 = (n // 10) % 10
digito3 = (n // 100) % 10

impares += digito1 % 2
impares += digito2 % 2
impares += digito3 % 2

if impares == 0:
    print(f"Não há dígitos ímpares em {n:03}.")
elif impares == 1:
    print(f"Há apenas 1 dígito ímpar em {n:03}.")
else:
    print(f"Há {impares} dígitos ímpares em {n:03}.")
