from clases.enofilo import Enofilo
from clases.usuario import Usuario
from clases.siguiendo import Siguiendo
from mocks.vinos_mock import vinos_mock
from mocks.bodegas_mock import bodegas_mock

# mock de usuarios
usuarios_mock = [
    Usuario("enrique_gonzalez", "password123", False),
    Usuario("carlo_rossi", "wineLover456", True),
    Usuario("sofia_gomez", "securePass789", False),
    Usuario("lucas_fernandez", "myPassword321", True),
    Usuario("isabella_martinez", "bestWine2024", False),
]

# mock de seguidores
siguiendo_mock = [
    Siguiendo("2024-05-01", None, [], bodegas_mock[6]),
    Siguiendo("2024-06-01", None, [], bodegas_mock[1]),
    Siguiendo("2024-07-01", None, [], bodegas_mock[7])
]

# mock de enofilos
enofilos_mock = [
    Enofilo("Enrique", "Gonzalez", "imagen1.jpg", usuarios_mock[0], [siguiendo_mock[1]], [vinos_mock[0]]),
    Enofilo("Carlo", "Rossi", "imagen2.jpg", usuarios_mock[1], [siguiendo_mock[0]], []),
    Enofilo("Sofia", "Gomez", "imagen3.jpg", usuarios_mock[2], [], [vinos_mock[7]]),
    Enofilo("Lucas", "Fernandez", "imagen4.jpg", usuarios_mock[3], [], []),
    Enofilo("Isabella", "Martinez", "imagen5.jpg", usuarios_mock[4], [siguiendo_mock[2]], [vinos_mock[9], vinos_mock[3]]),
]