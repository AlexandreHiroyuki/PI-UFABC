"""Exercício 2.5 - Tipo de triângulo"""

x = float(input("Comprimento 1: "))
y = float(input("Comprimento 2: "))
z = float(input("Comprimento 3: "))

if (x > 0 and y > 0 and z > 0) and (x + y > z and x + z > y and y + z > x):
    if x == y and y == z:
        print("Equilátero")
    elif x == y or y == z or x == z:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não é um triângulo")
