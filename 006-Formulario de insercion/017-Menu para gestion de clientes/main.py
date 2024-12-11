import tkinter as tk
from menu import *
from panelbienvenida import *
import json
import time

ventana = tk.Tk()
ventana.title("Programa de Jose Vicente")
ventana.geometry("512x512")

from insertar import *

mostrarMenu(ventana)
panelBienvenida(ventana)
panelInsertar(ventana)

ventana.mainloop()
