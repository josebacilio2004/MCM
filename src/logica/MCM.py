# mcm_library.py

import math


def gcd(a, b):
    """Calcula el Máximo Común Divisor (MCD) de dos números usando el algoritmo de Euclides."""
    while b:
        a, b = b, a % b
    return a


def lcm_two(a, b):
    """Calcula el Mínimo Común Múltiplo (MCM) de dos números."""
    return (a * b) // gcd(a, b)


def gcd_three(a, b, c):
    """Calcula el MCD de tres números, usando el MCD en pares."""
    return gcd(gcd(a, b), c)


def lcm_three(a, b, c):
    """Calcula el MCM de tres números."""
    return (a * b * c) // gcd_three(a, b, c)


def input_and_calculate_lcm():
    """Solicita al usuario el número de valores y calcula el MCM de dos o tres números."""
    print("Seleccione el tipo de cálculo para el Mínimo Común Múltiplo (MCM):")
    print("1. Dos números")
    print("2. Tres números")

    choice = input("Ingrese su opción (1 o 2): ")

    if choice == '1':
        # Para dos números
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        result = lcm_two(a, b)
        print(f"El MCM de {a} y {b} es: {result}")

    elif choice == '2':
        # Para tres números
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        c = int(input("Ingrese el tercer número: "))
        result = lcm_three(a, b, c)
        print(f"El MCM de {a}, {b} y {c} es: {result}")

    else:
        print("Opción no válida. Por favor, intente de nuevo.")


# Ejecutar la función de entrada de datos solo si este script se ejecuta directamente
if __name__ == "__main__":
    input_and_calculate_lcm()