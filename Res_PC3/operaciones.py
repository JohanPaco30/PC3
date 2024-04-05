def suma(num1: float, num2: float)-> float:
    try:
        resultado = num1 + num2
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def resta(num1: float, num2: float)-> float:
    try:
        resultado = num1 - num2
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def producto(num1: float, num2: float)-> float:
    try:
        resultado = num1 * num2
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def division(num1: float, num2: float)-> float:
    try:
        if num2 == 0:
            return "Error: No es posible dividir entre cero"
        resultado = num1 / num2
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"