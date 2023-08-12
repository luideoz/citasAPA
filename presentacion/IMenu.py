from tkinter import *
from tkinter import ttk
from dominio import Autores
from dominio import controlCitas,Editoriales,Articulos
from tkinter import messagebox
import pyperclip

class IMenu:
    def __init__(self):
        
        self.window = Tk()
        self.window.title('APA Creator')
        self.window.geometry('720x720')
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
        
        #frame autores
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
        
        #editorial frame
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
        
        #articulos frame
        self.list_articulos = Listbox(self.articulos_frame, fg='black',bg='white',font=('Comic Sans',20),height=50,width=20)
        self.list_articulos.pack(side='left',anchor='nw',padx=0,pady=0)
        
        self.list_articulos.bind("<<ListboxSelect>>",self.rellenarArticulos)
        
        articulos = controlCitas.selectArticulos()
        for index in range(len(articulos)):
            self.list_articulos.insert(self.list_articulos.size(),articulos[index])
        
        self.nameArticulo_label = Label(self.articulos_frame, text='Nombre',fg='black',bg='pink',font=('Comic Sans',20))
        self.nameArticulo_label.pack()
        self.nameArticulo_text = Entry(self.articulos_frame, font=('Comic Sans',20),bg='white',fg='black')
        self.nameArticulo_text.pack()
        
        self.año_label = Label(self.articulos_frame, text='Año', bg='pink', fg='black', font=('Comic Sans',20))
        self.año_label.pack()
        
        self.año_text = Entry(self.articulos_frame, font=('Comic Sans',20),bg='white',fg='black')
        self.año_text.pack()
        
        self.edicion_label = Label(self.articulos_frame, font=('Comic Sans',20),text='Edicion',bg='pink',fg='black')
        self.edicion_label.pack()
        
        self.edicion_text = Entry(self.articulos_frame, font=('Comic Sans',20),bg='white',fg='black')
        self.edicion_text.pack()
        
        self.autor_label = Label(self.articulos_frame, text='Autor', font=('Comic Sans',20),bg='pink',fg='black')
        self.autor_label.pack()
        
        self.autor_text = ttk.Combobox(self.articulos_frame, font=('Comic Sans',20),foreground='black',background='white',values=autores,state='readonly')
        self.autor_text.pack()
        
        self.editorial_label = Label(self.articulos_frame, text='Editorial', font=('Comic Sans',20), fg='black', bg='pink')
        self.editorial_label.pack()
        
        self.editorial_text = ttk.Combobox(self.articulos_frame, font=('Comic Sans',20), background='white',foreground='black',values=editoriales, state='readonly')
        self.editorial_text.pack()
        
        self.insertArticulo_button = Button(self.articulos_frame, text='Insertar', bg='white', fg='black', font=('Comic Sans',20), width=20,height=2,command=self.insertArticulo)
        self.insertArticulo_button.pack(pady=20)
        
        self.deleteArticulo_button = Button(self.articulos_frame, text='Eliminar', fg='black', bg='white',font=('Comic Sans',20), width=20, height=2,command=self.deleteArticulo)
        self.deleteArticulo_button.pack(pady=20)
        
        #citas frame
        self.information_label = Label(self.citas_frame, text='Introduzca el rango de paginas si es necesario y seleccione el articulo',font=('Comic Sans',15),bg='pink',fg='black')
        self.information_label.pack(side='top')
        
        self.rango_label = Label(self.citas_frame, text='Rango de paginas',font=('Comic Sans',20),bg='pink',fg='black')
        self.rango_label.pack(pady=20)
        
        self.rango_text = Entry(self.citas_frame, bg='white', fg='black', font=('Comic Sans',20))
        self.rango_text.pack(pady=10)
        
        self.articulos_label = Label(self.citas_frame, text='Articulos',font=('Comic Sans',20),bg='pink',fg='black')
        self.articulos_label.pack(pady=10)
        
        articulos = controlCitas.selectArticulos()
        self.combo_articulos = ttk.Combobox(self.citas_frame, font=('Comic Sans',20),foreground='black',background='white',values=articulos,state='readonly')
        self.combo_articulos.pack(pady=15)   
        
        self.cita = StringVar()
        
        self.cita_label = Label(self.citas_frame, font=('Comic Sans',15),bg='white',fg='black',textvariable=self.cita,width=40)
        self.cita_label.pack(pady=15)
        
        self.generate_button = Button(self.citas_frame, text='Generar cita',font=('Comic Sans',20),bg='white',fg='black',width=25,height=3,command=self.crearCita)
        self.generate_button.pack(pady=20)
        
        self.copy_button = Button(self.citas_frame, text='Copiar cita', font=('Comic Sans',20), fg='black',bg='white',width=25,height=3,command=self.copyCita)
        self.copy_button.pack(pady=20)
        self.window.mainloop()
        
    def introducirAutor(self):
        if self.name_text.get() != '' and self.subname_text.get() != '':
            name = self.name_text.get()
            subname = self.subname_text.get()
            autor = Autores.Autores(name,subname)
            try:
                autor.insert()
                self.list_autores.delete(0,END)
                self.autor_text['values'] = []
                autores = controlCitas.selectAutores()
                for index in range(len(autores)):
                    self.list_autores.insert(self.list_autores.size(),autores[index])
                self.autor_text.config(values=autores)
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
    
    def rellenarEditorial(self,event):
        try:
            if self.list_editorial.curselection() != '':
                self.nombreEditorial_text.delete(0,END)
                editorial = self.list_editorial.get(self.list_editorial.curselection())
                self.nombreEditorial_text.insert(0,editorial)
        except TclError:
            pass
    
    def rellenarArticulos(self,event):
        try:
            if self.list_articulos.curselection() != '':
                self.nameArticulo_text.delete(0,END)
                self.año_text.delete(0,END)
                self.edicion_text.delete(0,END)
                self.autor_text.delete(0,END)
                self.editorial_text.delete(0,END)
                nombre = self.list_articulos.get(self.list_articulos.curselection())
                año,edicion,nombreA,apellidoA,editorial = controlCitas.selectArticulos_Completos(nombre=nombre)
                nombre_completo = apellidoA + ' ' + nombreA
                self.nameArticulo_text.insert(0,nombre)
                self.año_text.insert(0,str(año))
                self.edicion_text.insert(0,str(edicion))
                self.autor_text.set(nombre_completo)
                self.editorial_text.set(editorial)
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
                    self.autor_text['values'] = []
                    autores = controlCitas.selectAutores()
                    for index in range(len(autores)):
                        self.list_autores.insert(self.list_autores.size(),autores[index])
                    self.autor_text.config(values=autores)
                    self.name_text.delete(0,END)
                    self.subname_text.delete(0,END)
                    autor.deleteArticulo()
                    self.list_articulos.delete(0,END)
                    articulos = controlCitas.selectArticulos()
                    for index in range(len(articulos)):
                        self.list_articulos.insert(self.list_articulos.size(),articulos[index])
                    self.combo_articulos['values'] = []
                    self.combo_articulos.config(values=articulos)
                except Exception:
                    messagebox.showerror(title='Eliminar',message='Se ha producido un error')
        else:
            messagebox.showerror(title='Eliminar',message='Faltan campos')
    
    def insertEditorial(self):
        if self.nombreEditorial_text.get() != '':
            editorial = Editoriales.Editoriales(self.nombreEditorial_text.get())
            try:
                editorial.insert()
                messagebox.showinfo(title='Insertar',message='Exito al insertar')
                self.nombreEditorial_text.delete(0,END)
                self.list_editorial.delete(0,END)
                self.editorial_text['values'] = []
                editoriales = controlCitas.selectEditoriales()
                for index in range(len(editoriales)):
                    self.list_editorial.insert(self.list_editorial.size(),editoriales[index])
                self.editorial_text.config(values=editoriales)
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
                    self.editorial_text['values'] = []
                    editoriales = controlCitas.selectEditoriales()
                    for index in range(len(editoriales)):
                        self.list_editorial.insert(self.list_editorial.size(),editoriales[index])
                    self.editorial_text.config(values=editoriales)
                    editorial.deleteArticulo()
                    self.list_articulos.delete(0,END)
                    articulos = controlCitas.selectArticulos()
                    for index in range(len(articulos)):
                        self.list_articulos.insert(self.list_articulos.size(),articulos[index])
                    self.combo_articulos['values'] = []
                    self.combo_articulos.config(values=articulos)
                except Exception:
                    messagebox.showerror(title='Eliminar',message='Error al eliminar')
        else:
            messagebox.showerror(title='Eliminar',message='Error, nombre vacio')
    
    def insertArticulo(self):
        if self.nameArticulo_text.get() != '' and self.año_text.get() != '' and self.edicion_text.get() != '' and self.autor_text.get() != '' and self.editorial_text.get() != '':
            partes = self.autor_text.get().split()
            aurticulo = Articulos.Articulos(self.nameArticulo_text.get(),self.año_text.get(),self.edicion_text.get(),partes[1],partes[0],self.editorial_text.get())
            try:
                aurticulo.insert()
                messagebox.showinfo(title='Insercion',message='Insertado con exito')
                self.nameArticulo_text.delete(0,END)
                self.año_text.delete(0,END)
                self.edicion_text.delete(0,END)
                self.autor_text.set('')
                self.editorial_text.set('')
                self.list_articulos.delete(0,END)
                self.combo_articulos['values'] = []
                articulos = controlCitas.selectArticulos()
                for index in range(len(articulos)):
                    self.list_articulos.insert(self.list_articulos.size(),articulos[index])
                self.combo_articulos.config(values=articulos)
            except Exception:
                messagebox.showerror(title='Insertar',message='Error al insertar')
        else:
            messagebox.showerror(title='Insercion',message='Error. Faltan campos')
    
    def deleteArticulo(self):
        if self.nameArticulo_text.get() != '' and self.año_text.get() != '' and self.edicion_text.get() != '' and self.autor_text.get() != '' and self.editorial_text.get() != '':
            if messagebox.askyesno(title='Eliminar',message='¿Seguro que desea eliminar?'):
                partes = self.autor_text.get().split()
                articulo = Articulos.Articulos(self.nameArticulo_text.get(),self.año_text.get(),self.edicion_text.get(),partes[1],partes[0],self.editorial_text.get())
                try:
                    articulo.Delete()
                    messagebox.showinfo(title='Eliminar',message='Eliminado con exito')
                    self.nameArticulo_text.delete(0,END)
                    self.año_text.delete(0,END)
                    self.edicion_text.delete(0,END)
                    self.autor_text.set('')
                    self.editorial_text.set('')
                    self.list_articulos.delete(0,END)
                    self.combo_articulos['values'] = []
                    articulos = controlCitas.selectArticulos()
                    for index in range(len(articulos)):
                        self.list_articulos.insert(self.list_articulos.size(),articulos[index])
                    self.combo_articulos.config(values=articulos)
                except Exception:
                    messagebox.showerror(title='Eliminar',message='Error al eliminar')
        else:
            messagebox.showerror(title='Eliminar',message='Error, faltan campos')
    
    def crearCita(self):
        nombreArticulo = self.combo_articulos.get()
        try:
            cita = controlCitas.crearCita(nombre=nombreArticulo,rango=self.rango_text.get())
            self.cita.set(cita)
        except IndexError:
            messagebox.showerror(title='Generar cita', message='No hay articulo seleccionado')
    
    def copyCita(self):
        texto = self.cita.get()
        pyperclip.copy(texto)
        messagebox.showinfo(title='Copiar',message='Copiado')
        
            
    
            