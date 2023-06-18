"""Exercício 3.6 - Soma de série"""

n = int(input("Digite o n: "))

sn = 0
for i in range(n + 1):
    sn += 1 / (2 * i + 1)

# sn = 0
# for i in range(1, 2 * n + 2, 2):
#     sn += 1 / i

print(f"S({n}) = {sn:.2f}")
