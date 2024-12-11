import tkinter as tk

def salirPrograma(ventana):
    ventana.quit()
def insertarCliente(ventana):
    print("Vamos a insertar un cliente")
def listarClientes(ventana):
    print("Vamos a listar todos los clientes")

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
    # Menu clientes
    menu_clientes = tk.Menu(
        barra_menu,
        tearoff=0
        )
    menu_clientes.add_command(
        label="Insertar un nuevo cliente",
        command=lambda: insertarCliente(ventana)
        )
    menu_clientes.add_command(
        label="Listar clientes",
        command=lambda: listarClientes(ventana)
        )
    barra_menu.add_cascade(
        label="Clientes",
        menu=menu_clientes
        )
    # Menu ayuda
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
