class Enofilo:
    def __init__(self, nombre, apellido, imagen_perfil, usuario, seguido, vino):
        self.nombre = nombre
        self.apellido = apellido
        self.imagen_perfil = imagen_perfil
        self.usuario = usuario
        self.seguido = seguido
        self.vino_favorito = vino
        
    def seguis_a_bodega(self, bodega):
        for seguido in self.seguido:
            if seguido.sos_de_bodega(bodega):
                return(self.get_nombre_usuario())
            else:
                continue

    def get_nombre_usuario(self):
        return(self.usuario.get_nombre())