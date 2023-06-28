"""Exercício 4.4 - Monte Carlo"""
import random


def dentro_do_circulo_unitario(x, y):
    return x * x + y * y <= 1


def pi_mc(n):
    m = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        m += dentro_do_circulo_unitario(x, y)
    return 4 * (m / n)


print(pi_mc(5000000))
