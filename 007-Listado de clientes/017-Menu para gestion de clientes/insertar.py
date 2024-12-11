import tkinter as tk
import time
import json

nombre_del_cliente = tk.StringVar()
apellidos_del_cliente = tk.StringVar()
email_del_cliente = tk.StringVar()

def guardaDatos():
    print("Vamos a guardar los datos")
    # Primero recojo el contenido de los campos
    nombre = nombre_del_cliente.get()
    apellidos = apellidos_del_cliente.get()
    email = email_del_cliente.get()
    # Creo un diccionario con el contenido de los campos
    diccionario = {
        "nombre":nombre,
        "apellidos":apellidos,
        "email":email
    }
    # Guardo ese diccionario en un archivo json en el disco duro
    archivo = open("db/"+str(time.time())+".json",'w')
    json.dump(diccionario,archivo, indent=4)
    archivo.close()
def panelInsertar(ventana):
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
    # Boton de envío
    tk.Button(
        panel_insertar,
        text="Enviar",
        command=guardaDatos
    ).pack()