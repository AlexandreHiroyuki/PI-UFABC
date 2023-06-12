"""Exercício 2.4 - Estrela da Morte"""

cx1 = float(input("Coordenada x do centro da circunferência 1: "))
cy1 = float(input("Coordenada y do centro da circunferência 1: "))
r1 = float(input("Raio da circunferência 1: "))

cx2 = float(input("Coordenada x do centro da circunferência 2: "))
cy2 = float(input("Coordenada y do centro da circunferência 2: "))
r2 = float(input("Raio da circunferência 2: "))

dx = cx1 - cx2
dy = cy1 - cy2
distancia_entre_centros = (dx * dx + dy * dy) ** 0.5

if abs(r2 - r1) > 5 and distancia_entre_centros <= max(r1, r2) - min(r1, r2):
    print("É uma Estrela da Morte! Chame o Luke!")
else:
    print("Ufa, não é uma Estrela da Morte.")
