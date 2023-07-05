"""Menor múltiplo de 3"""


import math

n = int(input("Entre a quantidade de números: "))
md3 = math.inf
for i in range(n):
    x = int(input())
    if x % 3 == 0:
        md3 = min(md3, x)

if md3 != math.inf:
    print("O menor número divisível por 3 é", md3)
else:
    print("Nenhum número é divisível por 3")

