from persistencia import DBManager

class Editoriales:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def insert(self):
        DBManager.InsertEditorial(self.nombre)
        
    def Delete(self):
        DBManager.deleteEditorial(self.nombre)
    
    def deleteArticulo(self):
        DBManager.deleteArticulo_editorial(self.nombre)