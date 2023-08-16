from persistencia import DBManager

class Autores:
    
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def insert(self):
        DBManager.InsertAutor(self.nombre, self.apellido)
        
    def delete(self):
        DBManager.deleteAutor(self.nombre,self.apellido)
    
    def deleteArticulo(self):
        DBManager.deleteAutor_Articulo_autores(self.nombre, self.apellido)