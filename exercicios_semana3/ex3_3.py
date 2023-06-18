"""Exercício 3.3 - Evitando loop infinito"""

n = int(input("Digite o n: "))

while n > 0:  # Nova condição evita loop infinito se n < 0
    print(n)
    n -= 1
