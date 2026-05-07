class Usuario:
    def __init__(self, usuario_id, usuario, contraseña, rol_id):
        self.usuario_id = usuario_id
        self.usuario = usuario
        self.contraseña = contraseña
        self.rol_id = rol_id

    def __str__(self):
        return f"{self.usuario} (RolID: {self.rol_id})"
