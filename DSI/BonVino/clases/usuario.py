class Usuario:
    def __init__(self, nombre, contraseña, premium):
        self.nombre = nombre
        self.contraseña = contraseña
        self.premium = premium

    def get_nombre(self):
        return self.nombre
