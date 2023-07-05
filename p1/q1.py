"""Fases da Lua"""


def lua(m1, m2):
    if m2 <= 2:
        print("Nova")
    elif m2 <= 96:
        if m2 >= m1:
            print("Crescente")
        else:
            print("Minguante")
    else:
        print("Cheia")


lua(0, 2)  # Nova
lua(2, 3)  # Crescente
lua(99, 97)  # Cheia
lua(97, 94)  # Minguante
lua(30, 35)  # Crescente
lua(45, 35)  # Minguante
lua(66, 31)  # Minguante
lua(21, 52)  # Crescente
lua(52, 93)  # Crescente
lua(33, 4)  # Minguante
