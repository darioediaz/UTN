#from mocks.vinos_mock import maridajes

class Maridaje:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        
        
    def sos_maridaje(maridaje_seleccionado, maridajes):
        for maridaje in maridajes:
            if maridaje.nombre == maridaje_seleccionado.nombre:
                return True
        return False