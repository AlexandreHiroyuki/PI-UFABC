"""Exercício 7.6 - Jogo da Forca"""


palavra_oculta = "samambaias"
tentativas = 5
acertos = set()

print("** Jogo da Forca **")

while tentativas > 0:
    # Imprime palavra
    print("Palavra: ", end="")
    for c in palavra_oculta:
        print(c if c in acertos else "_", end="")
    print()

    # Pede uma letra e verifica se houve acerto
    letra = input("Adivinhe a letra: ")
    if letra in palavra_oculta:
        acertos.add(letra)
        # Verifica se ganhou
        if acertos == set(palavra_oculta):
            break
        print("Acertou!")
    else:
        tentativas -= 1
        if tentativas > 0:
            print("Tentativas restantes:", tentativas)
        else:
            print("Errou!")

    print()

if tentativas > 0:
    print("Você ganhou!")
else:
    print("Acabaram suas tentativas.")

print(f"A palavra era {palavra_oculta}.")

