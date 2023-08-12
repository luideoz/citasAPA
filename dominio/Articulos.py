from persistencia import DBManager

class Articulos:
    def __init__(self,nombre,año,edicion,nombreA,apellidoA,editorial):
        
        self.nombre = nombre
        self.año = año
        self.edicion = edicion
        self.nombreA = nombreA
        self.apellidoA = apellidoA
        self.editorial = editorial
        
    def insert(self):
        DBManager.InsertArticulo(self.nombre,self.año,self.edicion,self.nombreA,self.apellidoA,self.editorial)
        
    def Delete(self):
        DBManager.deleteArticulo(self.nombre)