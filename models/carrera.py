class Carrera:
    def __init__(self, carrera_id, nombre):
        self.carrera_id = carrera_id
        self.nombre = nombre

    def __str__(self):
        return f"{self.carrera_id} - {self.nombre}"
