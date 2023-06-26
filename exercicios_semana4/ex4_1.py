"""Exercício 4.1 - Cara ou coroa"""
import random

jogada = int(input("Cara (0) ou coroa (1)? "))

sorteio = random.randint(0, 1)

if jogada == sorteio:
    print("Acertou!")
else:
    print("Errou!")

if sorteio == 0:
    sorteio_str = "CARA"
else:
    sorteio_str = "COROA"

# Forma mais simples:
# sorteio_str = "COROA" if sorteio else "CARA"

print(f"Foi sorteado {sorteio} ({sorteio_str}).")
