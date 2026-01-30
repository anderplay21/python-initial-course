# Ejercicio 4: ingresar datos por teclado

# Objetivo: pedir datos al usuario y mostrarlos.
# Este ejercicio es como el ejemplo basico, pero usando input().

nombre = input("Ingresa tu nombre: ")
edad_texto = input("Ingresa tu edad: ")
altura_texto = input("Ingresa tu altura (ejemplo 1.65): ")
es_estudiante_texto = input("Eres estudiante? (si/no): ")

edad = int(edad_texto)
altura = float(altura_texto)
es_estudiante = es_estudiante_texto.strip().lower() == "si"

print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("Es estudiante:", es_estudiante)
