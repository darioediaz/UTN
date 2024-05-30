class TipoUva:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
    
    # setters    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        
    def set_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion
        
    # getters
    def conocer_descripcion(self):
        return self.descripcion
    
    def conocer_nombre(self):
        return self.nombre
        
    # funcion del metodo sos_tipo_uva
    def sos_tipo_uva(tipo_uva_seleccionada, tipos_uva):
        for tipo_uva in tipos_uva:
            if tipo_uva.nombre == tipo_uva_seleccionada.nombre:
                return True
        return False