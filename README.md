# 📁 Gestor de Archivos en Python

Aplicación de escritorio construida con Python y Tkinter para gestionar archivos y carpetas sin necesidad de utilizar el explorador del sistema operativo. Este proyecto restringe todas sus operaciones a una carpeta segura de trabajo llamada `GESTOR_SO`, evitando modificaciones accidentales a los archivos personales o del sistema.

## 🚀 Características

El sistema cuenta con una interfaz gráfica amigable que permite realizar las siguientes operaciones fundamentales:
- **Crear:** Generar nuevos directorios y archivos de texto plano (.txt).
- **Modificar:** Escribir nueva información (añadir texto) en archivos existentes.
- **Visualizar:** Leer el contenido de los archivos de texto directamente en la aplicación.
- **Gestionar:** Renombrar, copiar y eliminar archivos o carpetas (con advertencias de seguridad).
- **Explorar:** Listar de manera automática todo el contenido de la carpeta de trabajo.
- **Auditar:** Consultar la información detallada de cualquier archivo (tamaño en bytes y fecha exacta de su última modificación).

## 🛠️ Tecnologías utilizadas

- **Lenguaje:** Python 3.x
- **Interfaz Gráfica:** Tkinter (Librería estándar)
- **Módulos estándar:** `os`, `shutil`, `datetime`, `pathlib`

## ⚙️ Instalación y Uso

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone [https://github.com/Jolrueda/Gestor-de-Archivos-SO-.git](https://github.com/Jolrueda/Gestor-de-Archivos-SO-.git)
