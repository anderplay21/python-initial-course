# Ejercicios de listas

Objetivo: practicar crear y recorrer listas.

## Archivos

- `ejercicio_1.py`
- `ejercicio_2.py`
- `ejercicio_3.py`

## Como resolver

1. Agrega o cambia elementos de la lista.
2. Ejecuta y observa la salida.

## Como ejecutar

```bash
python app/conceptos/listas/ejercicios/ejercicio_1.py
python app/conceptos/listas/ejercicios/ejercicio_2.py
python app/conceptos/listas/ejercicios/ejercicio_3.py
```

## Como ejecutar con Docker

Primero construye la imagen (solo una vez):

```bash
docker build -t hola-mundo .
```

Luego ejecuta los ejercicios montando el proyecto:

```bash
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/listas/ejercicios/ejercicio_1.py
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/listas/ejercicios/ejercicio_2.py
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/listas/ejercicios/ejercicio_3.py
```

Notas para Windows:
- PowerShell: usa `${PWD}` tal como esta.
- CMD: reemplaza `${PWD}` por `%cd%`.
