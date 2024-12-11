import tkinter as tk
from menu import *
from panelbienvenida import *
import json
import time

def listadoClientes():
    print("Vamos a listar los clientes")

ventana = tk.Tk()
ventana.title("Programa de Jose Vicente")
ventana.geometry("512x512")

from insertar import *

mostrarMenu(ventana)
panelBienvenida(ventana)
panelInsertar(ventana)

marco_listado = tk.Frame(ventana)
marco_listado.pack()

tk.Button(
    marco_listado,
    text="Obtener clientes",
    command = listadoClientes
    ).pack()

ventana_texto = tk.Text(
    marco_listado
)
ventana_texto.pack()

ventana.mainloop()
