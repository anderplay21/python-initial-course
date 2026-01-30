# Instalar y validar Python en Windows

Esta guia explica como instalar Python y validar que quedo listo en Windows.

## 1) Descargar Python

1. Abre el navegador y entra a: https://www.python.org/downloads/
2. Haz clic en el boton de descarga de la ultima version estable para Windows.

## 2) Instalar Python

1. Ejecuta el instalador que descargaste.
2. Marca la casilla **Add Python to PATH**.
3. Haz clic en **Install Now** y espera a que termine.

## 3) Verificar la instalacion

1. Abre PowerShell o CMD.
2. Ejecuta:

```bash
python --version
```

Deberias ver una salida similar a:

```text
Python 3.13.x
```

Si el comando no funciona, intenta con:

```bash
py --version
```

## 4) Validar que pip este instalado

Ejecuta:

```bash
python -m pip --version
```

Deberias ver una salida con la version de pip.

## 5) Solucion rapida si no aparece Python en PATH

1. Cierra y abre de nuevo la terminal.
2. Si sigue sin funcionar, reinstala Python y asegurate de marcar
   **Add Python to PATH**.
