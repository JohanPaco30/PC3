import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area1 = math.pi * (self.radio ** 2)
        return area1

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        area2 = self.largo * self.ancho
        return area2
    
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        area3 = self.lado ** 2
        return area3

def calcular_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    circulo = Circulo(radio)
    area1 = round(circulo.calcular_area(), 2)
    print(f"El área del círculo es: {area1} metros cuadrados.")

def calcular_rectangulo():
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    rectangulo = Rectangulo(largo, ancho)
    area2 = round(rectangulo.calcular_area(), 2)
    print(f"El área del rectángulo es: {area2} metros cuadrados.")

def calcular_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    cuadrado = Cuadrado(lado)
    area3 = round(cuadrado.calcular_area(), 2)
    print(f"El área del cuadrado es: {area3} metros cuadrados.")

