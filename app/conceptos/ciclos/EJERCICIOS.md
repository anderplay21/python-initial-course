# Ejercicios de ciclos

Objetivo: practicar ciclos `for` y `while`.

## Archivos

- `ejercicio_1.py`
- `ejercicio_2.py`
- `ejercicio_3.py`

## Como resolver

1. Ejecuta el ejercicio.
2. Cambia el rango o la condicion para ver otros resultados.

## Como ejecutar

```bash
python app/conceptos/ciclos/ejercicios/ejercicio_1.py
python app/conceptos/ciclos/ejercicios/ejercicio_2.py
python app/conceptos/ciclos/ejercicios/ejercicio_3.py
```

## Como ejecutar con Docker

Primero construye la imagen (solo una vez):

```bash
docker build -t hola-mundo .
```

Luego ejecuta los ejercicios montando el proyecto:

```bash
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/ciclos/ejercicios/ejercicio_1.py
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/ciclos/ejercicios/ejercicio_2.py
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/ciclos/ejercicios/ejercicio_3.py
```

Notas para Windows:
- PowerShell: usa `${PWD}` tal como esta.
- CMD: reemplaza `${PWD}` por `%cd%`.
