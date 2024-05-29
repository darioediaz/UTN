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
        opciones = []
        print("\nBodegas con actualizaciones pendientes:\n")
        for bodega in bodegas_a_actualizar:
            opciones.append(bodega)
            print(f"{i})-{bodega.nombre}")
            i = i + 1

        opciones.append("Salir")
        print("0)-Salir\n")

        # Menu de seleccion de bodegas
        seleccion = None
        while seleccion != 0:
            seleccion = int(input("Seleccione el número de la bodega que desea actualizar (Ingrese 0 para salir): "))
            
            if seleccion > 0 or seleccion < i-1:
                self.tomar_seleccion_bodega(opciones[seleccion - 1])
            elif seleccion == 0: 
                print("Saliendo...\n")
            else:
                print("Esa opción no es válida. Por favor, seleccione un número válido.\n")
                

    # funcion para el metodo tomar_seleccion_bodegas()
    def tomar_seleccion_bodega(self, bodega):
        self.gestor.tomar_seleccion_bodega(bodega)

    # funcion para el metodo mostrar_resumen_vinos_importados()
    def mostrar_resumen_vinos_importados(bodega, vinos_actualizados, vinos_creados):
        print(f"\nVinos actualizados para bodega: {bodega.nombre}")
        for vino in vinos_actualizados:
            print(vino)
            print("\n")
        print(f"\nVinos creados para bodega: {bodega.nombre}")
        for vino in vinos_creados:
            print(vino)
            print("\n")
