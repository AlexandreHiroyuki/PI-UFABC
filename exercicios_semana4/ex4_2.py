"""Exercício 4.2 - Número palíndromo"""


def num_digitos(n):
    """Retorna o número de dígitos de um inteiro positivo."""
    total = 0
    while n > 0:
        n //= 10
        total += 1
    return total


def palindromo(n):
    """Retorna True se o inteiro n é um palíndromo."""
    nd = num_digitos(n)
    for i in range(nd // 2):
        di = (n // 10**i) % 10
        es = (n // 10 ** (nd - i - 1)) % 10
        if es != di:
            return False
    return True


print(palindromo(123321))
print(palindromo(1234321))
print(palindromo(7))
print(palindromo(44))
print(palindromo(123))
print(palindromo(537))
print(palindromo(73865837))
