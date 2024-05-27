from clases.vinos import Vino
from clases.maridaje import Maridaje
from clases.varietal import Varietal
from clases.tipo_uva import TipoUva
from mocks.bodegas_mock import bodegas_mock

# Crear instancias de TipoUva
tipo_uva_malbec = TipoUva("Malbec", "Uva tinta de origen francés, típica de Argentina.")
tipo_uva_cabernet_sauvignon = TipoUva("Cabernet Sauvignon", "Una de las variedades de uva tinta más conocidas.")
tipo_uva_merlot = TipoUva("Merlot", "Uva tinta, caracterizada por su suavidad y cuerpo.")
tipo_uva_syrah = TipoUva("Syrah", "Uva tinta que produce vinos especiados y con cuerpo.")
tipo_uva_chardonnay = TipoUva("Chardonnay", "Uva blanca, la más cultivada del mundo.")
tipo_uva_tempranillo = TipoUva("Tempranillo", "Uva tinta, autóctona de España.")
tipo_uva_garnacha = TipoUva("Garnacha", "Uva tinta muy versátil y cultivada en varias regiones.")
tipo_uva_pinot_noir = TipoUva("Pinot Noir", "Uva tinta de Borgoña, Francia, conocida por su dificultad de cultivo.")
tipo_uva_zinfandel = TipoUva("Zinfandel", "Uva tinta, muy popular en California.")
tipo_uva_petit_verdot = TipoUva("Petit Verdot", "Uva tinta, usada principalmente en mezclas de Bordeaux.")
tipo_uva_sauvignon_blanc = TipoUva("Sauvignon Blanc", "Uva blanca, conocida por sus aromas herbáceos.")
tipo_uva_carmenere = TipoUva("Carmenere", "Uva tinta, originaria de Bordeaux y muy cultivada en Chile.")
tipo_uva_viognier = TipoUva("Viognier", "Uva blanca, con aromas florales y frutales.")
tipo_uva_albarino = TipoUva("Albariño", "Uva blanca, típica de la región de Galicia en España.")
tipo_uva_sangiovese = TipoUva("Sangiovese", "Uva tinta, principal en la producción de Chianti en Italia.")
tipo_uva_barbera = TipoUva("Barbera", "Uva tinta, muy cultivada en el Piamonte italiano.")
tipo_uva_moscato = TipoUva("Moscato", "Uva blanca, utilizada para vinos dulces y espumantes.")
tipo_uva_nebbiolo = TipoUva("Nebbiolo", "Uva tinta, conocida por sus taninos y acidez en el Piamonte italiano.")
tipo_uva_grenache = TipoUva("Grenache", "Uva tinta, muy cultivada en España y Francia.")
tipo_uva_cabernet_franc = TipoUva("Cabernet Franc", "Uva tinta, utilizada en mezclas de Bordeaux y varietales en el Valle del Loira.")

# Crear instancias de Varietal
varietal_malbec = Varietal("Varietal de Malbec, 100% Malbec", 100, tipo_uva_malbec)
varietal_cabernet_sauvignon = Varietal("Varietal de Cabernet Sauvignon, 100% Cabernet Sauvignon", 100, tipo_uva_cabernet_sauvignon)
varietal_merlot = Varietal("Varietal de Merlot, 100% Merlot", 100, tipo_uva_merlot)
varietal_syrah = Varietal("Varietal de Syrah, 100% Syrah", 100, tipo_uva_syrah)
varietal_chardonnay = Varietal("Varietal de Chardonnay, 100% Chardonnay", 100, tipo_uva_chardonnay)
varietal_tempranillo = Varietal("Varietal de Tempranillo, 100% Tempranillo", 100, tipo_uva_tempranillo)
varietal_garnacha = Varietal("Varietal de Garnacha, 100% Garnacha", 100, tipo_uva_garnacha)
varietal_pinot_noir = Varietal("Varietal de Pinot Noir, 100% Pinot Noir", 100, tipo_uva_pinot_noir)
varietal_zinfandel = Varietal("Varietal de Zinfandel, 100% Zinfandel", 100, tipo_uva_zinfandel)
varietal_petit_verdot = Varietal("Varietal de Petit Verdot, 100% Petit Verdot", 100, tipo_uva_petit_verdot)
varietal_sauvignon_blanc = Varietal("Varietal de Sauvignon Blanc, 100% Sauvignon Blanc", 100, tipo_uva_sauvignon_blanc)
varietal_carmenere = Varietal("Varietal de Carmenere, 100% Carmenere", 100, tipo_uva_carmenere)
varietal_viognier = Varietal("Varietal de Viognier, 100% Viognier", 100, tipo_uva_viognier)
varietal_albarino = Varietal("Varietal de Albariño, 100% Albariño", 100, tipo_uva_albarino)
varietal_sangiovese = Varietal("Varietal de Sangiovese, 100% Sangiovese", 100, tipo_uva_sangiovese)
varietal_barbera = Varietal("Varietal de Barbera, 100% Barbera", 100, tipo_uva_barbera)
varietal_moscato = Varietal("Varietal de Moscato, 100% Moscato", 100, tipo_uva_moscato)
varietal_nebbiolo = Varietal("Varietal de Nebbiolo, 100% Nebbiolo", 100, tipo_uva_nebbiolo)
varietal_grenache = Varietal("Varietal de Grenache, 100% Grenache", 100, tipo_uva_grenache)
varietal_cabernet_franc = Varietal("Varietal de Cabernet Franc, 100% Cabernet Franc", 100, tipo_uva_cabernet_franc)

