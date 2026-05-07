class Alumno:
    def __init__(self, alumno_id, codigo, nombre, carrera_id):
        self.alumno_id = alumno_id
        self.codigo = codigo
        self.nombre = nombre
        self.carrera_id = carrera_id

    def __str__(self):
        return f"{self.codigo} - {self.nombre} (CarreraID: {self.carrera_id})"
