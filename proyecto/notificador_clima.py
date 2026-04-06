# Base de datos del clima

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
    

#Buscar ciudad en la base de datos
def buscar_ciudad(ciudad_clima):
    encontrada = False

    for registro in bd_clima:
        if registro["ciudad"] == ciudad_clima:
            encontrada== True
        break


    return mostrar_datos_del_clima(ciudad_clima)

#Mostrar los datos del clima
def mostrar_datos_del_clima(ciudad_clima):
     for registro in bd_clima:
        if registro["ciudad"] == ciudad_clima:
            print("Ciudad: ", registro["ciudad"])
            print("Clima: ", registro["clima"])
            print("Temperatura: ", registro["temperatura"])
            print("Sensación termica: ", registro["sensacion_termica"])
            print("Humedad: ", registro["humedad"])
            print("Velocidad del viento: ", registro["viento"])


#Solicita el nombre de la ciudad
def main():
    #Mensaje de Bienvenida
    print("Hola. Bienvenido al notificador del clima")
    
    while True:
    ciudad_clima = input("Ingresa el nombre de una ciudad (o escribe 'salir' para terminar): ")
    if ciudad_clima.lower() == "salir":
        print("Gracias por usar el notificador del clima")
        break

    if not ciudad_clima.lower()
    datos_del_clima = buscar_ciudad(ciudad_clima)
    mostrar_datos_del_clima(ciudad_clima)



#inicial funcion Solicitar_ciudad:
if __name__ == "__main__":
    main()