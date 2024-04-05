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

    print("Calificaciones como enteros:", calificaciones_enteros)


if __name__ == "__main__":
    main()