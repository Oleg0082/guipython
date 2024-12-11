import tkinter as tk

def salirPrograma():
    ventana.quit()

def mostrarMenu():
    barra_menu = tk.Menu(ventana)
    menu_archivo = tk.Menu(
        barra_menu,
        tearoff=0
        )
    menu_archivo.add_command(
        label="Salir",
        command=salirPrograma
        )
    barra_menu.add_cascade(
        label="Archivo",
        menu=menu_archivo
        )
    ventana.config(menu=barra_menu)

ventana = tk.Tk()
ventana.title("Programa de Jose Vicente")
ventana.geometry("512x512")



panel_bienvenida = tk.Frame(ventana)
panel_bienvenida.pack()

titulo = tk.Label(
    panel_bienvenida,
    text="Programa de Jose Vicente"
    )
titulo.pack(padx=50,pady=50)

ventana.mainloop()
