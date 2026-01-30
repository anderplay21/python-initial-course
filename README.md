# Hola Mundo (Python)

Proyecto basico de Python para principiantes con ejemplos, ejercicios y reto.

Guia completa de ejemplos y ejercicios:
- `GUIA_EJEMPLOS_EJERCICIOS.md`

Documento del curso (razon, actividades, evaluaciones y competencias):
- `DOCUMENTO_CURSO.md`

Guias de instalacion en Windows:
- `INSTALAR_PYTHON_WINDOWS.md`
- `INSTALAR_DOCKER_WINDOWS.md`

## Requisitos

- Python 3.13+
- Docker (opcional)

## Ejecutar en local

```bash
python app/main.py
python app/main.py "Ana"
```

## Ejemplos por conceptos

Puedes ejecutar cada ejemplo de forma independiente:

```bash
python app/conceptos/variables/ejemplo_basico.py
python app/conceptos/variables/mas_ejemplos.py

python app/conceptos/condicionales/ejemplo_basico.py
python app/conceptos/condicionales/mas_ejemplos.py

python app/conceptos/ciclos/ejemplo_basico.py
python app/conceptos/ciclos/mas_ejemplos.py

python app/conceptos/listas/ejemplo_basico.py
python app/conceptos/listas/mas_ejemplos.py

python app/conceptos/funciones/ejemplo_basico.py
python app/conceptos/funciones/mas_ejemplos.py
```

## Ejemplos por conceptos con Docker

Primero construye la imagen:

```bash
docker build -t hola-mundo .
```

Luego ejecuta cada ejemplo montando el proyecto en el contenedor:

```bash
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/variables/ejemplo_basico.py
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/variables/mas_ejemplos.py

docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/condicionales/ejemplo_basico.py
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/condicionales/mas_ejemplos.py

docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/ciclos/ejemplo_basico.py
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/ciclos/mas_ejemplos.py

docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/listas/ejemplo_basico.py
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/listas/mas_ejemplos.py

docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/funciones/ejemplo_basico.py
docker run --rm -v "${PWD}:/app" -w /app hola-mundo python app/conceptos/funciones/mas_ejemplos.py
```

Notas para Windows:
- PowerShell: usa `${PWD}` tal como esta en los ejemplos.
- CMD: reemplaza `${PWD}` por `%cd%`.
