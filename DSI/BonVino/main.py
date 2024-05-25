from DSI.BonVino.Boundary.InterfazNotificacionPush import InterfazNotificacionPush
from DSI.BonVino.Boundary.PantallaImportBodega import PantallaImportBodega
from DSI.BonVino.Control.GestorImportBodega import GestorImportBodega
from DSI.BonVino.Entity.Bodega import Bodega
from DSI.BonVino.Entity.Enofilo import Enofilo
from DSI.BonVino.Entity.Maridaje import Maridaje
from DSI.BonVino.Entity.TipoUva import TipoUva
from DSI.BonVino.Entity.Usuario import Usuario
from DSI.BonVino.Entity.Vino import Vino

pantalla = PantallaImportBodega()
pantalla.habilitarVentana()

gestor = GestorImportBodega()
gestor.opImportarActualizacionVinosBodega()
gestor.importarActualizacionVinosBodega()
gestor.buscarBodegaParaActualizar()
gestor.estaParaActualizarNovedadesVino()

bodega = Bodega()
bodega.tomarSeleccionBodega()
bodega.obtenerActualizacionVinos()

vino = Vino()
vino.sosEsteVino()
vino.actualizarCaracteristicasVinoExistente()
vino.setPrecio()
vino.setNotaCata()
vino.setImagenEtiqueta()
vino.setFechaActualizacion()
vino.crearVino()

maridaje = Maridaje()
maridaje.sosMaridaje()

tipo_uva = TipoUva()
tipo_uva.sosTipoUva()

enofilo = Enofilo()
enofilo.seguisABodega()

usuario = Usuario()
usuario.getNombre()

notificacion_push = InterfazNotificacionPush()
notificacion_push.notificarNovedadVinoParaBodega()

sistema_bodega = SistemaDeBodega()
sistema_bodega.buscarSeguidoresDeBodega()