# Ejercicio 2: agregar y recorrer lista

# 1) Crea una lista vacia.
# 2) Agrega tres frutas usando append.
# 3) Recorre la lista e imprime cada fruta.

frutas: list[str] = []
frutas.append("manzana")
frutas.append("banana")
frutas.append("naranja")

for fruta in frutas:
    print(fruta)

motos: list[str]=[]
motos.append("susuki")
motos.append("kawasaki")
motos.append("ktm")
motos.append("yamaha")

for moto in motos:
    print("Esta es la marca de la moto:", moto) 
