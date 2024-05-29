class PantallaImportBodega():
    def __init__(self, gestor):
        self.gestor = gestor

    # funcion para el metodo habilitar_ventana
    def habilitar_ventana(self):
        bodegas_a_actualizar = self.gestor.importar_actualizacion_vinos_bodega()
        self.solicitar_seleccion_bodegas(bodegas_a_actualizar)

    # funcion para el metodo solicitar_seleccion_bodegas
    def solicitar_seleccion_bodegas(self, bodegas_a_actualizar):
        i = 1
        print("\nBodegas con actualizaciones pendientes:\n")
        for bodega in bodegas_a_actualizar:
            print(f"{i})-{bodega.nombre}")
            i = i + 1
        print("0) Salir\n")
        
        # menu para seleccionar bodegas
        while True:
            seleccion = int(input("Seleccione el numero de la bodega que desea actualizar (0 para salir): "))
            if seleccion == 0:
                print("Saliendo...\n")
                break
            elif seleccion < 1 or seleccion > i - 1:
                print("Esa opcion no es valida. Intente nuevamente.\n")
            else:
                self.tomar_seleccion_bodega(bodegas_a_actualizar[(seleccion) - 1])
        
    # funcion para el metodo tomar_seleccion_bodegas()
    def tomar_seleccion_bodega(self, bodega):
        self.gestor.tomar_seleccion_bodega(bodega)

    # funcion para el metodo mostrar_resumen_vinos_importados()
    def mostrar_resumen_vinos_importados(bodega, vinos_actualizados, vinos_creados):
        print(f"\nVinos ACTUALIZADOS para: {bodega.nombre}")
        for vino in vinos_actualizados:
            print(vino)
        print(f"\nVinos CREADOS para: {bodega.nombre}")
        for vino in vinos_creados:
            print(vino)