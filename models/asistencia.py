class Asistencia:
    def __init__(
        self, asistencia_id, alumno_id, curso_id, profesor_id, fecha, estado_id
    ):
        self.asistencia_id = asistencia_id
        self.alumno_id = alumno_id
        self.curso_id = curso_id
        self.profesor_id = profesor_id
        self.fecha = fecha
        self.estado_id = estado_id

    def __str__(self):
        return f"Asistencia {self.asistencia_id}: Alumno {self.alumno_id}, Curso {self.curso_id}, Profesor {self.profesor_id}, Fecha {self.fecha}, Estado {self.estado_id}"
