import tkinter as tk

def salirPrograma(ventana):
    ventana.quit()

def mostrarMenu(ventana):
    barra_menu = tk.Menu(ventana)
    menu_archivo = tk.Menu(
        barra_menu,
        tearoff=0
        )
    menu_archivo.add_command(
        label="Salir",
        command=lambda: salirPrograma(ventana)
        )
    barra_menu.add_cascade(
        label="Archivo",
        menu=menu_archivo
        )
    ventana.config(menu=barra_menu)
