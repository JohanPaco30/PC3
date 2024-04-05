import random

def generar_numeros_aleatorios():
    numeros = [random.randint(0, 100) for _ in range(20)]
    return numeros

lista_azar = generar_numeros_aleatorios()
print(f"Lista al azar:\n {lista_azar}")

lista_azar.sort()
print(f"Lista ordenada:\n {lista_azar}")