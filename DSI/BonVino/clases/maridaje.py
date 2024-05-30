#from mocks.vinos_mock import maridajes

class Maridaje:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        
    # setters
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion
        
    # getters
    def get_nombre(self):
        return self.nombre
    
    def get_descripcion(self):
        return self.descripcion        
            
    # funcion del metodo sos_maridaje
    def sos_maridaje(maridaje_seleccionado, maridajes):
        for maridaje in maridajes:
            if maridaje.nombre == maridaje_seleccionado.nombre:
                return True
        return False