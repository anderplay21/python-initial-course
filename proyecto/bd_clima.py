bd_clima =[
    {
     "ciudad": "Medellin",
     "clima": "Parcialmente nublado",
     "temperatura": "24°",
     "sensacion_termica": "26°",
     "humedad": "70%",
     "viento": "15 K/H"
    },
    {
     "ciudad": "Bogota",
     "clima": "Luvioso",
     "temperatura": "13°",
     "sensacion_termica": "10°",
     "humedad": "85%",
     "viento": "20 K/H"
    },
    {
     "ciudad": "Cali",
     "clima": "Soleado",
     "temperatura": "30°",
     "sensacion_termica": "34°",
     "humedad": "60%",
     "viento": "10 K/H"
    },
    {
     "ciudad": "Barranquilla",
     "clima": "Caluroso y humedo",
     "temperatura": "35°",
     "sensacion_termica": "40°",
     "humedad": "90%",
     "viento": "25 K/H"
    },
    {
     "ciudad": "Cartagena",
     "clima": "Despejado",
     "temperatura": "33°",
     "sensacion_termica": "37°",
     "humedad": "78%",
     "viento": "18 K/H"
    },
    {
     "ciudad": "Manizales",
     "clima": "Nublado con brisa",
     "temperatura": "17°",
     "sensacion_termica": "14°",
     "humedad": "75%",
     "viento": "22 K/H"
    }
     
]

ciudad_clima = input("Ingresa el nombre de una Ciudad: ")
encontrada=False

for registro in bd_clima:
    if registro["ciudad"] == ciudad_clima:
        encontrada=True
        print("ciudad encontrada")
        break
    else: input("Ingresa el nombre de una Ciudad: ")