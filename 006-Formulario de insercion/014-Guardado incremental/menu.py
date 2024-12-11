import tkinter as tk

def salirPrograma(ventana):
    ventana.quit()

def mostrarMenu(ventana):
    barra_menu = tk.Menu(ventana)
    # Menu archivo
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
    menu_ayuda = tk.Menu(
        barra_menu,
        tearoff=0
        )
    menu_ayuda.add_command(
        label="Acerca de..."
        )
    barra_menu.add_cascade(
        label="Ayuda",
        menu=menu_ayuda
        )
    ventana.config(menu=barra_menu)
