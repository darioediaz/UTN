from gestor_bodega import *


class PantallaImportBodega:

    def __init__(self, gestor):
        self.gestor = gestor

    def habilitar_ventana(self):
        bodegas_a_actualizar = self.gestor.importar_actualizacion_vinos_bodega()
        self.solicitar_seleccion_bodegas(bodegas_a_actualizar)

    def solicitar_seleccion_bodegas(self, bodegas_a_actualizar):
        i = 1
        print("Bodegas con actualizaciones pendientes:\n")
        for bodega in bodegas_a_actualizar:
            print(f"{i})-{bodega.nombre}\n")
            i = i + 1
        seleccion = int(
            input("Seleccione el número de la bodega que desea actualizar:")
        )
        self.tomar_seleccion_bodega(bodegas_a_actualizar[seleccion - 1])

    def tomar_seleccion_bodega(self, bodega):
        self.gestor.tomar_seleccion_bodega(bodega)

    def mostrar_resumen_vinos_importados(bodega, vinos_actualizados, vinos_creados):
        print(f"Vinos actualizados para bodega: {bodega.nombre}")
        for vino in vinos_actualizados:
            print(vino)
            print("\n")
        print("\n\n")
        print(f"Vinos creados para bodega: {bodega.nombre}")
        for vino in vinos_creados:
            print(vino)
            print("\n")


gestor = GestorImportBodega()
pantalla = PantallaImportBodega(gestor)
pantalla.habilitar_ventana()
