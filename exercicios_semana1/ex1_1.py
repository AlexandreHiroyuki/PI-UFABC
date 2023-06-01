"""Exercício 1.1 - Troca de variáveis"""

x = 42
y = "PI-UFABC"

# Swap usando uma variável adicional
z = x
x = y
y = z

# Outra forma de fazer swap (específico do Python)
# x, y = y, x

print(x)
print(y)
