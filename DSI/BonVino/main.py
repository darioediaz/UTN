from clases.pantalla_import_bodega import *
from clases.gestor_bodega import *

def main():
    gestor = GestorImportBodega()
    pantalla = PantallaImportBodega(gestor)
    pantalla.op_importar_a_actualizacion_vinos_bodega()

if __name__ == "__main__":
    main()