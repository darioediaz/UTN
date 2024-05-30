class Usuario:
    def __init__(self, nombre, contraseña, premium):
        self.nombre = nombre
        self.contraseña = contraseña
        self.premium = premium
        
    # setters    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_contraseña(self, contraseña):
        self.contrasenya = contraseña
        
    def set_premium(self, premium):
        self.premium = premium
        
    # getters
    def get_nombre(self):
        return self.nombre
    
    def get_contraseña(self):
        return self.contraseña
    
    def get_premium(self):
        return self.premium
            
    