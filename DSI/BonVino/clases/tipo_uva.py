class TipoUva:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def sos_tipo_uva(tipo_uva_seleccionada, tipos_uva):
        for tipo_uva in tipos_uva:
            if tipo_uva.nombre == tipo_uva_seleccionada.nombre:
                return True
        return False
