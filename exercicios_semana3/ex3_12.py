"""Exercício 3.12 - Fibonacci"""

n = int(input("Digite o n: "))

a = 0
b = 1

if n >= 1:
    print(a)
if n >= 2:
    print(b)

for i in range(3, n + 1):
    a, b = b, a + b
    print(b)
