from dominio import Autores
from persistencia import DBManager

def selectAutores():
    autores = DBManager.selectAutores()
    autores_procesado = []
    
    for index in range(len(autores)):
        name,subname = autores[index]
        subname_name = subname + ' ' + name
        autores_procesado.append(subname_name)
    
    return autores_procesado

def selectEditoriales():
    editoriales = DBManager.selectEditoriales()
    
    editoriales_procesado = []
    
    for index in range(len(editoriales)):
        editorial = editoriales[index][0]
        editoriales_procesado.append(editorial)
    
    return editoriales_procesado

def selectArticulos_Autor(nombre,apellido):
    articulos = DBManager.selectArticulos_Autor(nombreA=nombre,apellidoA=apellido)
    articulos_procesados = []
    
    for index in range(len(articulos)):
        articulo = articulos[index][0]
        articulos_procesados.append(articulo)
    
    return articulos_procesados

def selectArticulos():
    articulos = DBManager.selectArticulos()
    articulos_procesados = []
    for index in range(len(articulos)):
        nombre = articulos[index][0]
        articulos_procesados.append(nombre)
    return articulos_procesados

def selectArticulos_Completos(nombre):
    articulos = DBManager.selectArticulosCompletos(nombre=nombre)
    año,edicion,lugar,editorial = articulos[0]
    return año,edicion,lugar,editorial

def crearCita(nombre,rango):
    articulos = DBManager.selectArticulosCompletos(nombre=nombre)
    año,edicion,lugar,editorial = articulos[0]
    autor_articulos = DBManager.selectAutor_Articulo_Completo(articulo=nombre)
    cita = ''
    
    if len(autor_articulos) <= 2:
        for index in range(len(autor_articulos)):
            cita += autor_articulos[index][1].upper()
            cita += ' '+autor_articulos[index][0].upper() + ','
    else:
        cita += autor_articulos[0][1].upper()
        cita += ' '+autor_articulos[0][0].upper() +'et al.'
    
    if rango == '':
        cita += nombre + ',' + lugar + ',' + editorial + ',' + str(año)
    else:
        cita += nombre + ',' + rango + ',' +lugar + ',' + editorial + ',' + str(año)
    
    return cita
        

def deleteAll():
    DBManager.deleteAll()

