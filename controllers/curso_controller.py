from database.connection import get_connection
from models.curso import Curso


class CursoController:

    # RECORRIDO SECUENCIAL
    # Listar cursos desde la BD
    # Algoritmo: recorrido lineal
    def listar_cursos(self):
        conn = get_connection()
        cursos = []
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT CursoID, Nombre, Seccion, DocenteID FROM Cursos")
            rows = cursor.fetchall()
            for row in rows:
                curso = Curso(row[0], row[1], row[2], row[3])
                cursos.append(curso)
            conn.close()
        return cursos

    # CRUD BÁSICO
    # Agregar curso
    def agregar_curso(self, nombre, seccion):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Cursos (Nombre, Seccion) VALUES (?, ?)", (nombre, seccion)
            )
            conn.commit()
            conn.close()
            return True
        return False

    # CRUD BÁSICO
    # Actualizar curso
    def actualizar_curso(self, curso_id, nuevo_nombre, nueva_seccion):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Cursos SET Nombre = ?, Seccion = ? WHERE CursoID = ?",
                (nuevo_nombre, nueva_seccion, curso_id),
            )
            conn.commit()
            conn.close()
            return True
        return False

    # CRUD BÁSICO
    # Eliminar curso
    def eliminar_curso(self, curso_id):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Cursos WHERE CursoID = ?", (curso_id,))
            conn.commit()
            conn.close()
            return True
        return False

    # BÚSQUEDA BINARIA
    # Buscar curso por nombre
    # Algoritmo: búsqueda binaria

    def buscar_curso_binaria(self, nombre):
        cursos = sorted(self.listar_cursos(), key=lambda c: c.nombre)
        izquierda, derecha = 0, len(cursos) - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if cursos[medio].nombre == nombre:
                return cursos[medio]
            elif cursos[medio].nombre < nombre:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return None

    # Calcular estadísticas de cursos dividiendo en secciones
    # Algoritmo: divide y vencerás
    def estadisticas_divide_venceras(self, cursos):
        #  si la lista tiene un solo curso, devolvemos estadísticas simples
        if len(cursos) == 1:
            return {cursos[0].nombre: 1}

        # Dividimos la lista en dos mitades
        medio = len(cursos) // 2
        izquierda = cursos[:medio]
        derecha = cursos[medio:]

        # Resolvemos recursivamente cada mitad
        estadisticas_izq = self.estadisticas_divide_venceras(izquierda)
        estadisticas_der = self.estadisticas_divide_venceras(derecha)

        # Combinamos resultados (conquista)
        estadisticas = {}
        estadisticas.update(estadisticas_izq)
        estadisticas.update(estadisticas_der)

        return estadisticas
