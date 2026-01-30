# Ejercicios de variables

Objetivo: practicar como guardar y usar datos en variables.

## Archivos

- `ejercicio_1.py`
- `ejercicio_2.py`
- `ejercicio_3.py`
- `ejercicio_4.py`

## Como resolver

1. Abre el archivo del ejercicio.
2. Lee los comentarios y completa los valores.
3. Guarda el archivo.

## Como ejecutar

Desde la raiz del proyecto:

```bash
python app/conceptos/variables/ejercicios/ejercicio_1.py
python app/conceptos/variables/ejercicios/ejercicio_2.py
python app/conceptos/variables/ejercicios/ejercicio_3.py
python app/conceptos/variables/ejercicios/ejercicio_4.py
```

## Como ejecutar con Docker

Primero construye la imagen (solo una vez):

```bash
docker build -t hola-mundo .
```

Luego ejecuta los ejercicios montando el proyecto:

```bash
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/variables/ejercicios/ejercicio_1.py
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/variables/ejercicios/ejercicio_2.py
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/variables/ejercicios/ejercicio_3.py
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/variables/ejercicios/ejercicio_4.py
```

Notas para Windows:
- PowerShell: usa `${PWD}` tal como esta.
- CMD: reemplaza `${PWD}` por `%cd%`.

Nota sobre el ejercicio 4:
- Este ejercicio usa `input()` y necesita un contenedor interactivo.
- En Docker usa `-it`, por ejemplo:

```bash
docker run --rm -it -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/variables/ejercicios/ejercicio_4.py
```
