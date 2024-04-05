"""
Problema 1:
Implemente un programa que solicite al usuario una fracción, con
formato X/Y, donde cada uno de X e Y es un número entero, y luego
muestra, como un porcentaje redondeado al número entero más
cercano, donde se indicará la cantidad de combustible en el
tanque.
"""

def cant_combustible (x: int, y: int)-> int:
    assert x <= y, "El numerador no debe superar al demominador."
    return x/y


try:    
    x = int(input("Introduzca el numerador: "))
    y = int(input("Introduzca el denominador: "))

    frac = int(cant_combustible(x,y)*100)

    if frac < 1:
        print("E")
    elif frac > 99:
        print("F")
    else:
        print(f'{frac}%')

except ZeroDivisionError:
        print("""Se detectó un valor nulo en el denominador.
        Inténtelo nuevamente""")
        
        
except ValueError:
        print("Solo numeros enteros. Inténtelo nuevamente")

"""
Problema 2:
Cree un programa que solicite al usuario una lista de calificaciones 
separadas por comas. Divida la cadena en calificaciones individuales y
almacénelas en una lista para luego convertir cada calificación en un entero.
Deberá utilizar una sentencia try/except para informar al usuario cuando los 
valores introducidos no puedan ser convertidos debido a un error de tipeo o
formato. (Los métodos de cadena le serán de utilidad).
"""
def main():
    solicitud = input("Ingrese las calificaciones separadas por comas: ")
    lista = solicitud.split(",")
    cali_enteros = []

    for calificacion in lista:
        try:
            cali_ent = int(calificacion.strip())
            cali_enteros.append(cali_ent)
        except ValueError:
            print(f"Error: '{calificacion.strip()}' no es un número válido.")

    print("Calificaciones ingresadas:", cali_enteros)


if __name__ == "__main__":
    main()

"""
Problema 3:
Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio.Problema 3:
Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio.
"""
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        return area


mi_circulo = Circulo(float(input("Ingrese el radio del circulo: ")))

area_circulo = round(mi_circulo.calcular_area(), 2)
print(f"El área del círculo es: {area_circulo} metros cuadrados.")

"""
Problema 4:
Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
atributos de la clase.
"""
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        area = self.largo * self.ancho
        return area

largo = float(input("Ingerese el largo del rectangulo: "))
ancho = float(input("Ingerese el ancho del rectangulo: "))
mi_rectangulo = Rectangulo(largo = largo, ancho = ancho)

area_rectangulo = round(mi_rectangulo.calcular_area(), 2)
print(f"El área del rectángulo es: {area_rectangulo} metros cuadrados.")

"""
Problema 5:
Cree una clase Alumno e inicialícela con el nombre y el número de registro. Haga los métodos
para:
1. Display - Debe mostrar toda la información del estudiante (nombre y número de
registro).
2. setAge - Debe asignar la edad al estudiante
3. setNota - Debe asignar las notas al estudiante.
"""
class Alumno:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.numero_registro = id
        self.edad = None
        self.notas = []

    def display(self):
        print(f"""Nombre: {self.nombre}
Número de registro: {self.numero_registro}
Edad: {self.edad}
Notas: {self.notas}""")

    def set_age(self, edad):
        self.edad = edad

    def set_notas(self, notas):
        self.notas = notas


alumno = Alumno("Johan", "1416")
alumno.set_age(20)
alumno.set_notas([20,20,20])
alumno.display()


"""
Problema 6:
Una tienda de autopartes necesita un programa para catalogar sus productos, crear la clase
Catálogo y Producto, realizar un objeto dentro de un catálogo productos el cual debe tener un
método para agregar productos y otra para mostrar toda la lista de productos.
Agregar 2 funcionalidades al catálogo (por ejemplo, filtro según año) , asi mismo se puede
agregar más atributos a los productos para que se puedan hacer otras funcionalidades
Guiarse de
https://github.com/gdelgador/ProgramacionPython/blob/main/Modulo3/scripts/clases_objeto
s/catalogo_peliculas.py
"""

class Productos:

    def __init__(self, nombre, precio, marca):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        print('Se ha agregado el producto:', self.nombre)

    def __str__(self):
        return '{} ({} soles)'.format(self.nombre, self.precio)

class Catalogo:

    productos = []

    def __init__(self, productos=[]):
        self.productos = productos

    def agregar(self, p):
        self.productos.append(p)

    def mostrar(self):
        for p in self.productos:
            print(p)


p = Productos(nombre= "Neumatico LTX FORCE", precio=707, marca= "Michelin")
p2 = Productos(nombre= "Bateria 40b19l", precio=327, marca= "BOSCH56")

catalogo_neumaticos = Catalogo([p])
catalogo_baterias = Catalogo([p2])

print("\n En la seccion NEUMATICOS tenemos: ")
catalogo_neumaticos.mostrar()
print("En la seccion BATERIAS tenemos: ")
catalogo_baterias.mostrar()

catalogo_neumaticos.agregar(Productos(nombre='Neumatico PRIMACY 4', precio=766, marca= "Michelin"))
print("\n En la seccion NEUMATICOS tenemos: ")
catalogo_neumaticos.mostrar()

"""
Problema 8:
Desarrollar un módulo que contenga las siguientes funciones:
● Que genere 20 números enteros aleatorios entre 0 y 100 y devuelva una lista.
● Mostrar la lista obtenida por pantalla.
● Ordenar los valores de la lista y mostrarla por pantalla.
Luego crea un script main.py en el mismo directorio en el que deberás importar el módulo y
ejecutar las funciones.
Nota: utilizar el módulo “random” para generar un número aleatorio.
"""

#El modulo con las funciones esta en "problema8.py" y la ejecucion en el archivo "main.py".

"""
Problema 9:
Cree un módulo llamado operaciones.py el cual contendrá 4 funciones para realizar una suma,
una resta, un producto y una división entre dos números. Todas ellas devolverán el resultado.
En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para
evitar que se quede bloqueada una funcionalidad, esto incluye:
● En caso de que se envíen valores a las funciones que no sean números, deberá
aparecer un mensaje que informe Error: Tipo de dato no válido.
● En caso de realizar una división por cero, deberá aparecer un mensaje que informe
Error: No es posible dividir entre cero.
Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás
importar el módulo y ejecutar las funciones.
"""

#Cree un modulo "operaciones.py" y el script "calculos.py" para que ejecutara las 4 funciones.

"""
Problema 10
Cree un menú que reutilice a manera de módulos las clases creadas en los ejercicios 3 y 4. El
menú para utilizar deberá tener las siguientes funcionalidades:
1. Calcular el área de un circulo
2. Calcular el área de un rectangulo
3. Calcular
"""
#Cree un modulo "Clases3y4.py" donde puse las clases y funciones y la ejecute en este archivo la 
#funcion MAIN

import Clases3y4 as CS

def main():
    while True:
        print("""\nMenú de opciones:
1. Calcular el área de un círculo
2. Calcular el área de un rectángulo
3. Calcular el área de un cuadrado")
4. Salir""")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            CS.calcular_circulo()
        elif opcion == 2:
            CS.calcular_rectangulo()
        elif opcion == 3:
            CS.calcular_cuadrado()
        elif opcion == 4:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()