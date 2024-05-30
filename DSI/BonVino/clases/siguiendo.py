class Siguiendo:
    def __init__(self, fecha_inicio, fecha_fin, amigo, bodega):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.amigo = amigo
        self.bodega = bodega
        
    # setters
    def set_bodega(self, bodega):
        self.bodega = bodega
        
    def set_amigo(self, amigo):
        self.amigo = amigo
    
    def set_fecha_inicio(self, fecha_inicio):
        self.fecha_inicio = fecha_inicio
    
    def set_fecha_fin(self, fecha_fin):
        self.fecha_fin = fecha_fin    
        
    # getters
    def get_bodega(self):
        return(self.bodega)
    
    def get_amigo(self):
        return(self.amigo)
    
    def get_fecha_inicio(self):
        return(self.fecha_inicio)
    
    def get_fecha_fin(self):
        return(self.fecha_fin)
        
    # funcion del metodo sos_de_bodega
    def sos_de_bodega(self, bodega):
        return(self.bodega.nombre == bodega.nombre)
