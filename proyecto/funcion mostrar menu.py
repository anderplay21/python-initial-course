def mostrar_menu() -> None:
    #Imprime el menu con las opciones.
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Salir")

def main() -> None:
    tareas: list[str] = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ").strip()
        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opcion invalida. Intenta de nuevo.")
        print()


if __name__ == "__main__":
    main()
