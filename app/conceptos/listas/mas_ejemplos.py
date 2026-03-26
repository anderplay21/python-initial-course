# Mas ejemplos de listas

carros = ["mazda cx5", "Toyota Yaris"]
carros.append("BMW")
carros.remove("mazda cx5")
carros.pop(1)
print("Lista completa:", carros)

for carro in carros:
    print("Carros:", carro)