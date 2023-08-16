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
    
    def selectArticulos(self):
        DBManager.selectArticulo_editorial(self.nombre)
        
    def deleteArticulos_editorial(self,articulos):
        DBManager.deleteArticulos_Editorial(articulos=articulos)