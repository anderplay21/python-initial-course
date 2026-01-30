# Ejercicio 3: costo total con descuento

# Objetivo: calcular un total con descuento de forma simple.
# 1) Cambia el precio y la cantidad.
# 2) Si la cantidad es 10 o mas, aplica 10% de descuento.
# 3) Imprime el total final.

precio = 5.0
cantidad = 12

subtotal = precio * cantidad

if cantidad >= 10:
    descuento = subtotal * 0.10
else:
    descuento = 0.0

total = subtotal - descuento

print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Total:", total)