# Crear instancias de Maridaje
maridaje_carnes_rojas = Maridaje("Carnes Rojas", "Ideal para acompañar con carnes rojas a la parrilla o asadas.")
maridaje_quesos_curados = Maridaje("Quesos Curados", "Perfecto con una selección de quesos curados.")
maridaje_pasta = Maridaje("Pasta", "Acompaña bien con pastas con salsa de tomate.")
maridaje_cordero = Maridaje("Cordero", "Excelente con cordero asado o guisado.")
maridaje_pescado = Maridaje("Pescado", "Ideal con pescados a la parrilla o al horno.")
maridaje_tapas = Maridaje("Tapas", "Marida bien con una variedad de tapas.")
maridaje_pollo = Maridaje("Pollo", "Acompaña bien con pollo asado o a la parrilla.")
maridaje_setas = Maridaje("Setas", "Ideal con platos de setas y hongos.")
maridaje_bbq = Maridaje("BBQ", "Perfecto para carnes a la barbacoa.")
maridaje_bistec = Maridaje("Bistec", "Excelente con un buen bistec a la parrilla.")
maridaje_ensaladas = Maridaje("Ensaladas", "Marida bien con ensaladas verdes y frescas.")
maridaje_embutidos = Maridaje("Embutidos", "Acompaña bien con una selección de embutidos.")
maridaje_quesos_suaves = Maridaje("Quesos Suaves", "Perfecto con quesos suaves y cremosos.")
maridaje_mariscos = Maridaje("Mariscos", "Ideal con mariscos frescos y a la parrilla.")
maridaje_pizza = Maridaje("Pizza", "Marida bien con pizza y platos italianos.")
maridaje_guisos = Maridaje("Guisos", "Acompaña bien con guisos de carne y legumbres.")
maridaje_postres = Maridaje("Postres", "Perfecto para acompañar con postres dulces.")
maridaje_caza = Maridaje("Caza", "Ideal con carnes de caza.")
maridaje_emputidos = Maridaje("Embutidos", "Acompaña bien con una selección de embutidos.")

