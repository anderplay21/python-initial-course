# Mas ejemplos de funciones

def sumar(a: int, b: int) -> int:
    return a + b


resultado = sumar(3, 5)
print("Resultado de sumar:", resultado)

# Funcion que recibe una lista y devuelve su longitud.
def contar_elementos(items: list[str]) -> int:
    return len(items)


cantidad = contar_elementos(["a", "b", "c"])
print("Cantidad de elementos:", cantidad)
