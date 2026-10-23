import tkinter as tk
from tkinter import messagebox
from Scirpt_BidRequest1_1 import keywords_def

# Crear ventana principal
ventana = tk.Tk()
ventana.title("OptiFiltro")
ventana.geometry("400x300")
ventana.resizable(False, False)
imagen = tk.PhotoImage(file = "OPTIMEN.png")
imagen = imagen.subsample(3,3)
#Entrada de texto

# Título

titulo_logo = tk.Label(
    ventana,
    # Mostrar imagen
    image = imagen
)

titulo_logo.place(x=0, y=0, relwidth=1, relheight=1)
text_inicio = tk.Label(ventana,text = "Introduce la palabra a filtrar")
text_inicio.pack(pady = 10)

# Funciones de los botones
def mostrar():
    texto = keywords_def(entrada.get()) # lee lo que escribió el usuario
    resultado.config(text=texto)    
        
def salir():
    ventana.destroy()

entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

resultado = tk.Label(ventana, text="")
resultado.pack(pady=5)

# Botones}
boton = tk.Button(
    ventana, 
    text="Guardar", 
    command=mostrar
)
boton.pack(pady=5)

boton2 = tk.Button(
    ventana,
    text="Salir",
    command=salir,
    width=20,
    bg="#B8251B",
    fg="white"
)
boton2.pack(pady=5)

# Iniciar aplicación
ventana.mainloop()