vinos_a_actualizar_mock = [
    Vino("Vino A1", 2018, "imagenA1.jpg", "Notas de frutos rojos y especias", 2525.0, "2024-05-26", varietal_malbec, [maridaje_carnes_rojas], bodegas_mock[2]),
    Vino("Vino B1", 2017, "imagenB1.jpg", "Aromas a ciruela y roble", 3025.0, "2024-05-26", varietal_cabernet_sauvignon, [maridaje_quesos_curados], bodegas_mock[2]),
    Vino("Vino C1", 2019, "imagenC1.jpg", "Cuerpo robusto y taninos suaves", 4525.0, "2024-05-26", varietal_merlot, [maridaje_pasta], bodegas_mock[2]),
    Vino("Vino D1", 2016, "imagenD1.jpg", "Notas de vainilla y chocolate", 5025.0, "2024-05-26", varietal_syrah, [maridaje_cordero], bodegas_mock[2]),
    Vino("Vino A12", 2020, "imagenE1.jpg", "Aromas florales y cítricos", 3525.0, "2024-05-26", varietal_chardonnay, [maridaje_pescado, maridaje_bistec], bodegas_mock[2]),
    Vino("Vino F1", 2015, "imagenF1.jpg", "Especiado con final largo", 6025.0, "2024-05-26", varietal_tempranillo, [maridaje_tapas, maridaje_cordero], bodegas_mock[2]),
    Vino("Vino G1", 2018, "imagenG1.jpg", "Notas de frutas maduras", 4025.0, "2024-05-26", varietal_garnacha, [maridaje_pollo], bodegas_mock[2]),
    Vino("Vino H1", 2017, "imagenH1.jpg", "Notas de mora y regaliz", 5525.0, "2024-05-26", varietal_pinot_noir, [maridaje_setas], bodegas_mock[7]),
    Vino("Vino I1", 2019, "imagenI1.jpg", "Estructurado con final persistente", 6525.0, "2024-05-26", varietal_zinfandel, [maridaje_bbq], bodegas_mock[7]),
    Vino("Vino J1", 2016, "imagenJ1.jpg", "Notas a cacao y tabaco", 7025.0, "2024-05-26", varietal_petit_verdot, [maridaje_bistec], bodegas_mock[7]),
    Vino("Vino K12", 2020, "imagenK1.jpg", "Notas cítricas y minerales", 4525.0, "2024-05-26", varietal_sauvignon_blanc, [maridaje_ensaladas], bodegas_mock[7]),
    Vino("Vino L1", 2015, "imagenL1.jpg", "Especiado con final persistente", 7525.0, "2024-05-26", varietal_carmenere, [maridaje_embutidos, maridaje_pescado], bodegas_mock[7]),
    Vino("Vino M1", 2018, "imagenM1.jpg", "Aromas a frutas tropicales", 3525.0, "2024-05-26", varietal_viognier, [maridaje_quesos_suaves], bodegas_mock[7]),
    Vino("Vino N1", 2017, "imagenN1.jpg", "Notas de manzana y pera", 4025.0, "2024-05-26", varietal_albarino, [maridaje_mariscos], bodegas_mock[11]),
    Vino("Vino O1", 2019, "imagenO1.jpg", "Estructurado con final largo", 5525.0, "2024-05-26", varietal_sangiovese, [maridaje_pizza], bodegas_mock[11]),
    Vino("Vino P12", 2016, "imagenP1.jpg", "Notas de cereza y especias", 6025.0, "2024-05-26", varietal_barbera, [maridaje_guisos], bodegas_mock[11]),
    Vino("Vino Q1", 2020, "imagenQ1.jpg", "Aromas a durazno y melón", 4525.0, "2024-05-26", varietal_moscato, [maridaje_postres], bodegas_mock[11]),
    Vino("Vino R1", 2015, "imagenR1.jpg", "Especiado con final persistente", 7025.0, "2024-05-26", varietal_nebbiolo, [maridaje_caza], bodegas_mock[11]),
    Vino("Vino S1", 2018, "imagenS1.jpg", "Notas de frutos rojos y especias", 2525.0, "2024-05-26", varietal_grenache, [maridaje_embutidos], bodegas_mock[11]),
    Vino("Vino T1", 2017, "imagenT1.jpg", "Aromas a ciruela y roble", 3025.0, "2024-05-26", varietal_malbec, [maridaje_quesos_curados], bodegas_mock[13]),
    Vino("Vino U12", 2019, "imagenU1.jpg", "Cuerpo robusto y taninos suaves", 4525.0, "2024-05-26", varietal_cabernet_franc, [maridaje_carnes_rojas], bodegas_mock[13]),
    Vino("Vino V1", 2016, "imagenV1.jpg", "Notas de vainilla y chocolate", 5025.0, "2024-05-26", varietal_syrah, [maridaje_cordero], bodegas_mock[13]),
    Vino("Vino W1", 2020, "imagenW1.jpg", "Aromas florales y cítricos", 3525.0, "2024-05-26", varietal_chardonnay, [maridaje_pescado, maridaje_pasta], bodegas_mock[14]),
    Vino("Vino X1", 2015, "imagenX1.jpg", "Especiado con final largo", 6025.0, "2024-05-26", varietal_tempranillo, [], bodegas_mock[14]),
    Vino("Vino Y12", 2018, "imagenY1.jpg", "Notas de frutas maduras", 4025.0, "2024-05-26", varietal_garnacha, [maridaje_pollo], bodegas_mock[14]),
    Vino("Vino Z1", 2017, "imagenZ1.jpg", "Notas de mora y regaliz", 5525.0, "2024-05-26", varietal_pinot_noir, [maridaje_setas, maridaje_embutidos, maridaje_cordero], bodegas_mock[14])
]