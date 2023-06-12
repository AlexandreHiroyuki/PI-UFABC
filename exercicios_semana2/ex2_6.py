"""Exercício 2.6 - Ordem crescente"""

print("Entre com os três números:")
x = float(input())
y = float(input())
z = float(input())

# Permutações:
# x < y < z
# x < z < y
# y < x < z
# y < z < x
# z < x < y
# z < y < x

print("Em ordem crescente:")

if x < y and x < z:
    # x é o menor
    if y < z:
        print(x, y, z)
    else:
        print(x, z, y)
elif y < x and y < z:
    # y é o menor
    if x < z:
        print(y, x, z)
    else:
        print(y, z, x)
else:
    # z é o menor
    if x < y:
        print(z, x, y)
    else:
        print(z, y, x)
