class Bodega:
    def __init__(self, nombre, ubicacion, descripcion, historia, tiene_actualizacion, periodo_actualizacion, fecha_ultima_actualizacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.descripcion = descripcion
        self.historia = historia
        self.actualizaciones_disponibles = tiene_actualizacion
        self.periodo_actualizacion = periodo_actualizacion
        self.fecha_ultima_actualizacion = fecha_ultima_actualizacion

    def esta_para_actualizar_novedades_vino(self):
        return self.actualizaciones_disponibles

