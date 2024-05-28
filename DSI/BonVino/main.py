from pantalla_import_bodega import PantallaImportBodega
from gestor_bodega import GestorImportBodega

def main():
    gestor = GestorImportBodega()
    pantalla = PantallaImportBodega(gestor)
    pantalla.habilitar_ventana()

if __name__ == "__main__":
    main()