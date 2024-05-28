from pantalla_import_bodega import *
from gestor_bodega import *


def main():
    gestor = GestorImportBodega()
    pantalla = PantallaImportBodega(gestor)
    pantalla.habilitar_ventana()


if __name__ == "__main__":
    main()
