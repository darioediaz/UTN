from gestor_bodega import GestorImportBodega

class PantallaImportBodega():

    def habilitar_ventana(self):

        gestor = GestorImportBodega()
        bodegas_a_actualizar = gestor.importar_actualizacion_vinos_bodega()
        self.solicitar_seleccion_bodegas(bodegas_a_actualizar)

    def solicitar_seleccion_bodegas(self, bodegas_a_actualizar):
        i = 1
        print("Bodegas con actualizaciones pendientes:\n")
        for bodega in bodegas_a_actualizar:
            print(f"{i})-{bodega}\n")
            i = i + 1
        seleccion = int(input("Seleccione el número de la bodega que desea actualizar:"))
        self.tomar_seleccion_bodega(seleccion)

    def tomar_seleccion_bodega(self, seleccion):
        print(seleccion)
        pass