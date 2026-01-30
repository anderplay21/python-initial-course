# Instalar Docker en Windows y ejecutar la app

Esta guia explica como instalar Docker Desktop en Windows y ejecutar
la aplicacion dentro de un contenedor.

## 1) Requisitos

- Windows 10/11 actualizado
- Cuenta en Docker Hub (opcional, solo si quieres iniciar sesion)

## 2) Descargar Docker Desktop

1. Entra a: https://www.docker.com/products/docker-desktop/
2. Descarga Docker Desktop para Windows.

## 3) Instalar Docker Desktop

1. Ejecuta el instalador.
2. Acepta el uso de WSL 2 si el instalador lo sugiere.
3. Finaliza la instalacion y reinicia si se solicita.

## 4) Verificar instalacion

Abre PowerShell y ejecuta:

```bash
docker --version
```

Deberias ver una salida similar a:

```text
Docker version 27.x.x, build ...
```

## 5) Construir la imagen

Desde la carpeta del proyecto, ejecuta:

```bash
docker build -t hola-mundo .
```

## 6) Ejecutar la aplicacion

```bash
docker run --rm hola-mundo
```

Para pasar un nombre:

```bash
docker run --rm hola-mundo Ana
```

## 7) Solucion rapida de problemas

- Si Docker no inicia, abre Docker Desktop y espera a que termine de cargar.
- Si ves errores con WSL 2, abre una terminal con permisos de administrador
  y ejecuta: `wsl --update`
