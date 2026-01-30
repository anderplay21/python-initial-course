# Ejercicio 3: suma de numeros

# Objetivo: sumar una secuencia con un ciclo.
# 1) Cambia el valor de n.
# 2) Suma los numeros del 1 al n.
# 3) Imprime el resultado.

n = 5
total = 0

for numero in range(1, n + 1):
    total += numero

print("Suma:", total)
