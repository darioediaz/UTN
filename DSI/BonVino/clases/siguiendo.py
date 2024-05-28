class Siguiendo:
    def __init__(self, fecha_inicio, fecha_fin, amigo, bodega):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.amigo = amigo
        self.bodega = bodega
        
    def sos_de_bodega(self, bodega):
        return(self.bodega.nombre == bodega.nombre)
