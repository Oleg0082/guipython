import tkinter as tk
from menu import *
from panelbienvenida import *
import json
import time
import os

def listadoClientes(ventana_texto):
    print("Vamos a listar los clientes")
    carpeta = "db"
    archivos = files = os.listdir(carpeta)
    for archivo in archivos:
        ventana_texto.insert(tk.END, archivo+"\n")


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
    command = lambda:listadoClientes(ventana_texto)
    ).pack()

ventana_texto = tk.Text(
    marco_listado
)
ventana_texto.pack()

ventana.mainloop()
