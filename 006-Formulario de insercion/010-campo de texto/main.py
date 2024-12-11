import tkinter as tk
from menu import *

ventana = tk.Tk()
ventana.title("Programa de Jose Vicente")
ventana.geometry("512x512")

nombre_del_cliente = tk.StringVar()

mostrarMenu(ventana)

panel_bienvenida = tk.Frame(ventana)
panel_bienvenida.pack()

titulo = tk.Label(
    panel_bienvenida,
    text="Programa de Jose Vicente"
    )
titulo.pack(padx=50,pady=50)

panel_insertar = tk.Frame(ventana)
panel_insertar.pack()

tk.Label(
    panel_insertar,
    text="Introduce el nombre del cliente"
    ).pack()
tk.Entry(
    panel_insertar,
    textvariable = nombre_del_cliente
).pack()

ventana.mainloop()
