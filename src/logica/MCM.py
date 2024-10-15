# mcm_library.py

import math

def gcd(a, b):
    """Calculaa el Máximo Común Divisor (MCD) de dos números usando el algoritmo de Euclides."""
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