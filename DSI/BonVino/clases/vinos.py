class Vino:
    def __init__(self, nombre, añada, imagen, nota, precio, fecha_actualizacion, varietal, maridaje, bodega):
        self.nombre = nombre
        self.añada = añada
        self.imagen_etiqueta = imagen
        self.nota_de_cata_bodega = nota
        self.precio = precio
        self.fecha_actualizacion = fecha_actualizacion
        self.varietal = varietal
        self.maridaje = maridaje
        self.bodega = bodega

    def sos_este_vino(vino_a_actualizar, vinos_de_bodega):

        for vino in vinos_de_bodega:
            if vino.nombre == vino_a_actualizar.nombre:
                return True
        return False
            
    def set_precio(vino_original, precio):
        vino_original.precio = precio

    def set_nota_cata_bodega(vino_original, nota_de_cata_bodega):
        vino_original.nota_cata = nota_de_cata_bodega

    def set_imagen_etiqueta(vino_original, imagen_etiqueta):
        vino_original.imagen_etiqueta = imagen_etiqueta

    def set_fecha_actualizacion(vino_original, fecha):
        vino_original.fecha_actualizacion = fecha

    def __str__(self):
        maridajes = "\n".join([f"  - {maridaje.nombre}: {maridaje.descripcion}" for maridaje in self.maridaje])
        return (f"Nombre: {self.nombre}\n"
                f"Añada: {self.añada}\n"
                f"Imagen de la etiqueta: {self.imagen_etiqueta}\n"
                f"Nota de cata de la bodega: {self.nota_de_cata_bodega}\n"
                f"Precio: {self.precio}\n"
                f"Fecha de última actualización: {self.fecha_actualizacion}\n"
                f"Varietal: {self.varietal.descripcion} ({self.varietal.porcentaje_composicion}%) - Tipo de uva: {self.varietal.tipo_uva.nombre}\n"
                f"Maridajes:\n{maridajes}\n"
                f"Bodega: {self.bodega.nombre}")