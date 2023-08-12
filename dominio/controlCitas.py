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
        editorial = editoriales[index]
        editoriales_procesado.append(editorial)
    
    return editoriales_procesado

def selectArticulos():
    articulos = DBManager.selectArticulos()
    articulos_procesados = []
    for index in range(len(articulos)):
        nombre,año,edicion,nombreA,apellidoA,editorial = articulos[index]
        articulos_procesados.append(nombre)
    return articulos_procesados

def selectArticulos_Completos(nombre):
    articulos = DBManager.selectArticulosCompletos(nombre=nombre)
    año,edicion,nombreA,apellidoA,editorial = articulos[0]
    return año,edicion,nombreA,apellidoA,editorial

def crearCita(nombre,rango):
    articulos = DBManager.selectArticulosCompletos(nombre=nombre)
    año,edicion,nombreA,apellidoA,editorial = articulos[0]
    if rango != '':
        cita = apellidoA + ' ' + nombreA + '.(' + str(año) + ').' + nombre + rango + '.' + editorial
    else:
         cita = apellidoA + ' ' + nombreA + '.(' + str(año) + ').' + nombre +  '.' + editorial
    return cita

def deleteAll():
    DBManager.deleteAll()

