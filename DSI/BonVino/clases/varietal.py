class Varietal:
    def __init__(self, descripcion, porcentaje, tipo_uva):
        self.descripcion = descripcion
        self.porcentaje_composicion = porcentaje
        self.tipo_uva = tipo_uva       
        
     # setters
    def set_descripcion(self, nuevo_descripcion):
        self.descripcion = nuevo_descripcion    
        
    def set_porcentaje_composicion(self, nuevo_porcentaje):
        self.porcentaje_composicion = nuevo_porcentaje  
        
    def set_tipo_uva(self, nueva_uva):
        self.tipo_uva = nueva_uva

    # getters
    def conocer_tipo_uva(self):
        return self.tipo_uva
    
    def conocer_porcentaje_composicion(self):
        return self.porcentaje_composicion
    
    def conocer_descripcion(self):
        return self.descripcion
    
    # funcion del metodo es_de_tipo_uva
    def es_de_tipo_uva(self, tipo_uva):
        return self.tipo_uva == tipo_uva
    
    