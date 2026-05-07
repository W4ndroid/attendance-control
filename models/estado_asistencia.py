class EstadoAsistencia:
    def __init__(self, estado_id, nombre):
        self.estado_id = estado_id
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}"
