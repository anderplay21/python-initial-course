# Ejercicios de funciones

Objetivo: practicar crear y usar funciones.

## Archivos

- `ejercicio_1.py`
- `ejercicio_2.py`
- `ejercicio_3.py`

## Como resolver

1. Lee lo que hace la funcion.
2. Cambia los valores y vuelve a ejecutar.

## Como ejecutar

```bash
python app/conceptos/funciones/ejercicios/ejercicio_1.py
python app/conceptos/funciones/ejercicios/ejercicio_2.py
python app/conceptos/funciones/ejercicios/ejercicio_3.py
```

## Como ejecutar con Docker

Primero construye la imagen (solo una vez):

```bash
docker build -t hola-mundo .
```

Luego ejecuta los ejercicios montando el proyecto:

```bash
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/funciones/ejercicios/ejercicio_1.py
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/funciones/ejercicios/ejercicio_2.py
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/funciones/ejercicios/ejercicio_3.py
```

Notas para Windows:
- PowerShell: usa `${PWD}` tal como esta.
- CMD: reemplaza `${PWD}` por `%cd%`.
