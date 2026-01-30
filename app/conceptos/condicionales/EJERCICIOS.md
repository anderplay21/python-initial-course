# Ejercicios de condicionales

Objetivo: practicar decisiones con `if`, `elif` y `else`.

## Archivos

- `ejercicio_1.py`
- `ejercicio_2.py`
- `ejercicio_3.py`

## Como resolver

1. Cambia los valores iniciales.
2. Ejecuta el archivo y observa la salida.

## Como ejecutar

```bash
python app/conceptos/condicionales/ejercicios/ejercicio_1.py
python app/conceptos/condicionales/ejercicios/ejercicio_2.py
python app/conceptos/condicionales/ejercicios/ejercicio_3.py
```

## Como ejecutar con Docker

Primero construye la imagen (solo una vez):

```bash
docker build -t hola-mundo .
```

Luego ejecuta los ejercicios montando el proyecto:

```bash
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/condicionales/ejercicios/ejercicio_1.py
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/condicionales/ejercicios/ejercicio_2.py
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/condicionales/ejercicios/ejercicio_3.py
```

Notas para Windows:
- PowerShell: usa `${PWD}` tal como esta.
- CMD: reemplaza `${PWD}` por `%cd%`.
