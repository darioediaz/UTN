from clases.vinos import Vino


class Bodega:
    def __init__(
        self,
        nombre,
        ubicacion,
        descripcion,
        historia,
        tiene_actualizacion,
        periodo_actualizacion,
        fecha_ultima_actualizacion,
    ):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.descripcion = descripcion
        self.historia = historia
        self.actualizaciones_disponibles = tiene_actualizacion
        self.periodo_actualizacion = periodo_actualizacion
        self.fecha_ultima_actualizacion = fecha_ultima_actualizacion

    def esta_para_actualizar_novedades_vino(self):
        return self.actualizaciones_disponibles

    def obtener_actualizacion_vinos(bodega, vinos_a_actualizar):
        return [vino for vino in vinos_a_actualizar if vino.bodega == bodega]

    def tenes_este_vino(self, vinos_seleccionados, vinos):
        vinos_a_actualizar = []
        vinos_a_crear = []
        vinos_de_bodega = self.obtener_actualizacion_vinos(vinos)
        for vino in vinos_seleccionados:
            if Vino.sos_este_vino(vino, vinos_de_bodega):
                vinos_a_actualizar.append(vino)
            else:
                vinos_a_crear.append(vino)

        return vinos_a_actualizar, vinos_a_crear

    def actualizar_datos_vino(self, vino_a_actualizar, vinos):
        vinos_de_bodega = self.obtener_actualizacion_vinos(vinos)
        for vino in vinos_de_bodega:
            if vino.nombre == vino_a_actualizar.nombre:
                Vino.set_precio(vino, vino_a_actualizar.precio)
                Vino.set_nota_cata_bodega(vino, vino_a_actualizar.nota_de_cata_bodega)
                Vino.set_imagen_etiqueta(vino, vino_a_actualizar.imagen_etiqueta)
                Vino.set_fecha_actualizacion(
                    vino, vino_a_actualizar.fecha_actualizacion
                )

        return True

    def set_fecha_ultima_actualizacion(self, fecha):
        self.fecha_ultima_actualizacion = fecha
