import os
import shutil
import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

# Configuración inicial
CARPETA_BASE = "GESTOR_SO"
if not os.path.exists(CARPETA_BASE):
    os.makedirs(CARPETA_BASE)

def obtener_ruta(nombre):
    return os.path.join(CARPETA_BASE, nombre)

class GestorArchivosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Archivos")
        self.root.geometry("500x600")
        self.root.config(padx=20, pady=20)

        # Título
        tk.Label(root, text="GESTOR DE ARCHIVOS", font=("Arial", 16, "bold")).pack(pady=(0, 10))

        # Lista para mostrar archivos
        self.lista_archivos = tk.Listbox(root, width=50, height=10)
        self.lista_archivos.pack(pady=10)
        
        # Botón para actualizar lista manualmente
        tk.Button(root, text="Actualizar Lista", command=self.listar_archivos).pack(pady=(0, 15))

        # Marco para los botones de operaciones
        frame_botones = tk.Frame(root)
        frame_botones.pack(fill="both", expand=True)

        # Crear los botones del menú
        tk.Button(frame_botones, text="1. Crear un directorio", command=self.crear_directorio, width=30).pack(pady=2)
        tk.Button(frame_botones, text="2. Crear un archivo de texto", command=self.crear_archivo_texto, width=30).pack(pady=2)
        tk.Button(frame_botones, text="3. Escribir información en un archivo", command=self.escribir_archivo, width=30).pack(pady=2)
        tk.Button(frame_botones, text="4. Leer el contenido de un archivo", command=self.leer_archivo, width=30).pack(pady=2)
        tk.Button(frame_botones, text="5. Renombrar un archivo", command=self.renombrar_archivo, width=30).pack(pady=2)
        tk.Button(frame_botones, text="6. Copiar un archivo", command=self.copiar_archivo, width=30).pack(pady=2)
        tk.Button(frame_botones, text="7. Eliminar un archivo", command=self.eliminar_archivo, width=30).pack(pady=2)
        tk.Button(frame_botones, text="8. Consultar información de un archivo", command=self.consultar_info, width=30).pack(pady=2)
        tk.Button(frame_botones, text="0. Salir", command=root.quit, width=30, fg="red").pack(pady=10)

        # Cargar lista al inicio
        self.listar_archivos()

    def pedir_nombre(self, titulo, mensaje):
        return simpledialog.askstring(titulo, mensaje, parent=self.root)

    def crear_directorio(self):
        nombre = self.pedir_nombre("Crear Directorio", "Ingresa el nombre de la nueva carpeta:")
        if not nombre: return
        ruta = obtener_ruta(nombre)
        try:
            os.makedirs(ruta, exist_ok=False)
            messagebox.showinfo("Éxito", f"Carpeta '{nombre}' creada exitosamente.")
            self.listar_archivos()
        except FileExistsError:
            messagebox.showerror("Error", f"La carpeta '{nombre}' ya existe.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear la carpeta: {e}")

    def crear_archivo_texto(self):
        nombre = self.pedir_nombre("Crear Archivo", "Ingresa el nombre del archivo (con extensión .txt):")
        if not nombre: return
        if not nombre.endswith('.txt'):
            nombre += '.txt'
        ruta = obtener_ruta(nombre)
        
        if os.path.exists(ruta):
            messagebox.showerror("Error", f"El archivo '{nombre}' ya existe.")
        else:
            try:
                with open(ruta, 'w') as archivo:
                    pass
                messagebox.showinfo("Éxito", f"Archivo '{nombre}' creado exitosamente.")
                self.listar_archivos()
            except Exception as e:
                messagebox.showerror("Error", f"Error al crear el archivo: {e}")

    def escribir_archivo(self):
        nombre = self.pedir_nombre("Escribir Archivo", "Ingresa el nombre del archivo a modificar:")
        if not nombre: return
        ruta = obtener_ruta(nombre)
        
        if not os.path.exists(ruta):
            messagebox.showerror("Error", f"El archivo '{nombre}' no existe.")
            return
            
        texto = self.pedir_nombre("Escribir Archivo", "Escribe el texto que deseas agregar:")
        if texto is None: return
        
        try:
            with open(ruta, 'a') as archivo:
                archivo.write(texto + "\n")
            messagebox.showinfo("Éxito", "Información agregada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al escribir en el archivo: {e}")

    def leer_archivo(self):
        nombre = self.pedir_nombre("Leer Archivo", "Ingresa el nombre del archivo que deseas leer:")
        if not nombre: return
        ruta = obtener_ruta(nombre)
        
        if not os.path.exists(ruta):
            messagebox.showerror("Error", f"El archivo '{nombre}' no existe.")
            return
            
        try:
            with open(ruta, 'r') as archivo:
                contenido = archivo.read()
                if not contenido:
                    contenido = "(El archivo está vacío)"
                messagebox.showinfo(f"Contenido de {nombre}", contenido)
        except Exception as e:
            messagebox.showerror("Error", f"Error al leer el archivo: {e}")

    def renombrar_archivo(self):
        nombre_actual = self.pedir_nombre("Renombrar", "Ingresa el nombre actual del archivo/carpeta:")
        if not nombre_actual: return
        ruta_actual = obtener_ruta(nombre_actual)
        
        if not os.path.exists(ruta_actual):
            messagebox.showerror("Error", f"El archivo '{nombre_actual}' no existe.")
            return
            
        nuevo_nombre = self.pedir_nombre("Renombrar", "Ingresa el nuevo nombre:")
        if not nuevo_nombre: return
        ruta_nueva = obtener_ruta(nuevo_nombre)
        
        if os.path.exists(ruta_nueva):
            messagebox.showerror("Error", f"Ya existe un archivo con el nombre '{nuevo_nombre}'.")
            return
            
        try:
            os.rename(ruta_actual, ruta_nueva)
            messagebox.showinfo("Éxito", f"Archivo renombrado a '{nuevo_nombre}' exitosamente.")
            self.listar_archivos()
        except Exception as e:
            messagebox.showerror("Error", f"Error al renombrar: {e}")

    def copiar_archivo(self):
        nombre_origen = self.pedir_nombre("Copiar Archivo", "Ingresa el nombre del archivo a copiar:")
        if not nombre_origen: return
        ruta_origen = obtener_ruta(nombre_origen)
        
        if not os.path.exists(ruta_origen):
            messagebox.showerror("Error", f"El archivo '{nombre_origen}' no existe.")
            return
            
        nombre_destino = self.pedir_nombre("Copiar Archivo", "Ingresa el nombre de la copia:")
        if not nombre_destino: return
        ruta_destino = obtener_ruta(nombre_destino)
        
        if os.path.exists(ruta_destino):
            messagebox.showerror("Error", f"Ya existe un archivo con el nombre '{nombre_destino}'.")
            return
            
        try:
            shutil.copy2(ruta_origen, ruta_destino)
            messagebox.showinfo("Éxito", f"Archivo copiado exitosamente como '{nombre_destino}'.")
            self.listar_archivos()
        except Exception as e:
            messagebox.showerror("Error", f"Error al copiar: {e}")

    def eliminar_archivo(self):
        nombre = self.pedir_nombre("Eliminar Archivo", "Ingresa el nombre del archivo/carpeta a eliminar:")
        if not nombre: return
        ruta = obtener_ruta(nombre)
        
        if not os.path.exists(ruta):
            messagebox.showerror("Error", f"El archivo o carpeta '{nombre}' no existe.")
            return
            
        confirmacion = messagebox.askyesno("Confirmar", f"¿Estás seguro que deseas eliminar '{nombre}'?")
        if confirmacion:
            try:
                if os.path.isdir(ruta):
                    os.rmdir(ruta)
                else:
                    os.remove(ruta)
                messagebox.showinfo("Éxito", f"'{nombre}' eliminado exitosamente.")
                self.listar_archivos()
            except OSError:
                messagebox.showerror("Error", "La carpeta no está vacía o no se puede eliminar.")
            except Exception as e:
                messagebox.showerror("Error", f"Error al eliminar: {e}")

    def consultar_info(self):
        nombre = self.pedir_nombre("Información", "Ingresa el nombre del archivo o carpeta:")
        if not nombre: return
        ruta = obtener_ruta(nombre)
        
        if not os.path.exists(ruta):
            messagebox.showerror("Error", f"El archivo o carpeta '{nombre}' no existe.")
            return
            
        try:
            tamaño = os.path.getsize(ruta)
            fecha_mod = os.path.getmtime(ruta)
            fecha_legible = datetime.datetime.fromtimestamp(fecha_mod).strftime('%Y-%m-%d %H:%M:%S')
            
            info = f"Nombre: {nombre}\nTamano: {tamaño} bytes\nUltima modificación: {fecha_legible}"
            messagebox.showinfo("Información del Archivo", info)
        except Exception as e:
            messagebox.showerror("Error", f"Error al consultar información: {e}")

    def listar_archivos(self):
        self.lista_archivos.delete(0, tk.END)
        try:
            elementos = os.listdir(CARPETA_BASE)
            if not elementos:
                self.lista_archivos.insert(tk.END, "La carpeta GESTOR_SO está vacía.")
                return
                
            for item in elementos:
                ruta_item = obtener_ruta(item)
                tipo = "[Carpeta]" if os.path.isdir(ruta_item) else "[Archivo]"
                self.lista_archivos.insert(tk.END, f"{tipo} {item}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al listar el directorio: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestorArchivosApp(root)
    root.mainloop()