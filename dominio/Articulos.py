from persistencia import DBManager

class Articulos:
    def __init__(self,nombre,año,edicion,lugar,editorial):
        
        self.nombre = nombre
        self.año = año
        self.edicion = edicion
        self.lugar = lugar
        self.editorial = editorial
        
    def insert(self):
        DBManager.InsertArticulo(self.nombre,self.año,self.edicion,self.lugar,self.editorial)
        
    def Delete(self):
        DBManager.deleteArticulo(self.nombre)