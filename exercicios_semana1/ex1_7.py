"""Exercício 1.7 - Equação de segundo grau"""

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))

delta = b**2 - 4 * a * c
raiz_do_delta = delta**0.5
denominador = 2 * a

x1 = (-b + raiz_do_delta) / denominador
x2 = (-b - raiz_do_delta) / denominador

print(f"As raízes são x1 = {x1:.2f} e x2 = {x2:.2f}")
