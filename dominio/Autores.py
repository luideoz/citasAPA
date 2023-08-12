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
        DBManager.deleteArticulo_autor(self.nombre, self.apellido)