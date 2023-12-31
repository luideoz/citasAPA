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
        self.window.geometry('720x720')
        self.window.config(bg = 'pink')
        self.window.resizable(height=False,width=False)
        kitty = PhotoImage(file='/home/luis/Descargas/icons8-hello-kitty-doodle/icons8-hello-kitty-48.png')
        kitty2 = PhotoImage(file='/home/luis/Descargas/icons8-hello-kitty-bubbles/icons8-hello-kitty-50.png')
        
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
        self.list_autores = Listbox(self.autores_frame, bg='white', fg='black', font=('Garamond',15),height=50,width=25)
        self.list_autores.pack(side='left',anchor='nw',padx=0,pady=0)
        autores = controlCitas.selectAutores()
        
        #para rellenar la listbox
        for index in range(len(autores)):
            self.list_autores.insert(self.list_autores.size(),autores[index])
            
        self.list_autores.bind("<<ListboxSelect>>",self.rellenarAutores)
        
        
        self.name_label = Label(self.autores_frame, text='Nombre', font=('Garamond',20), fg='black',bg='pink')
        self.name_label.pack(padx=10,pady=10)
        self.name_text = Entry(self.autores_frame, font= ('Garamond',20),width=20,bg='white',fg='black')
        self.name_text.pack(pady=12,padx=10)
        self.subname_label = Label(self.autores_frame,text='Apellidos',bg='pink',fg='black',font=('Garamond',20))
        self.subname_label.pack(padx=10,pady=20)
        self.subname_text = Entry(self.autores_frame,font=('Garamond',20),bg='white',fg='black',width=20)
        self.subname_text.pack()
        
        self.insert_buttom = Button(self.autores_frame,text='Introducir',font=('Garamond',20),bg='white',fg='black',height=80,command=self.introducirAutor,image=kitty,compound='left')
        self.insert_buttom.pack(pady=50)
        self.delete_buttom = Button(self.autores_frame,text='Eliminar',font=('Garamond',20),bg='white',fg='black',height=85,command=self.eliminarAutor,image=kitty2,compound='left')
        self.delete_buttom.pack()
        
        #***EDITORIALES FRAME***
        self.list_editorial = Listbox(self.editoriales_frame, fg='black',bg='white',font=('Garamond',15),height=50,width=25)
        self.list_editorial.pack(side='left',anchor='nw',padx=0,pady=0)
        
        self.list_editorial.bind("<<ListboxSelect>>",self.rellenarEditorial)
        
        editoriales = controlCitas.selectEditoriales()
        for index in range(len(editoriales)):
            self.list_editorial.insert(self.list_editorial.size(),editoriales[index])
        
        self.nombreEditorial_label = Label(self.editoriales_frame, bg='pink',fg='black',font=('Garamond',20),text='Nombre')
        self.nombreEditorial_label.pack(padx=10,pady=10)
        self.nombreEditorial_text = Entry(self.editoriales_frame, fg='black',bg='white',font=('Garamond',20))
        self.nombreEditorial_text.pack(padx=10,pady=12)
        self.insertEditorial_button = Button(self.editoriales_frame,text='Insertar',font=('Garamond',20),bg='white',fg='black',height=85,command=self.insertEditorial,image=kitty,compound='left')
        self.insertEditorial_button.pack(pady=50)
        self.deleteEditorial_button = Button(self.editoriales_frame, text='Eliminar',font=('Garamond',20),bg='white',fg='black',height=80,command=self.deleteEditorial,image=kitty2,compound='left')
        self.deleteEditorial_button.pack()
        
        #***ARTICULOS FRAME***
        self.list_articulos = Listbox(self.articulos_frame, fg='black',bg='white',font=('Garamond',20),height=50,width=20)
        self.list_articulos.pack(side='left',anchor='w',padx=0,pady=0)
        
        self.list_articulos.bind("<<ListboxSelect>>",self.rellenarCampos_Articulo)
        self.articuloName_label = Label(self.articulos_frame, text='Nombre',font=('Garamond',20),bg='pink',fg='black')
        self.articuloName_label.pack()
        self.articuloName_text = Entry(self.articulos_frame, bg='white',fg='black',font=('Garamond',20))
        self.articuloName_text.pack()
        self.edicion_label = Label(self.articulos_frame, text='Edicion',font=('Garamond',20),bg='pink',fg='black')
        self.edicion_label.pack()
        self.edicion_text = Entry(self.articulos_frame, bg='white', fg='black', font=('Garamond',20))
        self.edicion_text.pack()
        self.año_label = Label(self.articulos_frame, text='Año',font=('Garamond',20),bg='pink',fg='black')
        self.año_label.pack()
        self.año_text = Entry(self.articulos_frame, bg='white',fg='black',font=('Garamond',20))
        self.año_text.pack()
        self.lugar_label = Label(self.articulos_frame, text='Lugar de edicion', font=('Garamond',20),bg='pink',fg='black')
        self.lugar_label.pack()
        self.lugar_text = Entry(self.articulos_frame, bg='white',fg='black',font=('Garamond',20))
        self.lugar_text.pack()
        self.editorial_label = Label(self.articulos_frame,text='Editorial',bg='pink',fg='black',font=('Garamond',20))
        self.editorial_label.pack()
        editoriales = controlCitas.selectEditoriales()
        self.editorial_text = ttk.Combobox(self.articulos_frame, foreground='black',background='white',font=('Garamond',20),values=editoriales,state='readonly')
        self.editorial_text.pack()
        self.autores_label = Label(self.articulos_frame, font=('Garamond',20),bg='pink',fg='black',text='Autor')
        self.autores_label.pack()
        autores = controlCitas.selectAutores()
        self.autores_text = ttk.Combobox(self.articulos_frame, font=('Garamond',20),background='white',foreground='black',values=autores, state='readonly')
        self.autores_text.pack()
        self.autores_text.bind("<<ComboboxSelected>>",self.rellenarArticulo)
        
        self.insertArticulo_button = Button(self.articulos_frame, text='Insertar',font=('Garamond',20),bg='white',fg='black',height=85,command=self.insertarArticulo,image=kitty,compound='left')
        self.insertArticulo_button.pack(pady=10)
        self.deleteArticulo_button = Button(self.articulos_frame, text='Eliminar',font=('Garamond',20),bg='white',fg='black',height=80,command=self.deleteArticulo,image=kitty2,compound='left')
        self.deleteArticulo_button.pack(pady=10)
        
        #**CITAS FRAME**
        self.information_label = Label(self.citas_frame, text='Introduzca el rango de paginas si es necesario y seleccione el articulo',font=('Garamond',15),bg='pink',fg='black')
        self.information_label.pack(side='top')
        
        self.rango_label = Label(self.citas_frame, text='Rango de paginas',font=('Garamond',20),bg='pink',fg='black')
        self.rango_label.pack(pady=20)
        
        self.rango_text = Entry(self.citas_frame, bg='white', fg='black', font=('Garamond',20))
        self.rango_text.pack(pady=10)
        
        self.articulos_label = Label(self.citas_frame, text='Articulos',font=('Garamond',20),bg='pink',fg='black')
        self.articulos_label.pack(pady=10)
        
        articulos = controlCitas.selectArticulos()
        self.combo_articulos = ttk.Combobox(self.citas_frame, font=('Garamond',20),foreground='black',background='white',values=articulos,state='readonly')
        self.combo_articulos.pack(pady=15)   
        
        self.cita = StringVar()
        
        self.cita_label = Label(self.citas_frame, font=('Garamond',15),bg='white',fg='black',textvariable=self.cita,width=40)
        self.cita_label.pack(pady=15)
        
        self.generate_button = Button(self.citas_frame, text='Generar cita',font=('Garamond',20),bg='white',fg='black',height=85,command=self.crearCita,image=kitty,compound='left')
        self.generate_button.pack(pady=20)
        
        self.copy_button = Button(self.citas_frame, text='Copiar cita', font=('Garamond',20), fg='black',bg='white',height=80,command=self.copyCita,image=kitty2,compound='left')
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
                self.autores_text['values'] = []
                autores = controlCitas.selectAutores()
                for index in range(len(autores)):
                    self.list_autores.insert(self.list_autores.size(),autores[index])
                messagebox.showinfo(title='Insercion',message='Exito al insertar')
                self.name_text.delete(0,END)
                self.autores_text.config(values=autores)
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
                    self.autores_text['values'] = []
                    autores = controlCitas.selectAutores()
                    for index in range(len(autores)):
                        self.list_autores.insert(self.list_autores.size(),autores[index])
                    self.name_text.delete(0,END)
                    self.autores_text.config(values=autores)
                    self.subname_text.delete(0,END)
                    autor.deleteArticulo()
                    articulos_distintos = controlCitas.selectDistinctArticulos()
                    if articulos_distintos != []:
                        for index in range(len(articulos_distintos)):
                            año,edicion,lugar,editorial = controlCitas.selectArticulos_Completos(nombre=articulos_distintos[index])
                            articulo= Articulos.Articulos(articulos_distintos[index],año,edicion,lugar,editorial)
                            articulo.Delete()
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
                self.editorial_text['values'] = []
                self.list_editorial.delete(0,END)
                editoriales = controlCitas.selectEditoriales()
                self.editorial_text.config(values=editoriales)
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
                    self.editorial_text['values'] = []
                    self.list_editorial.delete(0,END)
                    editoriales = controlCitas.selectEditoriales()
                    self.editorial_text.config(values=editoriales)
                    for index in range(len(editoriales)):
                        self.list_editorial.insert(self.list_editorial.size(),editoriales[index])
                    editorial.deleteArticulo()
                    articulos_faltantes = controlCitas.selectDistinctArticulos_editorial()
                    if articulos_faltantes != []:
                        for index in range(len(articulos_faltantes)):
                            controlCitas.deleteAutor_Articulo(articulos_faltantes[index])
                    
                except Exception:
                    messagebox.showerror(title='Eliminar',message='Error al eliminar')
        else:
            messagebox.showerror(title='Eliminar',message='Error, nombre vacio')
    
    def insertarArticulo(self):
        if self.articuloName_text.get() != '' and self.edicion_text.get() != '' and self.año_text.get() != '' and self.lugar_text.get() != '' and self.editorial_text.get() != '' and self.autores_text.get() != '':
            partes = self.autores_text.get().split()
            articulo = Articulos.Articulos(self.articuloName_text.get(),self.año_text.get(),self.edicion_text.get(),self.lugar_text.get(),self.editorial_text.get())
            articulos = controlCitas.selectArticulos()
            if articulo.nombre in articulos:
                    try:
                        articulo.insertArticulo_autor(partes[1],partes[0])
                        messagebox.showinfo(title='Insertar',message='Insertado con exito')
                        self.articuloName_text.delete(0,END)
                        self.año_text.delete(0,END)
                        self.edicion_text.delete(0,END)
                        self.lugar_text.delete(0,END)
                        self.editorial_text.set('')
                        articulos = controlCitas.selectArticulos_Autor(partes[1],partes[0])
                        self.list_articulos.delete(0,END)
                        articulos2 = controlCitas.selectArticulo_autor()
                        self.combo_articulos['values'] = []
                        self.combo_articulos.config(values=articulos2)
                        for index in range(len(articulos)):
                            self.list_articulos.insert(self.list_articulos.size(),articulos[index])
                    except Exception:
                        messagebox.showerror(title='Insertar',message='Ha ocurrido un error')
                        
            else:
                    try:
                        articulo.insert()
                    except Exception:
                        messagebox.showerror(title='Insertar',message='Ha ocurrido un error')
                    try:
                        articulo.insertArticulo_autor(partes[1],partes[0])
                        messagebox.showinfo(title='Insertar',message='Insertado con exito')
                        self.articuloName_text.delete(0,END)
                        self.año_text.delete(0,END)
                        self.edicion_text.delete(0,END)
                        self.lugar_text.delete(0,END)
                        self.editorial_text.set('')
                        articulos = controlCitas.selectArticulos_Autor(partes[1],partes[0])
                        self.list_articulos.delete(0,END)
                        for index in range(len(articulos)):
                            self.list_articulos.insert(self.list_articulos.size(),articulos[index])
                        articulos2 = controlCitas.selectArticulo_autor()
                        self.combo_articulos['values'] = []
                        self.combo_articulos.config(values=articulos2)
                    except Exception:
                        messagebox.showerror(title='Insertar',message='Ha ocurrido un error')
        else:
            messagebox.showerror(title='Insertar',message='Error.Faltan campos')
    
    def rellenarArticulo(self,event):
        try:
            nombre_apellido = self.autores_text.get()
            self.autores_text.delete(0,END)
            articulo = self.articuloName_text.get()
            self.articuloName_text.delete(0,END)
            año = self.año_text.get()
            self.año_text.delete(0,END)
            lugar = self.lugar_text.get()
            self.lugar_text.delete(0,END)
            edicion = self.edicion_text.get()
            self.edicion_text.delete(0,END)
            editorial = self.editorial_text.get()
            self.editorial_text.delete(0,END)
            if nombre_apellido:
                partes = nombre_apellido.split()
                self.list_articulos.delete(0,END)
                articulos = controlCitas.selectArticulos_Autor(partes[1],partes[0])
                for index in range(len(articulos)):
                    self.list_articulos.insert(self.list_articulos.size(),articulos[index])
                self.articuloName_text.insert(0,articulo)
                self.año_text.insert(0,año)
                self.lugar_text.insert(0,lugar)
                self.edicion_text.insert(0,edicion)
                self.editorial_text.set(editorial)
                return
        except Exception:
            pass
    
    def rellenarCampos_Articulo(self,event):
        try:
            if self.list_articulos.curselection() != '' and self.list_articulos.size() > 0:
                self.articuloName_text.delete(0,END)
                self.año_text.delete(0,END)
                self.edicion_text.delete(0,END)
                self.lugar_text.delete(0,END)
                self.editorial_text.set('')
                nombre = self.list_articulos.get(self.list_articulos.curselection())
                año,edicion,lugar,editorial = controlCitas.selectArticulos_Completos(nombre=nombre)
                self.articuloName_text.insert(0,nombre)
                self.año_text.insert(0,año)
                self.edicion_text.insert(0,edicion)
                self.lugar_text.insert(0,lugar)
                self.editorial_text.set(editorial)
        except Exception:
            pass
    
    def deleteArticulo(self):
        if self.articuloName_text.get() != '' and self.edicion_text.get() != '' and self.año_text.get() != '' and self.lugar_text.get() != '' and self.editorial_text.get() != '' and self.autores_text.get() != '':
            if messagebox.askyesno(title='Eliminar',message='¿Seguro que desea eliminar?'):
                articulo = Articulos.Articulos(self.articuloName_text.get(),self.año_text.get(),self.edicion_text.get(),self.lugar_text.get(),self.editorial_text.get())
                try:
                    articulo.Delete_autor_articulo()
                    articulo.Delete()
                    messagebox.showinfo(title='Eliminar',message='Eliminado con exito')
                    self.articuloName_text.delete(0,END)
                    self.año_text.delete(0,END)
                    self.lugar_text.delete(0,END)
                    self.edicion_text.delete(0,END)
                    self.editorial_text.set('')
                    partes = self.autores_text.get().split()
                    articulos = controlCitas.selectArticulos_Autor(partes[1],partes[0])
                    self.list_articulos.delete(0,END)
                    articulos2 = controlCitas.selectArticulo_autor()
                    self.combo_articulos['values'] = []
                    self.combo_articulos.config(values=articulos2)
                    for index in range(len(articulos)):
                        self.list_articulos.insert(self.list_articulos.size(),articulos[index])
                except Exception:
                    messagebox.showerror(title='Eliminar',message='Error al eliminar')
        else:
            messagebox.showerror(title='Eliminar',message='Error, faltan campos')
            
    def copyCita(self):
        texto = self.cita.get()
        pyperclip.copy(texto)
        messagebox.showinfo(title='Copiar',message='Copiado')
    
    def crearCita(self):
        nombreArticulo = self.combo_articulos.get()
        try:
            cita = controlCitas.crearCita(nombre=nombreArticulo,rango=self.rango_text.get())
            self.cita.set(cita)
        except IndexError:
            messagebox.showerror(title='Generar cita', message='No hay articulo seleccionado')
                        