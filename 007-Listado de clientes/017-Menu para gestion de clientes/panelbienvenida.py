import tkinter as tk

def panelBienvenida(ventana):
    panel_bienvenida = tk.Frame(ventana)
    panel_bienvenida.pack()

    titulo = tk.Label(
        panel_bienvenida,
        text="Programa de Jose Vicente"
        )
    titulo.pack(padx=50,pady=50)