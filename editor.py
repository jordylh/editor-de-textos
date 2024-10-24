from tkinter import *
from tkinter import filedialog as FileDialog

ruta = "" #Se almacena la ruta del fichero

def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0,"end")
    root.title(ruta+"- Mi editor")

def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta=FileDialog.askopenfilename(initialdir='.',
                                    filetypes=(("Fichero de texto","*.txt"),),
                                    title="Abrir un fichero de texto")
    if ruta!="":
        fichero=open(ruta,'r')
        contenido=fichero.read()
        texto.delete(1.0,"end")
        texto.insert('insert',contenido)
        fichero.close()
        root.title(ruta+"- Mi editor")

def guardar():
    global ruta
    mensaje.set("Guardar fichero") 
    if ruta!="":
        contenido=texto.get(1.0,'end-1c')
        fichero=open(ruta,'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente") 
    else:
        guardar_como()  

def guardar_como():
    global ruta
    mensaje.set("Guardar fichero Como")
    fichero =FileDialog.asksaveasfile(title="Guardar un fichero",mode='w',defaultextension=".txt")
    if fichero is not None:
        ruta=fichero.name
        contenido=texto.get(1.0,'end-1c')
        fichero=open(ruta,'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente") 
    else:
        mensaje.set("Guardado cancelado")
        ruta=""

root=Tk()
root.title("Mi editor")

#Se crea el menu
menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir" , command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir",command=root.quit)
menubar.add_cascade(menu=filemenu,label="Archivo")

#Caga de texto central
texto = Text(root)
texto.pack(fill="both" ,expand=1)
texto.config(bd=0,padx=6, pady=4, font=("Consolas",12))

#Monitor inferior
mensaje=StringVar()
mensaje.set("Bienvenido a tu editor")
monitor=Label(root,textvar=mensaje,justify='left')
monitor.pack(side="left")

#se agrega el menu a la interfaz
root.config(menu=menubar)

#Bucle de la aplicacion
root.mainloop()