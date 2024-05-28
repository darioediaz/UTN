from clases.vinos import Vino
from clases.maridaje import Maridaje
from clases.varietal import Varietal
from clases.tipo_uva import TipoUva
from mocks.bodegas_mock import bodegas_mock

# mock de Tipos de Uvas
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

# mock de Varietales
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
    Varietal("Varietal de Sangiovese, 100% Sangiovese", 100, tipos_uva_mock[14]),
    Varietal("Varietal de Barbera, 100% Barbera", 100, tipos_uva_mock[15]),
    Varietal("Varietal de Moscato, 100% Moscato", 100, tipos_uva_mock[16]),
    Varietal("Varietal de Nebbiolo, 100% Nebbiolo", 100, tipos_uva_mock[17]),
    Varietal("Varietal de Grenache, 100% Grenache", 100, tipos_uva_mock[18]),
    Varietal("Varietal de Cabernet Franc, 100% Cabernet Franc", 100, tipos_uva_mock[19])
]

# mock de Maridaje
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
# mock de vinos a actualizar o crear
vinos_a_actualizar_mock = [   
    #Vinos con algunas actualizaciones en su precio, no de cata e imagen 
    Vino("Gran Reserva 2018", 2018, "granreserva2018_new.jpg", "Notas de frutos rojos, especias y un toque de roble", 2750.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Malbec Premium 2017", 2017, "malbecpremium2017_new.jpg", "Aromas intensos a ciruela y roble con toques de vainilla", 3200.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Cabernet Sauvignon 2019", 2019, "cabernetsauvignon2019.jpg", "Cuerpo robusto y taninos suaves_new", 4500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Reserva Especial 2016", 2016, "reservaespecial2016.jpg", "Notas de vainilla y chocolate", 5000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Chardonnay 2020", 2020, "chardonnay2020_new.jpg", "Aromas florales, cítricos y un toque de miel", 3700.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Merlot Selección 2015", 2015, "merlotseleccion2015.jpg", "Especiado con final largo", 6000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Syrah 2018", 2018, "syrah2018.jpg", "Notas de frutas maduras", 4000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Shiraz Barossa 2017", 2017, "shirazbarossa2017.jpg", "Notas de mora y regaliz", 5500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Pinot Noir 2019", 2019, "pinotnoir2019_new.jpg", "Estructurado con final persistente y un toque de frambuesa", 6800.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Gran Shiraz 2016", 2016, "granshiraz2016.jpg", "Notas a cacao y tabaco", 7000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Sauvignon Blanc 2020", 2020, "sauvignonblanc2020.jpg", "Notas cítricas y minerales", 4500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Vintage Reserve 2015", 2015, "vintagereserve2015.jpg", "Especiado con final persistente_new", 7500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Tropical Blend 2018", 2018, "tropicalblend2018.jpg", "Aromas a frutas tropicales", 3500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Alba Toscana 2017", 2017, "albatoscana2017_new.jpg", "Notas de manzana, pera y un toque de miel", 4200.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Barolo Classico 2019", 2019, "baroloclassico2019.jpg", "Estructurado con final largo", 5500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Tempranillo Reserva 2016", 2016, "tempranilloreserva2016.jpg", "Notas de cereza y especias", 6000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Rosé Blush 2020", 2020, "roseblush2020.jpg", "Aromas a durazno y melón", 4500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Gran Reserva 2015", 2015, "granreserva2015.jpg", "Especiado con final persistente_new", 7000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Zinfandel 2018", 2018, "zinfandel2018.jpg", "Notas de frutos rojos y especias", 2550.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Rioja Alta 2017", 2017, "riojaalta2017_new.jpg", "Aromas a ciruela, roble y un toque de cuero", 3200.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[13]),
    Vino("Carmenere 2019", 2019, "carmenere2019.jpg", "Cuerpo robusto y taninos suaves", 4500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[13]),
    Vino("Amarone Classico 2016", 2016, "amaroneclassico2016.jpg", "Notas de vainilla y chocolate_new", 5000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[13]),
    Vino("Pinot Grigio 2020", 2020, "pinotgrigio2020_new.jpg", "Aromas florales, cítricos y un toque de pera", 3700.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[14]),
    Vino("Old Vine Zinfandel 2015", 2015, "oldvinezinfandel2015.jpg", "Especiado con final largo", 6000.0, "2024-05-26", [varietales_mock[1]], [], bodegas_mock[14]),
    Vino("Cabernet Franc 2018", 2018, "cabernetfranc2018.jpg", "Notas de frutas maduras_new", 4000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[14]),
    Vino("Petite Sirah 2017", 2017, "petitesirah2017.jpg", "Notas de mora y regaliz", 5500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[14]),
    # Vinos que sedeben crear
    Vino("Malbec Reserva 2015", 2015, "malbecreserva2015.jpg", "Intenso y elegante", 4800.0, "2024-05-28", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Chardonnay Grand Cru 2019", 2019, "chardonnaygrandcru2019.jpg", "Notas de manzana y toques de roble", 6200.0, "2024-05-28", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Merlot Reserva 2017", 2017, "merlotreserva2017.jpg", "Equilibrado con taninos suaves", 5300.0, "2024-05-28", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Syrah Gran Reserva 2016", 2016, "syrahgranreserva2016.jpg", "Notas de frutos negros y especias", 6700.0, "2024-05-28", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Sauvignon Blanc 2021", 2021, "sauvignonblanc2021.jpg", "Aromas a hierbas y cítricos", 4200.0, "2024-05-28", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Cabernet Sauvignon Reserva 2018", 2018, "cabernetsauvignonreserva2018.jpg", "Estructurado con final persistente", 5800.0, "2024-05-28", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Pinot Noir 2020", 2020, "pinotnoir2020.jpg", "Notas de cereza y violetas", 4900.0, "2024-05-28", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[13]),
    Vino("Riesling Late Harvest 2019", 2019, "rieslinglateharvest2019.jpg", "Dulce y refrescante", 4500.0, "2024-05-28", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[13]),
    Vino("Gewürztraminer 2020", 2020, "gewurztraminer2020.jpg", "Aromas intensos a rosas y lichis", 5100.0, "2024-05-28", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[14]),
    Vino("Cava Brut Nature", 2000, "cavabrutnature.jpg", "Burbujas finas y frescas", 3800.0, "2024-05-28", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[14])
]



