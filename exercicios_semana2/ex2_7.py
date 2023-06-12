"""Exercício 2.7 - Pedra, papel, tesoura"""

print("Digite 0 (pedra), 1 (papel) ou 2 (tesoura)")
j1 = int(input("Jogador 1: "))
j2 = int(input("Jogador 2: "))

if j1 == j2:
    print("Empate")
# elif (j1 == 0 and j2 == 2) or (j1 == 1 and j2 == 0) or (j1 == 2 and j2 == 1):
elif j2 == (j1 + 2) % 3:
    print("Jogador 1 venceu")
else:
    print("Jogador 2 venceu")
