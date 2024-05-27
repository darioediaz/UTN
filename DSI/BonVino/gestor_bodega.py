from clases.bodegas import Bodega
from mocks.bodegas_mock import bodegas_mock
from mocks.actualizaciones_mock import vinos_a_actualizar_mock
from mocks.vinos_mock import vinos_mock

class GestorImportBodega:
    def __init__(self):
        self.bodega = Bodega
        self.bodegas = bodegas_mock
        self.vinos_a_actualizar = vinos_a_actualizar_mock
        self.vinos = vinos_mock

    def importar_actualizacion_vinos_bodega(self):
        return(self.buscar_bodega_para_actualizar())

    def buscar_bodega_para_actualizar(self):
        bodegas_a_actualizar: Bodega = []
        for bodega in self.bodegas:
            if bodega.esta_para_actualizar_novedades_vino():
                bodegas_a_actualizar.append(bodega)
        return bodegas_a_actualizar

    
    def tomar_seleccion_bodega(self, bodega):
        self.obtener_actualizacion_vinos_bodega(bodega)


    def obtener_actualizacion_vinos_bodega(self, bodega):
        actualizacion_vinos = self.bodega.obtener_actualizacion_vinos(bodega, self.vinos_a_actualizar)
        self.determinar_vinos_a_actualizar(bodega, actualizacion_vinos)

    def determinar_vinos_a_actualizar(self, bodega, actualizacion_vinos):
        vinos_a_actualizar = []
        vinos_a_crear = []
        vinos_a_actualizar, vinos_a_crear = bodega.tenes_este_vino(actualizacion_vinos, self.vinos)
        self.actualizar_o_crear_vino(bodega, vinos_a_actualizar, vinos_a_crear)

    def actualizar_o_crear_vino(self, bodega, vinos_a_actualizar, vinos_a_crear):
        for vino in vinos_a_actualizar:
            self.actualizar_caracteristicas_vino_existente(bodega, vino, self.vinos)
            pass

        for vino in vinos_a_crear:
            pass

    def actualizar_caracteristicas_vino_existente(self, bodega, vino, vinos):
        bodega.actualizar_datos_vino(vino, vinos)