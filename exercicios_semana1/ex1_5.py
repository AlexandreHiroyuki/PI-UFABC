"""Exercício 1.5 - Parte inteira e parte fracionária"""

x = float(input("Digite um número real: "))

inteira = int(x)
fracionaria = x - inteira  # Também funciona com x % 1

print(f"A parte inteira é {inteira}, e a parte fracionária é {fracionaria}.")

# Dica: para a parte fracionária não incluir o erro de precisão númerica, use
# {fracionaria:g} na f-string.
