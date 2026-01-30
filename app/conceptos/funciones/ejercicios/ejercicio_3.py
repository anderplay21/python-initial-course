# Ejercicio 3: convertir temperatura

# Objetivo: crear una funcion que convierta de Celsius a Fahrenheit.
# 1) Completa la funcion.
# 2) Imprime el resultado para un valor de ejemplo.

def celsius_a_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


valor = 25.0
print("Fahrenheit:", celsius_a_fahrenheit(valor))
