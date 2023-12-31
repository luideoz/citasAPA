import sqlite3 as sql

#insert functions
def InsertAutor(nombre,apellido):
    conn = sql.connect('autores.db')
    cursor = conn.cursor()
    instruction = f"INSERT INTO autores VALUES ('{nombre}','{apellido}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()
    
def InsertEditorial(nombre):
    conn = sql.connect('editoriales.db')
    cursor = conn.cursor()
    instruction = f"INSERT INTO editoriales VALUES ('{nombre}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def InsertArticulo(nombre,año,edicion,lugar,editorial):
    conn = sql.connect('articulos.db')
    cursor = conn.cursor()
    instruction = f"INSERT INTO articulos VALUES ('{nombre}',{int(año)},{int(edicion)},'{lugar}','{editorial}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def InsertAutor_Articulo(nombreA,apellidoA,articulo):
    conn = sql.connect('autor_articulo.db')
    cursor = conn.cursor()
    instruction = f"INSERT INTO autor_articulo VALUES ('{nombreA}','{apellidoA}','{articulo}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close()
    
#create functions
def createAutores():
    conn = sql.connect('autores.db')
    cursor = conn.cursor()
    instruction = "CREATE TABLE autores( nombre text NOT NULL, apellido text NOT NULL, PRIMARY KEY(nombre,apellido))"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def createArticulos():
    conn = sql.connect('articulos.db')
    cursor = conn.cursor()
    instruction = "CREATE TABLE articulos(nombre text PRIMARY KEY NOT NULL, año integer NOT NULL, Edicion integer NOT NULL,lugar text NOT NULL,editorial text NOT NULL, FOREIGN KEY(editorial) REFERENCES editoriales(nombre) ON DELETE CASCADE)"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def createEditoriales():
    conn = sql.connect('editoriales.db')
    cursor = conn.cursor()
    instruction = "CREATE TABLE editoriales(nombre text PRIMARY KEY NOT NULL)"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def createAutor_Articulo():
    conn = sql.connect('autor_articulo.db')
    cursor = conn.cursor()
    instruction = "CREATE TABLE autor_articulo (nombreA TEXT, apellidoA TEXT, articulo TEXT,PRIMARY KEY (nombreA, apellidoA, articulo),FOREIGN KEY (nombreA, apellidoA) REFERENCES autores(nombre, apellido),FOREIGN KEY (articulo) REFERENCES articulos(nombre))"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

#delete functions
def deleteAutor(nombre,apellido):
    conn = sql.connect('autores.db')
    cursor = conn.cursor()
    instruction = f"DELETE FROM autores WHERE nombre='{nombre}' and apellido='{apellido}'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()
    
def deleteEditorial(nombre):
    conn = sql.connect('editoriales.db')
    cursor = conn.cursor()
    instruction = f"DELETE FROM editoriales WHERE nombre='{nombre}'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def deleteArticulo(nombre):
    conn = sql.connect('articulos.db')
    cursor = conn.cursor()
    instruction = f"DELETE FROM articulos WHERE nombre='{nombre}'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def deleteAutor_Articulo(articulo):
    conn = sql.connect('autor_articulo.db')
    cursor = conn.cursor()
    instruction = f"DELETE FROM autor_articulo WHERE articulo='{articulo}'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()
    
def deleteAutor_Articulo_autores(nombreA,apellidoA):
    conn = sql.connect('autor_articulo.db')
    cursor = conn.cursor()
    instruction = f"DELETE FROM autor_articulo WHERE nombreA='{nombreA}' AND apellidoA='{apellidoA}'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def deleteArticulo_editorial(nombre):
    conn = sql.connect('articulos.db')
    cursor = conn.cursor()
    instruction = f"DELETE FROM articulos WHERE editorial = '{nombre}'"
    cursor.execute(instruction)
    conn.commit()
    conn.close()

def deleteArticulos_Editorial(articulos):
    conn =sql.connect('autor_articulo.db')
    cursor = conn.cursor()
    instruction = "DELETE FROM autor_articulo WHERE articulo=?"
    cursor.executemany(instruction,articulos)
    conn.commit()
    conn.close() 

