from clases.vinos import Vino
from clases.maridaje import Maridaje
from clases.varietal import Varietal
from clases.tipo_uva import TipoUva
from mocks.bodegas_mock import bodegas_mock

# mock de tipos de uva
tipos_uva_mock = [
    TipoUva("Malbec", "Uva tinta de origen francés, típica de Argentina."),
    TipoUva("Cabernet Sauvignon", "Una de las variedades de uva tinta más conocidas."),
    TipoUva("Merlot", "Uva tinta, caracterizada por su suavidad y cuerpo."),
    TipoUva("Syrah", "Uva tinta que produce vinos especiados y con cuerpo."),
    TipoUva("Chardonnay", "Uva blanca, la más cultivada del mundo."),
    TipoUva("Tempranillo", "Uva tinta, autóctona de España."),
    TipoUva("Garnacha", "Uva tinta muy versátil y cultivada en varias regiones."),
    TipoUva("Pinot Noir", "Uva tinta de Borgoña, Francia, conocida por su dificultad de cultivo."),
    TipoUva("Zinfandel", "Uva tinta, muy popular en California."),
    TipoUva("Petit Verdot", "Uva tinta, usada principalmente en mezclas de Bordeaux."),
    TipoUva("Sauvignon Blanc", "Uva blanca, conocida por sus aromas herbáceos."),
    TipoUva("Carmenere", "Uva tinta, originaria de Bordeaux y muy cultivada en Chile."),
    TipoUva("Viognier", "Uva blanca, con aromas florales y frutales."),
    TipoUva("Albariño", "Uva blanca, típica de la región de Galicia en España."),
    TipoUva("Sangiovese", "Uva tinta, principal en la producción de Chianti en Italia."),
    TipoUva("Barbera", "Uva tinta, muy cultivada en el Piamonte italiano."),
    TipoUva("Moscato", "Uva blanca, utilizada para vinos dulces y espumantes."),
    TipoUva("Nebbiolo", "Uva tinta, conocida por sus taninos y acidez en el Piamonte italiano."),
    TipoUva("Grenache", "Uva tinta, muy cultivada en España y Francia."),
    TipoUva("Cabernet Franc", "Uva tinta, utilizada en mezclas de Bordeaux y varietales en el Valle del Loira.")
]

# mock de varietales
varietales_mock = [
    Varietal("Varietal de Malbec, 100% Malbec", 100, tipos_uva_mock[0]),
    Varietal("Varietal de Cabernet Sauvignon, 100% Cabernet Sauvignon", 100, tipos_uva_mock[1]),
    Varietal("Varietal de Merlot, 100% Merlot", 100, tipos_uva_mock[2]),
    Varietal("Varietal de Syrah, 100% Syrah", 100, tipos_uva_mock[3]),
    Varietal("Varietal de Chardonnay, 100% Chardonnay", 100, tipos_uva_mock[4]),
    Varietal("Varietal de Tempranillo, 100% Tempranillo", 100, tipos_uva_mock[5]),
    Varietal("Varietal de Garnacha, 100% Garnacha", 100, tipos_uva_mock[6]),
    Varietal("Varietal de Pinot Noir, 100% Pinot Noir", 100, tipos_uva_mock[7]),
    Varietal("Varietal de Zinfandel, 100% Zinfandel", 100, tipos_uva_mock[8]),
    Varietal("Varietal de Petit Verdot, 100% Petit Verdot", 100, tipos_uva_mock[9]),
    Varietal("Varietal de Sauvignon Blanc, 100% Sauvignon Blanc", 100, tipos_uva_mock[10]),
    Varietal("Varietal de Carmenere, 100% Carmenere", 100, tipos_uva_mock[11]),
    Varietal("Varietal de Viognier, 100% Viognier", 100, tipos_uva_mock[12]),
    Varietal("Varietal de Albariño, 100% Albariño", 100, tipos_uva_mock[13]),
    Varietal("Varietal de Sangiovese, 100% Sangiovese", 100, tipos_uva_mock[13]),
    Varietal("Varietal de Barbera, 100% Barbera", 100, tipos_uva_mock[15]),
    Varietal("Varietal de Moscato, 100% Moscato", 100, tipos_uva_mock[16]),
    Varietal("Varietal de Nebbiolo, 100% Nebbiolo", 100, tipos_uva_mock[17]),
    Varietal("Varietal de Grenache, 100% Grenache", 100, tipos_uva_mock[18]),
    Varietal("Varietal de Cabernet Franc, 100% Cabernet Franc", 100, tipos_uva_mock[19])
]

