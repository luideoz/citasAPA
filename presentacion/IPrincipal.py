from tkinter import *
from tkinter import messagebox
from presentacion import IMenu
from dominio import controlCitas

class IPrincipal:
    
    def __init__(self):
        self.window = Tk()
        self.window.title('APA Creator')
        self.window.geometry('450x450')
        self.window.resizable(height=False,width=False)
        icono = PhotoImage(file='/home/luis/Descargas/libro-abierto.png')
        kitty = PhotoImage(file='/home/luis/Descargas/icons8-hello-kitty-100.png')
        self.window.config(bg='pink')
        self.etiqueta_kitty = Label(self.window, image=kitty).pack(side='right',pady=50)
        self.window.iconphoto(True,icono)
        
        self.title = Label(self.window, text='CITAS APA', bg='white', fg= 'black', font=('Comic Sans',30)).pack()
        
        self.buttom = Button(self.window, text='Empezar', bg='white', fg= 'black', font=('Comic Sans',20),command=self.changeWindow,height=3).pack(pady=25)
        self.reset = Button(self.window, text='Reiniciar datos', font=('Comic Sans',20),bg='white',fg='black',height=3,command=self.deleteAll).pack(pady=75)
        
        self.window.mainloop()
        
    def changeWindow(self):
        self.window.destroy()
        IMenu.IMenu()
    
    def deleteAll(self):
        if messagebox.askyesno(title='Reiniciar',message='¿Seguro que desea reiniciar los datos?'):
            try:
                controlCitas.deleteAll()
                messagebox.showinfo(title='Reiniciar',message='Exito al reiniciar')
            except Exception:
                messagebox.showerror(title='Reiniciar',message='Error al reinciar')