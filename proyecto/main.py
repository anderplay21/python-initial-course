from __future__ import annotations


def mostrar_menu() -> None:
    #Imprime el menu con las opciones.
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Salir")


def agregar_tarea(tareas: list[str]) -> None:
    while True:
        tarea = input("Ingresa tu nueva tarea: ").strip()
        if tarea:
            tareas.append(tarea)
            break
        print("La tarea no puede estar vacia.")
    print("TAREA AGREGADA")


def ver_tareas(tareas: list[str]) -> None:
    if not tareas:
        print("No hay tareas.")
        return

    for numero, tarea in enumerate(tareas, start=1):
        print(f"{numero}. {tarea}")
    


def completar_tarea(tareas: list[str]) -> None:
    if not tareas:
        print("No hay tareas.")
        return

    ver_tareas(tareas)
    while True:
        numero_tarea = input("Ingresa el numero de la tarea a completar: ").strip()
        if not numero_tarea.isdigit():
            print("Ingresa un numero valido.")
            continue

        indice = int(numero_tarea) - 1
        if 0 <= indice < len(tareas):
            tareas.pop(indice)
            print("TAREA COMPLETADA")
            break

        print("Numero de tarea invalido.")


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
