from clases.pantalla_import_bodega import *
from clases.gestor_bodega import *

def main():
    gestor = GestorImportBodega()
    pantalla = PantallaImportBodega(gestor)
    pantalla.habilitar_ventana()

if __name__ == "__main__":
    main()