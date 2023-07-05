"""Caixa eletrônico"""


x = int(input("Quanto você quer sacar? "))

n50 = x // 50
x -= n50 * 50

n20 = x // 20
x -= n20 * 20

n5 = x // 5
x -= n5 * 5

if x:
    print("Não é possível sacar esse valor")
else:
    print("Notas de 50:", n50)
    print("Notas de 20:", n20)
    print("Notas de 5:", n5)