# mock de maridajes
maridajes_mock = [
    Maridaje("Carnes Rojas", "Ideal para acompañar con carnes rojas a la parrilla o asadas."),
    Maridaje("Quesos Curados", "Perfecto con una selección de quesos curados."),
    Maridaje("Pasta", "Acompaña bien con pastas con salsa de tomate."),
    Maridaje("Cordero", "Excelente con cordero asado o guisado."),
    Maridaje("Pescado", "Ideal con pescados a la parrilla o al horno."),
    Maridaje("Tapas", "Marida bien con una variedad de tapas."),
    Maridaje("Pollo", "Acompaña bien con pollo asado o a la parrilla."),
    Maridaje("Setas", "Ideal con platos de setas y hongos."),
    Maridaje("BBQ", "Perfecto para carnes a la barbacoa."),
    Maridaje("Bistec", "Excelente con un buen bistec a la parrilla."),
    Maridaje("Ensaladas", "Marida bien con ensaladas verdes y frescas."),
    Maridaje("Embutidos", "Acompaña bien con una selección de embutidos."),
    Maridaje("Quesos Suaves", "Perfecto con quesos suaves y cremosos."),
    Maridaje("Mariscos", "Ideal con mariscos frescos y a la parrilla."),
    Maridaje("Pizza", "Marida bien con pizza y platos italianos."),
    Maridaje("Guisos", "Acompaña bien con guisos de carne y legumbres."),
    Maridaje("Postres", "Perfecto para acompañar con postres dulces."),
    Maridaje("Caza", "Ideal con carnes de caza."),
    Maridaje("Embutidos", "Acompaña bien con una selección de embutidos.")
]

# mock de vinos a actualizar o crear (para simular actualizaciones provenientes de las bodegas)
vinos_a_actualizar_mock = [
    Vino("Gran Reserva 2018", 2018, "granreserva2018.jpg", "NUEVAS notas de frutos rojos y especias", 2550.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Malbec Premium 2017", 2017, "malbecpremium2017.jpg", "Aromas a ciruela y roble", 3000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Cabernet Sauvignon 2019", 2019, "cabernetsauvignon2019.jpg", "Cuerpo robusto y taninos suaves", 4500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Reserva Especial 2016", 2016, "reservaespecial2016.jpg", "NUEVAS notas de vainilla y chocolate", 5000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Chardonnay 2020", 2020, "chardonnay2020.jpg", "Aromas florales y cítricos", 3500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Merlot Selección 2015", 2015, "merlotseleccion2015.jpg", "Especiado con final largo", 6000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("NUEVO Syrah 2018", 2018, "syrah2018.jpg", "NUEVAS notas de frutas maduras", 4025.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Shiraz Barossa 2017", 2017, "shirazbarossa2017.jpg", "NUEVAS notas de mora y regaliz", 5525.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Pinot Noir 2019", 2019, "pinotnoir2019.jpg", "Estructurado con final persistente", 6525.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Gran Shiraz 2016", 2016, "granshiraz2016.jpg", "NUEVAS notas a cacao y tabaco", 7025.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Sauvignon Blanc 2020", 2020, "sauvignonblanc2020.jpg", "NUEVAS notas cítricas y minerales", 4525.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Vintage Reserve 2015", 2015, "vintagereserve2015.jpg", "Especiado con final persistente", 7525.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("NUEVO Tropical Blend 2018", 2018, "tropicalblend2018.jpg", "Aromas a frutas tropicales", 3525.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("NUEVO Alba Toscana 2017", 2017, "albatoscana2017.jpg", "NUEVAS notas de manzana y pera", 4025.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Barolo Classico 2019", 2019, "baroloclassico2019.jpg", "Estructurado con final largo", 5525.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Tempranillo Reserva 2016", 2016, "tempranilloreserva2016.jpg", "NUEVAS notas de cereza y especias", 6025.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Rosé Blush 2020", 2020, "roseblush2020.jpg", "Aromas a durazno y melón", 4525.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Gran Reserva 2015", 2015, "granreserva2015.jpg", "Especiado con final persistente", 7025.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Zinfandel 2018", 2018, "zinfandel2018.jpg", "NUEVAS notas de frutos rojos y especias", 2550.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Rioja Alta 2017", 2017, "riojaalta2017.jpg", "Aromas a ciruela y roble", 3025.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[13]),
    Vino("NUEVO Carmenere 2019", 2019, "carmenere2019.jpg", "Cuerpo robusto y taninos suaves", 4525.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[13]),
    Vino("Amarone Classico 2016", 2016, "amaroneclassico2016.jpg", "NUEVAS notas de vainilla y chocolate", 5025.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[13]),
    Vino("Pinot Grigio 2020", 2020, "pinotgrigio2020.jpg", "Aromas florales y cítricos", 3525.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[13]),
    # ALTERNATIVA a3: <sistema externo de bodega no da respuesta>
    Vino("Old Vine Zinfandel 2015", 2015, "oldvinezinfandel2015.jpg", "Especiado con final largo", 6025.50, "2024-05-26", [varietales_mock[1]], [], bodegas_mock[13]),
    Vino("Cabernet Franc 2018", 2018, "cabernetfranc2018.jpg", "NUEVAS notas de frutas maduras", 4025.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[13]),
    Vino("NUEVO Petite Sirah 2017", 2017, "petitesirah2017.jpg", "NUEVAS notas de mora y regaliz", 5525.50, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[13])
]