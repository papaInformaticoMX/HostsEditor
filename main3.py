import tkinter as tk
from tkinter import messagebox
import subprocess

# Función para modificar el archivo hosts
def modify_hosts():
    # Obtener el contenido de la caja de texto
    new_content = text_box.get("1.0", tk.END)
    
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

# Crear la ventana
window = tk.Tk()
window.title("Modificar archivo hosts")

# Crear la etiqueta
label = tk.Label(window, text="Edita el contenido del archivo hosts:")
label.pack()

# Crear la caja de texto
text_box = tk.Text(window, height=10, width=50)
text_box.pack(fill=tk.BOTH, expand=True)  # Maximizar la caja de texto

# Cargar el contenido actual del archivo en la caja de texto
with open(r"C:\Windows\System32\drivers\etc\hosts", "r") as f:
    content = f.read()
    text_box.insert(tk.END, content)

# Crear el botón
button = tk.Button(window, text="Guardar cambios", command=modify_hosts)
button.pack()

# Controlador de eventos para maximizar la caja de texto cuando la ventana se maximiza
def on_window_resize(event):
    text_box.pack(fill=tk.BOTH, expand=True)

window.bind("<Configure>", on_window_resize)

# Iniciar la ventana
window.mainloop()
