class Rol:
    def __init__(self, rol_id, nombre):
        self.rol_id = rol_id
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}"
