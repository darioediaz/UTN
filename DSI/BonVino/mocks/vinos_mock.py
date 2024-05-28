from clases.vinos import Vino
from clases.maridaje import Maridaje
from clases.varietal import Varietal
from clases.tipo_uva import TipoUva
from mocks.bodegas_mock import bodegas_mock

# Crear instancias de TipoUva
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

# Crear instancias de Varietal
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

# Crear instancias de Maridaje
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

vinos_mock = [
    Vino("Vino A1", 2018, "imagenA1.jpg", "Notas de frutos rojos y especias", 2550.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Vino B1", 2017, "imagenB1.jpg", "Aromas a ciruela y roble", 3000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Vino C1", 2019, "imagenC1.jpg", "Cuerpo robusto y taninos suaves", 4500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Vino D1", 2016, "imagenD1.jpg", "Notas de vainilla y chocolate", 5000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Vino E1", 2020, "imagenE1.jpg", "Aromas florales y cítricos", 3500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Vino F1", 2015, "imagenF1.jpg", "Especiado con final largo", 6000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Vino G1", 2018, "imagenG1.jpg", "Notas de frutas maduras", 4000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[2]),
    Vino("Vino H1", 2017, "imagenH1.jpg", "Notas de mora y regaliz", 5500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Vino I1", 2019, "imagenI1.jpg", "Estructurado con final persistente", 6500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Vino J1", 2016, "imagenJ1.jpg", "Notas a cacao y tabaco", 7000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Vino K1", 2020, "imagenK1.jpg", "Notas cítricas y minerales", 4500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Vino L1", 2015, "imagenL1.jpg", "Especiado con final persistente", 7500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Vino M1", 2018, "imagenM1.jpg", "Aromas a frutas tropicales", 3500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[7]),
    Vino("Vino N1", 2017, "imagenN1.jpg", "Notas de manzana y pera", 4000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Vino O1", 2019, "imagenO1.jpg", "Estructurado con final largo", 5500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Vino P1", 2016, "imagenP1.jpg", "Notas de cereza y especias", 6000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Vino Q1", 2020, "imagenQ1.jpg", "Aromas a durazno y melón", 4500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Vino R1", 2015, "imagenR1.jpg", "Especiado con final persistente", 7000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Vino S1", 2018, "imagenS1.jpg", "Notas de frutos rojos y especias", 2550.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[11]),
    Vino("Vino T1", 2017, "imagenT1.jpg", "Aromas a ciruela y roble", 3000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[13]),
    Vino("Vino U1", 2019, "imagenU1.jpg", "Cuerpo robusto y taninos suaves", 4500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[13]),
    Vino("Vino V1", 2016, "imagenV1.jpg", "Notas de vainilla y chocolate", 5000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[13]),
    Vino("Vino W1", 2020, "imagenW1.jpg", "Aromas florales y cítricos", 3500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[14]),
    Vino("Vino X1", 2015, "imagenX1.jpg", "Especiado con final largo", 6000.0, "2024-05-26", [varietales_mock[1]], [], bodegas_mock[14]),
    Vino("Vino Y1", 2018, "imagenY1.jpg", "Notas de frutas maduras", 4000.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[14]),
    Vino("Vino Z1", 2017, "imagenZ1.jpg", "Notas de mora y regaliz", 5500.0, "2024-05-26", [varietales_mock[1]], [maridajes_mock[0]], bodegas_mock[14])
]
