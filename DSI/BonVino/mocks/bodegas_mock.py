from clases.bodegas import Bodega

 # mock de bodegas
bodegas_mock = [
    Bodega("Bodega El Centenario", "La Rioja, Argentina", "Bodega con tradición centenaria.", "Fundada en 1890, ha pasado por varias generaciones familiares.", False, 12, "2024-01-01"),
    Bodega("Bodega Los Andes", "Mendoza, Argentina", "Famosa por sus Malbec.", "Establecida en 1920, conocida por la calidad de sus vinos tintos.", False, 6, "2024-02-01"),
    Bodega("Bodega Valle Verde", "Napa Valley, EE.UU.", "Innovadora en métodos de vinificación.", "Desde 1970, ha introducido técnicas modernas en la producción de vino.", True, 3, "2024-03-01"),
    Bodega("Bodega Château Lumière", "Bordeaux, Francia", "Especialista en vinos tintos de mezcla.", "Parte de una región histórica, famosa desde el siglo XIX.", False, 6, "2024-04-01"),
    Bodega("Bodega Montepulciano", "Toscana, Italia", "Productora de Chianti clásico.", "Sus viñedos han sido cultivados desde la época romana.", False, 12, "2024-05-01"),
    Bodega("Bodega Douro Vinho", "Douro, Portugal", "Reconocida por sus vinos de Oporto.", "En operación desde el siglo XVIII.", False, 9, "2024-06-01"),
    Bodega("Bodega La Sostenible", "Colchagua, Chile", "Bodega familiar con enfoque en la sostenibilidad.", "Inició en 1985, ha ganado varios premios internacionales.", False, 3, "2024-07-01"),
    Bodega("Bodega Shiraz Heritage", "Barossa Valley, Australia", "Conocida por su Shiraz.", "Fundada en 1847, una de las más antiguas de Australia.", True, 12, "2024-08-01"),
    Bodega("Bodega Stellen Excellence", "Stellenbosch, Sudáfrica", "Bodega boutique con producción limitada.", "Desde 1995, ha sido reconocida por su atención al detalle.", False, 6, "2024-09-01"),
    Bodega("Bodega Riesling Tradición", "Mosel, Alemania", "Famosa por sus vinos Riesling.", "Ha estado en la familia por 8 generaciones.", False, 9, "2024-10-01"),
    Bodega("Bodega Priorat Premier", "Priorat, España", "Bodega emergente con vinos premiados.", "Fundada en 2000, se ha destacado en concursos internacionales.", False, 12, "2024-11-01"),
    Bodega("Bodega Barolo Classico", "Piedmont, Italia", "Especialista en Barolo.", "Sus viñedos datan del siglo XIX.", True, 3, "2024-12-01"),
    Bodega("Bodega Hunter Valley Select", "Hunter Valley, Australia", "Conocida por su Semillon.", "En operación desde 1850.", False, 6, "2024-01-15"),
    Bodega("Bodega Champagne Royale", "Champagne, Francia", "Productora de Champagne tradicional.", "Fundada en 1760, con una historia rica en tradición.", True, 12, "2024-02-15"),
    Bodega("Bodega Terroir Innovación", "Valle de Uco, Argentina", "Bodega moderna con enfoque en terroir.", "Desde 2005, ha innovado en la producción de vinos de alta calidad.", True, 9, "2024-03-15"),
]

# alternativa A1: <bodegas sin acualizar>
#  # mock de bodegas para prueba de sin actualizacion
# bodegas_mock = [
#     Bodega("Bodega El Centenario", "La Rioja, Argentina", "Bodega con tradición centenaria.", "Fundada en 1890, ha pasado por varias generaciones familiares.", False, 12, "2024-01-01"),
#     Bodega("Bodega Los Andes", "Mendoza, Argentina", "Famosa por sus Malbec.", "Establecida en 1920, conocida por la calidad de sus vinos tintos.", False, 6, "2024-02-01"),
#     Bodega("Bodega Valle Verde", "Napa Valley, EE.UU.", "Innovadora en métodos de vinificación.", "Desde 1970, ha introducido técnicas modernas en la producción de vino.", False, 3, "2024-03-01"),
#     Bodega("Bodega Château Lumière", "Bordeaux, Francia", "Especialista en vinos tintos de mezcla.", "Parte de una región histórica, famosa desde el siglo XIX.", False, 6, "2024-04-01"),
#     Bodega("Bodega Montepulciano", "Toscana, Italia", "Productora de Chianti clásico.", "Sus viñedos han sido cultivados desde la época romana.", False, 12, "2024-05-01"),
#     Bodega("Bodega Douro Vinho", "Douro, Portugal", "Reconocida por sus vinos de Oporto.", "En operación desde el siglo XVIII.", False, 9, "2024-06-01"),
#     Bodega("Bodega La Sostenible", "Colchagua, Chile", "Bodega familiar con enfoque en la sostenibilidad.", "Inició en 1985, ha ganado varios premios internacionales.", False, 3, "2024-07-01"),
#     Bodega("Bodega Shiraz Heritage", "Barossa Valley, Australia", "Conocida por su Shiraz.", "Fundada en 1847, una de las más antiguas de Australia.", False, 12, "2024-08-01"),
#     Bodega("Bodega Stellen Excellence", "Stellenbosch, Sudáfrica", "Bodega boutique con producción limitada.", "Desde 1995, ha sido reconocida por su atención al detalle.", False, 6, "2024-09-01"),
#     Bodega("Bodega Riesling Tradición", "Mosel, Alemania", "Famosa por sus vinos Riesling.", "Ha estado en la familia por 8 generaciones.", False, 9, "2024-10-01"),
#     Bodega("Bodega Priorat Premier", "Priorat, España", "Bodega emergente con vinos premiados.", "Fundada en 2000, se ha destacado en concursos internacionales.", False, 12, "2024-11-01"),
#     Bodega("Bodega Barolo Classico", "Piedmont, Italia", "Especialista en Barolo.", "Sus viñedos datan del siglo XIX.", False, 3, "2024-12-01"),
#     Bodega("Bodega Hunter Valley Select", "Hunter Valley, Australia", "Conocida por su Semillon.", "En operación desde 1850.", False, 6, "2024-01-15"),
#     Bodega("Bodega Champagne Royale", "Champagne, Francia", "Productora de Champagne tradicional.", "Fundada en 1760, con una historia rica en tradición.", False, 12, "2024-02-15"),
#     Bodega("Bodega Terroir Innovación", "Valle de Uco, Argentina", "Bodega moderna con enfoque en terroir.", "Desde 2005, ha innovado en la producción de vinos de alta calidad.", False, 9, "2024-03-15"),
# ]