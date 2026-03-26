# Ejercicio 3: promedio de una lista

# Objetivo: calcular el promedio de una lista de numeros.
# 1) Cambia los valores de la lista.
# 2) Calcula la suma y el promedio.
# 3) Imprime el promedio.

numeros = [10, 8, 6, 9]

suma = 0
for numero in numeros:
    suma += numero

promedio = suma / len(numeros)
print("Promedio:", promedio)

print(numeros)

for numero in numeros:
    print("el numero es igual a: ",numero )