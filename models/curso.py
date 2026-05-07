class Curso:
    def __init__(self, curso_id, nombre, seccion, docente_id):
        self.curso_id = curso_id
        self.nombre = nombre
        self.seccion = seccion
        self.docente_id = docente_id

    def __str__(self):
        return f"{self.nombre} - Sección {self.seccion} (DocenteID: {self.docente_id})"
