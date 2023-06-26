"""Exercício 4.3 - Adivinhe o número"""
import random

print("Adivinhe o número de 1 a 100")

sorteio = random.randint(1, 100)
tentativas = 5

while tentativas > 0:
    print("Tentativas restantes:", tentativas)
    jogada = int(input("Qual é o número: "))

    dif = sorteio - jogada
    if dif == 0:
        break

    dica = "MENOR" if dif < 0 else "MAIOR"
    print(f"Errou. O número sorteado é {dica} que {jogada}")

    tentativas -= 1

if tentativas == 0:
    print("Acabaram suas tentativas.")
else:
    print("Parabéns! Você acertou.")

print("O número sorteado era", sorteio)
