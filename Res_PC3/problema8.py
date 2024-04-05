import random

def generar_numeros_aleatorios():
    numeros = [random.randint(0, 100) for _ in range(20)]
    return numeros
