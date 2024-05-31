class Enofilo:
    def __init__(self, nombre, apellido, imagen_perfil, usuario, seguido, vino):
        self.nombre = nombre
        self.apellido = apellido
        self.imagen_perfil = imagen_perfil
        self.usuario = usuario
        self.seguido = seguido
        self.vino_favorito = vino
        
    # setters
    def set_nombre(self, nombre):  
        self.nombre = nombre
    
    def set_apellido(self, apellido):
        self.apellido = apellido
        
    def set_imagen_perfil(self, imagen_perfil):
        self.imagen_perfil = imagen_perfil
        
    def set_vino_favorito(self, vino):
        self.vino_favorito = vino
        
    def set_usuario(self, usuario):
        self.usuario = usuario
        
    def set_seguido(self, seguido):
        self.seguido = seguido
    
    # getters     
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_imagen_perfil(self):
        return self.imagen_perfil
    
    def get_vino_favorito(self):
        return self.vino_favorito
    
    def get_seguido(self):
        return self.seguido 
    
    def get_usuario(self):
        return self.usuario 
    
    # funcion del metodo seguis_a_bodega
    def seguis_a_bodega(self, bodega):
        for seguido in self.seguido:
            if seguido.sos_de_bodega(bodega):
                return(self.get_nombre_usuario())
            else:
                continue
    
    # funcion del metodo get_nombre
    def get_nombre_usuario(self):
        return(self.usuario.get_nombre())