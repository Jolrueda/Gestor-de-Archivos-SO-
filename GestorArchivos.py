import os
import shutil
import datetime
from pathlib import Path

CARPETA_BASE = "GESTOR_SO"

if not os.path.exists(CARPETA_BASE):
    os.makedirs(CARPETA_BASE)

def obtener_ruta(nombre):
    return os.path.join(CARPETA_BASE, nombre)

def crear_directorio():
    nombre = input("Ingresa el nombre de la nueva carpeta: ")
    ruta = obtener_ruta(nombre)
    try:
        os.makedirs(ruta, exist_ok=False)
        print(f"Carpeta '{nombre}' creada exitosamente.")
    except FileExistsError:
        print(f"Error: La carpeta '{nombre}' ya existe.")
    except Exception as e:
        print(f"Error al crear la carpeta: {e}")

def crear_archivo_texto():
    nombre = input("Ingresa el nombre del archivo (con extensión .txt): ")
    if not nombre.endswith('.txt'):
        nombre += '.txt'
    ruta = obtener_ruta(nombre)
    
    if os.path.exists(ruta):
        print(f"Error: El archivo '{nombre}' ya existe.")
    else:
        try:
            with open(ruta, 'w') as archivo:
                pass 
            print(f"Archivo '{nombre}' creado exitosamente.")
        except Exception as e:
            print(f"Error al crear el archivo: {e}")

def escribir_archivo():
    nombre = input("Ingresa el nombre del archivo al que deseas agregar información: ")
    ruta = obtener_ruta(nombre)
    
    if not os.path.exists(ruta):
        print(f"Error: El archivo '{nombre}' no existe.")
        return
        
    texto = input("Escribe el texto que deseas agregar: ")
    try:
        with open(ruta, 'a') as archivo:
            archivo.write(texto + "\n")
        print("Información agregada correctamente.")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")

def leer_archivo():
    nombre = input("Ingresa el nombre del archivo que deseas leer: ")
    ruta = obtener_ruta(nombre)
    
    if not os.path.exists(ruta):
        print(f"Error: El archivo '{nombre}' no existe.")
        return
        
    try:
        with open(ruta, 'r') as archivo:
            contenido = archivo.read()
            print("\n--- Contenido del archivo ---")
            print(contenido if contenido else "(El archivo está vacío)")
            print("-----------------------------\n")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

def renombrar_archivo():
    nombre_actual = input("Ingresa el nombre actual del archivo: ")
    ruta_actual = obtener_ruta(nombre_actual)
    
    if not os.path.exists(ruta_actual):
        print(f"Error: El archivo '{nombre_actual}' no existe.")
        return
        
    nuevo_nombre = input("Ingresa el nuevo nombre: ")
    ruta_nueva = obtener_ruta(nuevo_nombre)
    
    if os.path.exists(ruta_nueva):
        print(f"Error: Ya existe un archivo con el nombre '{nuevo_nombre}'.")
        return
        
    try:
        os.rename(ruta_actual, ruta_nueva)
        print(f"Archivo renombrado a '{nuevo_nombre}' exitosamente.")
    except Exception as e:
        print(f"Error al renombrar: {e}")

def copiar_archivo():
    nombre_origen = input("Ingresa el nombre del archivo a copiar: ")
    ruta_origen = obtener_ruta(nombre_origen)
    
    if not os.path.exists(ruta_origen):
        print(f"Error: El archivo '{nombre_origen}' no existe.")
        return
        
    nombre_destino = input("Ingresa el nombre de la copia: ")
    ruta_destino = obtener_ruta(nombre_destino)
    
    if os.path.exists(ruta_destino):
        print(f"Error: Ya existe un archivo con el nombre '{nombre_destino}'.")
        return
        
    try:
        shutil.copy2(ruta_origen, ruta_destino)
        print(f"Archivo copiado exitosamente como '{nombre_destino}'.")
    except Exception as e:
        print(f"Error al copiar: {e}")

def eliminar_archivo():
    nombre = input("Ingresa el nombre del archivo/carpeta a eliminar: ")
    ruta = obtener_ruta(nombre)
    
    if not os.path.exists(ruta):
        print(f"Error: El archivo o carpeta '{nombre}' no existe.")
        return
        
    confirmacion = input(f"¿Estás seguro que deseas eliminar '{nombre}'? (s/n): ").lower()
    if confirmacion == 's':
        try:
            if os.path.isdir(ruta):
                os.rmdir(ruta) # Solo elimina carpetas vacías
            else:
                os.remove(ruta)
            print(f"'{nombre}' eliminado exitosamente.")
        except OSError:
            print(f"Error: La carpeta no está vacía o no se puede eliminar.")
        except Exception as e:
            print(f"Error al eliminar: {e}")
    else:
        print("Operación cancelada.")

def listar_archivos():
    try:
        elementos = os.listdir(CARPETA_BASE)
        if not elementos:
            print("La carpeta GESTOR_SO está vacía.")
            return
            
        print("\n--- Contenido de GESTOR_SO ---")
        for item in elementos:
            ruta_item = obtener_ruta(item)
            tipo = "Carpeta" if os.path.isdir(ruta_item) else "Archivo"
            print(f"- {item} ({tipo})")
        print("------------------------------\n")
    except Exception as e:
        print(f"Error al listar el directorio: {e}")

def consultar_info():
    nombre = input("Ingresa el nombre del archivo o carpeta para consultar su información: ")
    ruta = obtener_ruta(nombre)
    
    if not os.path.exists(ruta):
        print(f"Error: El archivo o carpeta '{nombre}' no existe.")
        return
        
    try:
        tamaño = os.path.getsize(ruta)
        fecha_mod = os.path.getmtime(ruta)
        fecha_legible = datetime.datetime.fromtimestamp(fecha_mod).strftime('%Y-%m-%d %H:%M:%S')
        
        print("\n--- Información ---")
        print(f"Nombre: {nombre}")
        print(f"Tamaño: {tamaño} bytes")
        print(f"Última modificación: {fecha_legible}")
        print("-------------------\n")
    except Exception as e:
        print(f"Error al consultar información: {e}")

def main():
    while True:
        print("\n" + "="*30)
        print("   GESTOR DE ARCHIVOS")
        print("="*30)
        print("1. Crear un directorio")
        print("2. Crear un archivo de texto")
        print("3. Escribir información en un archivo")
        print("4. Leer el contenido de un archivo")
        print("5. Renombrar un archivo")
        print("6. Copiar un archivo")
        print("7. Eliminar un archivo")
        print("8. Listar archivos de un directorio")
        print("9. Consultar información de un archivo")
        print("0. Salir")
        print("="*30)
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            crear_directorio()
        elif opcion == '2':
            crear_archivo_texto()
        elif opcion == '3':
            escribir_archivo()
        elif opcion == '4':
            leer_archivo()
        elif opcion == '5':
            renombrar_archivo()
        elif opcion == '6':
            copiar_archivo()
        elif opcion == '7':
            eliminar_archivo()
        elif opcion == '8':
            listar_archivos()
        elif opcion == '9':
            consultar_info()
        elif opcion == '0':
            print("Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()