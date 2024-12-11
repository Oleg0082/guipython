import tkinter as tk
from menu import *

ventana = tk.Tk()
ventana.title("Programa de Jose Vicente")
ventana.geometry("512x512")

nombre_del_cliente = tk.StringVar()
apellidos_del_cliente = tk.StringVar()
email_del_cliente = tk.StringVar()

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

# Nombre del cliente
tk.Label(
    panel_insertar,
    text="Introduce el nombre del cliente"
    ).pack()
tk.Entry(
    panel_insertar,
    textvariable = nombre_del_cliente
).pack()
# Apellidos del cliente
tk.Label(
    panel_insertar,
    text="Introduce los apellidos del cliente"
    ).pack()
tk.Entry(
    panel_insertar,
    textvariable = apellidos_del_cliente
).pack()
# Email del cliente
tk.Label(
    panel_insertar,
    text="Introduce el email del cliente"
    ).pack()
tk.Entry(
    panel_insertar,
    textvariable = email_del_cliente
).pack()

ventana.mainloop()