def deleteAll():
    conn = sql.connect('articulos.db')
    cursor = conn.cursor()
    instruction1 = "DELETE FROM articulos"
    cursor.execute(instruction1)
    conn.commit()
    conn.close()
    
    conn = sql.connect('autores.db')
    cursor = conn.cursor()
    instruction2 = "DELETE FROM autores"
    cursor.execute(instruction2)
    conn.commit()
    conn.close()
    
    conn = sql.connect('editoriales.db')
    cursor = conn.cursor()
    instruction3 = "DELETE FROM editoriales"
    cursor.execute(instruction3)
    conn.commit()
    conn.close()
    
    conn = sql.connect('autor_articulo.db')
    cursor = conn.cursor()
    instruction3 = "DELETE FROM autor_articulo"
    cursor.execute(instruction3)
    conn.commit()
    conn.close()

#select functions

def selectAutores():
    conn = sql.connect('autores.db')
    cursor = conn.cursor()
    instruccion = "SELECT * FROM autores ORDER BY apellido"
    cursor.execute(instruccion)
    datos = cursor.fetchall() #para devolver la lista con los campos
    conn.commit()
    conn.close()
    return datos

def selectEditoriales():
    conn = sql.connect('editoriales.db')
    cursor = conn.cursor()
    instruccion = "SELECT * FROM editoriales ORDER BY nombre"
    cursor.execute(instruccion)
    datos = cursor.fetchall() #para devolver la lista con los campos
    conn.commit()
    conn.close()
    return datos

def selectArticulos():
    conn = sql.connect('articulos.db')
    cursor = conn.cursor()
    instruccion = "SELECT nombre FROM articulos ORDER BY nombre"
    cursor.execute(instruccion)
    datos = cursor.fetchall() #para devolver la lista con los campos
    conn.commit()
    conn.close()
    return datos

def selectArticulo_autor():
    conn = sql.connect('autor_articulo.db')
    cursor = conn.cursor()
    instruccion = "SELECT articulo FROM autor_articulo ORDER BY articulo"
    cursor.execute(instruccion)
    datos = cursor.fetchall() #para devolver la lista con los campos
    conn.commit()
    conn.close()
    return datos

def selectArticulo_autor2():
    conn = sql.connect('autor_articulo.db')
    cursor = conn.cursor()
    instruccion = "SELECT DISTINCT articulo FROM autor_articulo ORDER BY articulo"
    cursor.execute(instruccion)
    datos = cursor.fetchall() #para devolver la lista con los campos
    conn.commit()
    conn.close()
    return datos

def selectArticulos_Autor(nombreA,apellidoA):
    conn = sql.connect('autor_articulo.db')
    cursor = conn.cursor()
    instruccion = f"SELECT DISTINCT articulo FROM autor_articulo WHERE nombreA='{nombreA}' AND apellidoA= '{apellidoA}' ORDER BY articulo"
    cursor.execute(instruccion)
    datos = cursor.fetchall() #para devolver la lista con los campos
    conn.commit()
    conn.close()
    return datos


def selectArticulosCompletos(nombre):
    conn = sql.connect('articulos.db')
    cursor = conn.cursor()
    instruccion = f"SELECT año,Edicion,lugar,editorial FROM articulos WHERE nombre='{nombre}' ORDER BY nombre"
    cursor.execute(instruccion)
    datos = cursor.fetchall() #para devolver la lista con los campos
    conn.commit()
    conn.close()
    return datos

def selectAutor_Articulo_Completo(articulo):
    conn = sql.connect('autor_articulo.db')
    cursor = conn.cursor()
    instruccion = f"SELECT nombreA, apellidoA FROM autor_articulo WHERE articulo='{articulo}' ORDER BY apellidoA"
    cursor.execute(instruccion)
    datos = cursor.fetchall() #para devolver la lista con los campos
    conn.commit()
    conn.close()
    return datos

def selectArticulo_editorial(editorial):
    conn = sql.connect('articulos.db')
    cursor = conn.cursor()
    instruccion = f"SELECT nombre FROM articulos WHERE editorial='{editorial}'"
    cursor.execute(instruccion)
    datos = cursor.fetchall() #para devolver la lista con los campos
    conn.commit()
    conn.close()
    return datos



    

    
    