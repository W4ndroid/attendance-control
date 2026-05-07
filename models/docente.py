class Docente:
    def __init__(self, docente_id, nombre, especialidad):
        self.docente_id = docente_id
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"
