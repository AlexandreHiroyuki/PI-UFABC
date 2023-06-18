"""Exercício 3.11 - FizzBuzz"""

n = int(input("Digite o n: "))


for i in range(1, n + 1):
    if i % 3 == 0:
        res = "Fizz"
        if i % 5 == 0:
            res += "Buzz"
    elif i % 5 == 0:
        res = "Buzz"
    else:
        res = i
    print(res)
