# Importar las clases y módulos necesarios

from PantallaImportBodega import PantallaImportBodega
from GestorImportBodega import GestorImportBodega
from TipoUva import TipoUva
from Bodega import Bodega
from Vino import Vino
from Enofilo import Enofilo
from Usuario import Usuario
from Maridaje import Maridaje
from Varietal import Varietal


def main():
    # Crear objetos y utilizar los métodos

    pantalla = PantallaImportBodega()
    pantalla.habilitarVentana()

    gestor = GestorImportBodega()
    gestor.opImportarActualizacionVinosBodega()

    tipo_uva = TipoUva("Cabernet Sauvignon")
    tipo_uva.sosTipoUva()

    bodega = Bodega("Bodega X", "Una bodega en Argentina")
    bodega.estaParaActualizarNovedadesVino()

    vino = Vino("Malbec", 200)
    vino.sosEsteVino()
    vino.setPrecio(250)

    enofilo = Enofilo("Juan", "Pérez")
    enofilo.seguisABodega(bodega)

    usuario = Usuario("Usuario1", "contraseña123")
    usuario.getNombre()

    maridaje = Maridaje("Carnes Rojas", "Maridaje ideal con carnes rojas")
    maridaje.sosMaridaje()

    varietal = Varietal("Malbec", 70)
    varietal.mostrarPorcentaje()


if __name__ == "__main__":
    main()