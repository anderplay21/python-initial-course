# Reto de proyecto: Lista de tareas

En este reto vas a crear un programa de consola para administrar tareas.
Usaras variables, condicionales, ciclos, listas y funciones.

## Objetivo

Crear un programa que permita:
- Agregar tareas
- Ver todas las tareas
- Marcar tareas como completadas
- Salir del programa

## Estructura sugerida

Crea un archivo llamado `proyecto/main.py` con este esquema:

1. Una lista para guardar las tareas.
2. Un menu que se repite con un ciclo `while`.
3. Funciones para cada opcion del menu.

## Ejemplo de menu (texto)

```
1. Agregar tarea
2. Ver tareas
3. Completar tarea
4. Salir
```

## Pasos detallados

1. Crea la lista `tareas = []`.
2. Crea una funcion `mostrar_menu()` que imprima el menu.
3. Crea una funcion `agregar_tarea(tareas)` que pida el texto y lo agregue.
4. Crea una funcion `ver_tareas(tareas)` que muestre cada tarea con su numero.
5. Crea una funcion `completar_tarea(tareas)` que:
   - Pida el numero de la tarea.
   - Valide que el numero exista.
   - Muestre un mensaje de confirmacion.
6. En el `while`, pide la opcion con `input()` y usa `if/elif/else`.
7. Si la opcion es 4, termina el programa.

## Validaciones simples (importante)

- Si la lista esta vacia, muestra "No hay tareas".
- Si el usuario escribe una opcion invalida, muestra un mensaje y continua.
- Si la tarea no existe, explica el error.

## Como ejecutar el proyecto

Desde la raiz del proyecto:

```bash
python proyecto/main.py
```

Si ves mensajes "TODO", significa que aun debes completar esa parte.
Sigue los comentarios dentro del archivo `proyecto/main.py`.

## Extra opcional

- Permite borrar una tarea.
- Permite editar el texto de una tarea.
