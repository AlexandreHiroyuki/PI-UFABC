"""Exercício 2.2 - Ponto no círculo"""

x = float(input("Coordenada x do ponto: "))
y = float(input("Coordenada y do ponto: "))
raio = float(input("Raio do círculo: "))
cx = float(input("Coordenada x do centro do círculo: "))
cy = float(input("Coordenada y do centro do círculo: "))

dx = x - cx
dy = y - cy
distancia = (dx * dx + dy * dy) ** 0.5

if distancia <= raio:
    print(f"O ponto ({x}, {y}) está DENTRO do círculo!")
else:
    print(f"O ponto ({x}, {y}) está FORA do círculo!")

# dentro_ou_fora = "DENTRO" if distancia <= raio else "FORA"
# print(f"O ponto ({x}, {y}) está {dentro_ou_fora} do círculo!")

print(f"A distância até o centro do círculo é {distancia:.2f}.")
