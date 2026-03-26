from __future__ import annotations


def mostrar_menu() -> None:
    TODO: #Imprime el menu con las opciones.
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Salir")


def agregar_tarea(tareas: list[str]) -> None:
    texto = input("Escribe la tarea: ").strip()
    if not texto:
        print("La tarea no puede estar vacia.")
        return
    tareas.append(texto)


def ver_tareas(tareas: list[str]) -> None:
    TODO: #Muestra todas las tareas con numero.
    # Si no hay tareas, muestra "No hay tareas."
    print("TODO: Implementar ver_tareas")


def completar_tarea(tareas: list[str]) -> None:
    TODO: #Pide el numero de la tarea a completar y validalo.
    # Si el numero existe, elimina la tarea de la lista.
    print("TODO: Implementar completar_tarea")


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
