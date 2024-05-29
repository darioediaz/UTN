from clases.bodegas import Bodega
from clases.maridaje import Maridaje
from clases.tipo_uva import TipoUva
from clases.vinos import Vino
from pantalla_import_bodega import PantallaImportBodega
from mocks.bodegas_mock import *
from mocks.actualizaciones_mock import *
from mocks.vinos_mock import *
from mocks.enofilos_mock import enofilos_mock

import datetime

class GestorImportBodega:
    def __init__(self):
        self.bodega = Bodega
        self.maridaje = Maridaje
        self.tipo_uva = TipoUva
        self.vino = Vino
        self.bodegas = bodegas_mock
        self.vinos_a_actualizar = vinos_a_actualizar_mock
        self.vinos = vinos_mock
        self.maridajes = maridajes_mock
        self.tipos_uva = tipos_uva_mock
        self.varietales = varietales_mock
        
    # funcion del metodo importar_actualizacion_vinos_bodega
    def importar_actualizacion_vinos_bodega(self):
        return(self.buscar_bodega_para_actualizar())
    
    # funcion del metodo importar_actualizacion_vinos_bodega
    def buscar_bodega_para_actualizar(self):
        bodegas_a_actualizar: Bodega = []
        for bodega in self.bodegas:
            if bodega.esta_para_actualizar_novedades_vino():
                bodegas_a_actualizar.append(bodega)
        return bodegas_a_actualizar

    # funcion del metodo tomar_seleccion_bodega    
    def tomar_seleccion_bodega(self, bodega):
        self.obtener_actualizacion_vinos_bodega(bodega)

    # funcion del metodo tomar_seleccion_bodega
    def obtener_actualizacion_vinos_bodega(self, bodega):
        actualizacion_vinos = self.bodega.obtener_actualizacion_vinos(bodega, self.vinos_a_actualizar)
        self.determinar_vinos_a_actualizar(bodega, actualizacion_vinos)
        
    # funcion del metodo tomar_seleccion_bodega
    def determinar_vinos_a_actualizar(self, bodega, actualizacion_vinos):
        vinos_a_actualizar = []
        vinos_a_crear = []
        vinos_a_actualizar, vinos_a_crear = bodega.tenes_este_vino(actualizacion_vinos, self.vinos)
        self.actualizar_o_crear_vino(bodega, vinos_a_actualizar, vinos_a_crear)

    # funcion del metodo tomar_seleccion_bodega
    def actualizar_o_crear_vino(self, bodega, vinos_a_actualizar, vinos_a_crear):
        for vino in vinos_a_actualizar:
            vinos_actualizados = self.actualizar_caracteristicas_vino_existente(bodega, vino, self.vinos)

        for vino in vinos_a_crear:
            vinos_creados = self.crear_vino(bodega, vino)
        
        if vinos_actualizados and vinos_creados:
            PantallaImportBodega.mostrar_resumen_vinos_importados(bodega, vinos_a_actualizar, vinos_a_crear)
            self.buscar_seguidores_bodega(bodega)

    # funcion del metodo tomar_seleccion_bodega
    def actualizar_caracteristicas_vino_existente(self, bodega, vino, vinos):
        return(bodega.actualizar_datos_vino(vino, vinos))
    
    # funcion del metodo tomar_seleccion_bodega
    def crear_vino(self, bodega, vino):
        return(self.buscar_maridaje(bodega, vino))
        
    # funcion del metodo tomar_seleccion_bodega
    def buscar_maridaje(self, bodega, vino):
        for maridaje in vino.maridaje:
            if(self.maridaje.sos_maridaje(maridaje, self.maridajes)):
                return(self.buscar_tipo_uva(vino, bodega))
    
    # funcion del metodo tomar_seleccion_bodega           
    def buscar_tipo_uva(self, vino, bodega):
        for varietal in vino.varietal:
            if(not self.tipo_uva.sos_tipo_uva(varietal.tipo_uva, self.tipos_uva)):
                return "Tipo de uva inexistente"
        return(self.crear_vinos(vino, bodega))
    
    # funcion del metodo tomar_seleccion_bodega
    def crear_vinos(self, vino, bodega):
        self.vino(vino.nombre, vino.añada, vino.imagen_etiqueta, vino.nota_de_cata_bodega, vino.precio, vino.fecha_actualizacion, vino.varietal, vino.maridaje, vino.bodega)
        self.vino.crear_varietal(vino.varietal)
        bodega.set_fecha_ultima_actualizacion(datetime.datetime.now())
        return True
    
    # funcion del metodo tomar_seleccion_bodega
    def buscar_seguidores_bodega(self, bodega):
        for enofilo in enofilos_mock:
            usuario = enofilo.seguis_a_bodega(bodega)
        if usuario != None:
            print(f"Notificar cambio actualizacion de bodegas al usuario: {usuario}\n")
        else:
            print(f"La {bodega.nombre} no tiene seguidores a quien notificar\n")
        
