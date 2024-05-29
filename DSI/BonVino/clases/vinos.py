from clases.varietal import Varietal

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

    # funcion del metodo sos_este_vino
    def sos_este_vino(vino_a_actualizar, vinos_de_bodega):
        for vino in vinos_de_bodega:
            if vino.nombre == vino_a_actualizar.nombre:
                return True
        return False
            
    # funciones del metodo set_precio
    def set_precio(vino_original, precio):
        vino_original.precio = precio

    # funciones del metodo set_nota_cata_bodega
    def set_nota_cata_bodega(vino_original, nota_de_cata_bodega):
        vino_original.nota_cata = nota_de_cata_bodega

    # funcion del metodo set_imagen_etiqueta
    def set_imagen_etiqueta(vino_original, imagen_etiqueta):
        vino_original.imagen_etiqueta = imagen_etiqueta

    # funcion del metodo set_fecha_actualizacion
    def set_fecha_actualizacion(vino_original, fecha):
        vino_original.fecha_actualizacion = fecha

    # funciones del metodo crear_varietal
    def crear_varietal(varietales):
        for varietal in varietales:
            Varietal(varietal.descripcion, varietal.porcentaje_composicion, varietal.tipo_uva)

    # funcion para mostrar el toString de vinos y sus atributos 
    def __str__(self):
        varietales_str = "\n".join([f"{varietal.descripcion} ({varietal.porcentaje_composicion}%) ◙ Tipo de uva: {varietal.tipo_uva.nombre}" for varietal in self.varietal])
        maridajes_str = "\n".join([f"{maridaje.nombre}: {maridaje.descripcion}" for maridaje in self.maridaje])

        return (f"\n◙ Nombre: {self.nombre}\n"
                f"◙ Añada: {self.añada}\n"
                f"◙ Imagen de la etiqueta: {self.imagen_etiqueta}\n"
                f"◙ Nota de cata de la bodega: {self.nota_de_cata_bodega}\n"
                f"◙ Precio: {self.precio}\n"
                f"◙ Fecha de última actualización: {self.fecha_actualizacion}\n"
                f"◙ Varietales: {varietales_str}\n"
                f"◙ Maridajes: {maridajes_str}\n"
                f"◙ Bodega: {self.bodega.nombre}\n")