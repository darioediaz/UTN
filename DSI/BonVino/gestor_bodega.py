from clases.bodegas import Bodega
from mocks.bodegas_mock import bodegas_mock

class GestorImportBodega:
    def __init__(self):
        self.bodegas = bodegas_mock

    def importar_actualizacion_vinos_bodega(self):
        return(self.buscar_bodega_para_actualizar())

    def buscar_bodega_para_actualizar(self):
        bodegas_a_actualizar: Bodega = []
        for bodega in self.bodegas:
            if bodega.esta_para_actualizar_novedades_vino():
                bodegas_a_actualizar.append(bodega.nombre)
        return bodegas_a_actualizar

    
    def tomar_seleccion_bodega(self, bodega):
        self.obtener_actualizacion_vinos_bodega()


    def obtener_actualizacion_vinos_bodega(self):
        return 0

    def actualizar_sistema(self, actualizaciones):
        # Lógica para actualizar el sistema con las novedades importadas
        print("Actualizaciones realizadas:")
        print(actualizaciones)

    def notificar_enofilos(self, bodega, actualizaciones):
        self.notificador.enviar_notificacion(bodega, actualizaciones)
