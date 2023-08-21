from tkinter import *
from tkinter import messagebox
from presentacion import IMain
from dominio import controlCitas

class IPrincipal:
    
    def __init__(self):
        self.window = Tk()
        self.window.title('APA Creator')
        self.window.geometry('450x450')
        self.window.resizable(height=False,width=False)
        icono = PhotoImage(file='/home/luis/Descargas/libro-abierto.png')
        kitty = PhotoImage(file='/home/luis/Descargas/icons8-hello-kitty-doodle/icons8-hello-kitty-48.png')
        kitty2 = PhotoImage(file='/home/luis/Descargas/icons8-hello-kitty-bubbles/icons8-hello-kitty-50.png')
        self.window.config(bg='pink')
        self.window.iconphoto(True,icono)
        
        self.title = Label(self.window, text='CITAS APA', bg='white', fg= 'black', font=('Garamond',30,'bold')).pack()
        
        self.buttom = Button(self.window, text='Empezar', bg='white', fg= 'black', font=('Garamond',20),command=self.changeWindow,height=90,image=kitty2,compound='left').pack(pady=25)
        self.reset = Button(self.window, text='Reiniciar datos', font=('Garamond',20),bg='white',fg='black',height=80,command=self.deleteAll,image=kitty,compound='left').pack(pady=75)
        
        self.window.mainloop()
        
    def changeWindow(self):
        self.window.destroy()
        IMain.IMain()
    
    def deleteAll(self):
        if messagebox.askyesno(title='Reiniciar',message='¿Seguro que desea reiniciar los datos?'):
            try:
                controlCitas.deleteAll()
                messagebox.showinfo(title='Reiniciar',message='Exito al reiniciar')
            except Exception:
                messagebox.showerror(title='Reiniciar',message='Error al reinciar')