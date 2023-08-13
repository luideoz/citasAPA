from tkinter import *
from tkinter import ttk
from dominio import Autores
from dominio import controlCitas,Editoriales,Articulos
from tkinter import messagebox
import pyperclip

class IMain:
    def __init__(self):
        
        self.window = Tk()
        self.window.title('APA Creator')
        self.window.geometry('900x900')
        self.window.config(bg = 'pink')
        
        self.tabs = ttk.Notebook(self.window)
        
        self.autores_frame = Frame(self.tabs)
        self.autores_frame.config(bg='pink')
        self.tabs.add(self.autores_frame,text='Autores')
        
        self.editoriales_frame = Frame(self.tabs)
        self.editoriales_frame.config(bg='pink')
        self.tabs.add(self.editoriales_frame,text='Editoriales')
        
        self.articulos_frame = Frame(self.tabs)
        self.articulos_frame.config(bg='pink')
        self.tabs.add(self.articulos_frame,text='Articulos')
        
        self.citas_frame = Frame(self.tabs)
        self.citas_frame.config(bg='pink')
        self.tabs.add(self.citas_frame,text='Citas')
        self.tabs.pack(fill='both', expand=True)
        
        #**FRAME AUTORES**
        self.list_autores = Listbox(self.autores_frame, bg='white', fg='black', font=('Comic Sans',15),height=50,width=25)
        self.list_autores.pack(side='left',anchor='nw',padx=0,pady=0)
        autores = controlCitas.selectAutores()
        
        #para rellenar la listbox
        for index in range(len(autores)):
            self.list_autores.insert(self.list_autores.size(),autores[index])
            
        self.list_autores.bind("<<ListboxSelect>>",self.rellenarAutores)
        
        
        self.name_label = Label(self.autores_frame, text='Nombre', font=('Comic Sans',20), fg='black',bg='pink')
        self.name_label.pack(padx=10,pady=10)
        self.name_text = Entry(self.autores_frame, font= ('Comic Sans',20),width=20,bg='white',fg='black')
        self.name_text.pack(pady=12,padx=10)
        self.subname_label = Label(self.autores_frame,text='Apellidos',bg='pink',fg='black',font=('Comic Sans',20))
        self.subname_label.pack(padx=10,pady=20)
        self.subname_text = Entry(self.autores_frame,font=('Comic Sans',20),bg='white',fg='black',width=20)
        self.subname_text.pack()
        
        self.insert_buttom = Button(self.autores_frame,text='Introducir',font=('Comic Sans',20),bg='white',fg='black',width=20,height=3,command=self.introducirAutor)
        self.insert_buttom.pack(pady=50)
        self.delete_buttom = Button(self.autores_frame,text='Eliminar',font=('Comic Sans',20),bg='white',fg='black',height=3,width=20,command=self.eliminarAutor)
        self.delete_buttom.pack()
        
        #***EDITORIALES FRAME***
        self.list_editorial = Listbox(self.editoriales_frame, fg='black',bg='white',font=('Comic Sans',15),height=50,width=25)
        self.list_editorial.pack(side='left',anchor='nw',padx=0,pady=0)
        
        self.list_editorial.bind("<<ListboxSelect>>",self.rellenarEditorial)
        
        editoriales = controlCitas.selectEditoriales()
        for index in range(len(editoriales)):
            self.list_editorial.insert(self.list_editorial.size(),editoriales[index])
        
        self.nombreEditorial_label = Label(self.editoriales_frame, bg='pink',fg='black',font=('Comic Sans',20),text='Nombre')
        self.nombreEditorial_label.pack(padx=10,pady=10)
        self.nombreEditorial_text = Entry(self.editoriales_frame, fg='black',bg='white',font=('Comic Sans',20))
        self.nombreEditorial_text.pack(padx=10,pady=12)
        self.insertEditorial_button = Button(self.editoriales_frame,text='Insertar',font=('Comic Sans',20),bg='white',fg='black',width=20,height=3,command=self.insertEditorial)
        self.insertEditorial_button.pack(pady=50)
        self.deleteEditorial_button = Button(self.editoriales_frame, text='Eliminar',font=('Comic Sans',20),bg='white',fg='black',width=20,height=3,command=self.deleteEditorial)
        self.deleteEditorial_button.pack()
        
        #***ARTICULOS FRAME***
        self.title_label = Label(self.articulos_frame, text='Articulos', fg='black', bg='pink', font=('Comic Sans',20))
        self.title_label.pack(padx=40,pady=0,anchor='w')
        self.list_articulos = Listbox(self.articulos_frame, fg='black',bg='white',font=('Comic Sans',20),height=50,width=20)
        self.list_articulos.pack(side='left',anchor='nw',padx=0,pady=0)
        
        
        articulos = controlCitas.selectArticulos()
        for index in range(len(articulos)):
            self.list_articulos.insert(self.list_articulos.size(),articulos[index])
        
        self.autores_label = Label(self.articulos_frame, text='Autores', fg='black', bg='pink', font=('Comic Sans',20))
        self.autores_label.pack(anchor='w',pady=0,padx=80,side='top')
        self.listArticulos_autores = Listbox(self.articulos_frame, font=('Comic Sans',20),bg='white',fg='black',width=20,height=50)
        self.listArticulos_autores.pack(side='top',anchor='nw',padx=5, pady=0)
        
        self.articuloName_label = Label(self.articulos_frame, text='Nombre',font=('Comic Sans',20),fg='black',bg='pink')
        self.articuloName_label.pack(side='right')
        
        #self.articuloName_text = Entry(self.articulos_frame, fg='black',bg='white',font=('Comic Sans',20))
        #self.articuloName_text.pack()
        
        
        
        
        
        self.window.mainloop()
    
    def introducirAutor(self):
        if self.name_text.get() != '' and self.subname_text.get() != '':
            name = self.name_text.get()
            subname = self.subname_text.get()
            autor = Autores.Autores(name,subname)
            try:
                autor.insert()
                self.list_autores.delete(0,END)
                autores = controlCitas.selectAutores()
                for index in range(len(autores)):
                    self.list_autores.insert(self.list_autores.size(),autores[index])
                messagebox.showinfo(title='Insercion',message='Exito al insertar')
                self.name_text.delete(0,END)
                self.subname_text.delete(0,END)
            except Exception:
                messagebox.showerror(title='Insercion',message='Fallo al insertar autor')
        else:
            messagebox.showerror(title='Insercion',message='Error,faltan campo(s)')
            
    def rellenarAutores(self,event):
        try:
            if self.list_autores.curselection() != '':
                self.name_text.delete(0,END)
                self.subname_text.delete(0,END)
                subname_name= self.list_autores.get(self.list_autores.curselection())
                partes = subname_name.split()
                self.name_text.insert(0,partes[1])
                self.subname_text.insert(0,partes[0])
        except TclError:
            pass
    
    def eliminarAutor(self):
        if self.name_text.get() != '' and self.subname_text.get() != '':
            autor = Autores.Autores(self.name_text.get(),self.subname_text.get())
            if messagebox.askyesno(title='Eliminar',message='¿Desea continuar?'):
                try:
                    autor.delete()
                    messagebox.showinfo(title='Eliminar',message='Eliminado correctamente')
                    self.list_autores.delete(0,END)
                    autores = controlCitas.selectAutores()
                    for index in range(len(autores)):
                        self.list_autores.insert(self.list_autores.size(),autores[index])
                    self.name_text.delete(0,END)
                    self.subname_text.delete(0,END)
                except Exception:
                    messagebox.showerror(title='Eliminar',message='Se ha producido un error')
        else:
            messagebox.showerror(title='Eliminar',message='Faltan campos')
    
    def rellenarEditorial(self,event):
        try:
            if self.list_editorial.curselection() != '':
                self.nombreEditorial_text.delete(0,END)
                editorial = self.list_editorial.get(self.list_editorial.curselection())
                self.nombreEditorial_text.insert(0,editorial)
        except TclError:
            pass
    
    def insertEditorial(self):
        if self.nombreEditorial_text.get() != '':
            editorial = Editoriales.Editoriales(self.nombreEditorial_text.get())
            try:
                editorial.insert()
                messagebox.showinfo(title='Insertar',message='Exito al insertar')
                self.nombreEditorial_text.delete(0,END)
                self.list_editorial.delete(0,END)
                editoriales = controlCitas.selectEditoriales()
                for index in range(len(editoriales)):
                    self.list_editorial.insert(self.list_editorial.size(),editoriales[index])
            except Exception:
                messagebox.showerror(title='Insertar',message='Error al insertar')
        else:
            messagebox.showerror(title='Insertar',message='Error, falta el nombre')
    
    def deleteEditorial(self):
        if self.nombreEditorial_text.get() != '':
            editorial = Editoriales.Editoriales(self.nombreEditorial_text.get())
            if messagebox.askyesno(title='Eliminar',message='¿Seguro que desea eliminar?'):
                try:
                    editorial.Delete()
                    messagebox.showinfo(title='Eliminar',message='Eliminado con exito')
                    self.nombreEditorial_text.delete(0,END)
                    self.list_editorial.delete(0,END)
                    editoriales = controlCitas.selectEditoriales()
                    for index in range(len(editoriales)):
                        self.list_editorial.insert(self.list_editorial.size(),editoriales[index])
                except Exception:
                    messagebox.showerror(title='Eliminar',message='Error al eliminar')
        else:
            messagebox.showerror(title='Eliminar',message='Error, nombre vacio')