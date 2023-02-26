import tkinter as tk
from tkinter import messagebox
import subprocess
import re

# Función para modificar el archivo hosts
def modify_hosts():
    # Obtener el contenido de la caja de texto
    new_content = text_box.get("1.0", tk.END)

    # Validar la sintaxis del contenido
    if not is_valid_hosts_content(new_content):
        # Mostrar mensaje de error si el contenido no es válido
        messagebox.showerror("Error", "El contenido del archivo hosts no es válido.")
        return

    # Obtener la ruta del archivo hosts
    hosts_file = r"C:\Windows\System32\drivers\etc\hosts"

    # Abrir el archivo en modo de escritura
    with open(hosts_file, "w") as f:
        # Escribir el nuevo contenido en el archivo
        f.write(new_content)

    # Reiniciar el servicio DNS
    subprocess.call(["ipconfig", "/flushdns"])

    # Mostrar mensaje de éxito
    messagebox.showinfo("Éxito", "El archivo hosts ha sido modificado correctamente.")

# Función para validar la sintaxis del contenido del archivo hosts
def is_valid_hosts_content(content):
    # Expresión regular para validar el contenido
    regex = r"(?P<ip_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<host_name>\S+)"
    return all(re.match(regex, line) for line in content.splitlines() if line.strip() and not line.startswith("#"))

# Función para agregar la línea de Netflix
def add_netflix_line():
    text_box.insert(tk.END, "127.0.0.1   netflix.com\n")
    text_box.insert(tk.END, "127.0.0.1   youtube.com\n")
    text_box.insert(tk.END, "127.0.0.1   disneyplus.com\n")

# Crear la ventana
window = tk.Tk()
window.title("Modificar archivo hosts")

# Crear la etiqueta
label = tk.Label(window, text="Edita el contenido del archivo hosts:")
label.pack()

# Crear la caja de texto
text_box = tk.Text(window, height=10, width=50)
text_box.pack(fill=tk.BOTH, expand=True)

# Cargar el contenido actual del archivo en la caja de texto
with open(r"C:\Windows\System32\drivers\etc\hosts", "r") as f:
    content = f.read()
    text_box.insert(tk.END, content)

# Crear el botón para guardar cambios
button = tk.Button(window, text="Guardar cambios", command=modify_hosts)
button.pack()

# Crear el botón para agregar la línea de Netflix
netflix_button = tk.Button(window, text="Bloquear Netflix, disney y youtube", command=add_netflix_line)
netflix_button.pack()

# Controlador de eventos para maximizar la caja de texto cuando la ventana se maximiza
def on_window_resize(event):
    text_box.pack(fill=tk.BOTH, expand=True)

window.bind("<Configure>", on_window_resize)

# Iniciar la ventana
window.mainloop()
