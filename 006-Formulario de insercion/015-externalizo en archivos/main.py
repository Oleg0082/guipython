import tkinter as tk
from menu import *

import json
import time

ventana = tk.Tk()
ventana.title("Programa de Jose Vicente")
ventana.geometry("512x512")

from insertar import *

mostrarMenu(ventana)

panel_bienvenida = tk.Frame(ventana)
panel_bienvenida.pack()

titulo = tk.Label(
    panel_bienvenida,
    text="Programa de Jose Vicente"
    )
titulo.pack(padx=50,pady=50)

panelInsertar(ventana)

ventana.mainloop()
