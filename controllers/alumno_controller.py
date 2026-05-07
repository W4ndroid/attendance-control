from database.connection import get_connection
from models.alumno import Alumno


class AlumnoController:

    ### listamos los Alumno desde la BD
    def listar_alumno(self):
        conn = get_connection()
        alumnos = []
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT AlumnoID, Codigo, Nombre, CarreraID FROM Alumnos")
            rows = cursor.fetchall()
            for row in rows:
                alumno = Alumno(row[0], row[1], row[2], row[3])
                alumnos.append(alumno)
            conn.close()
        return alumnos

    ### Usamos BUSQUEDA LINEAL: para hacer una busqueda por nombre
    def buscar_por_nombre_lineal(self, nombre):
        alumnos = self.listar_alumno()
        for alumno in alumnos:
            if alumno.nombre == nombre:
                return alumno
        return None

    ### usaremos BUSQUEDA BINARIA para ordernar a los alumnos y buscar por codigo
    def buscar_por_codigo_binaria(self, codigo):
        alumnos = sorted(self.listar_alumno(), key=lambda a: a.codigo)
        izquierda, derecha = 0, len(alumnos) - 1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if alumnos[medio].codigo == codigo:
                return alumnos[medio]
            elif alumnos[medio].codigo < codigo:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return None
