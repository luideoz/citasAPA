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
    
    def insertArticulo_autor(self,nombreA,apellidoA):
        DBManager.InsertAutor_Articulo(nombreA=nombreA,apellidoA=apellidoA, articulo=self.nombre)
    
    def Delete_autor_articulo(self):
        DBManager.deleteAutor_Articulo(self.nombre)