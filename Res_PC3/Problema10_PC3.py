from Resolucion_PC3 import CIRCULO, RECTANGULO

print("""Menú:
1. Calcular el área de un círculo
2. Calcular el área de un rectángulo
3. Calcular el área de un cuadrado
4. Salir""")

opcion = input("Seleccione una opción: ")
   
def main():
    while True:

        if opcion == '1':
            entrada = float(input("Ingrese el radio del círculo: "))
            radio = radio.append(entrada)
            area = round(radio.area_c(),2)
            print(f"El área del círculo es: {area}")
        elif opcion == '2':
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            rectangulo = RECTANGULO(largo, ancho)
            area = round(rectangulo.area_cuad(),2)
            print(f"El área del rectángulo es: {area}")
        elif opcion == '3':
            lado = float(input("Ingrese el lado del cuadrado: "))
            area_cuadrado = lado ** 2
            print(f"El área del cuadrado es: {area_cuadrado}")
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()