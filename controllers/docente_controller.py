from database.connection import get_connection
from models.docente import Docente


class DocenteController:

    # Listar docentes desde la BD
    # Algoritmo: recorrido lineal

    def listar_docentes(self):
        conn = get_connection()
        docentes = []
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT DocenteID, Nombre, Especialidad FROM Docentes")
            rows = cursor.fetchall()
            for row in rows:
                docente = Docente(row[0], row[1], row[2])
                docentes.append(docente)
            conn.close()
        return docentes

    # CRUD BÁSICO
    # Agregar docente
    def agregar_docente(self, nombre, especialidad):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Docentes (Nombre, Especialidad) VALUES (?, ?)",
                (nombre, especialidad),
            )
            conn.commit()
            conn.close()
            return True
        return False

    # CRUD BÁSICO
    # Actualizar docente

    def actualizar_docente(self, docente_id, nuevo_nombre, nueva_especialidad):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Docentes SET Nombre = ?, Especialidad = ? WHERE DocenteID = ?",
                (nuevo_nombre, nueva_especialidad, docente_id),
            )
            conn.commit()
            conn.close()
            return True
        return False

    # CRUD BÁSICO
    # Eliminar docente

    def eliminar_docente(self, docente_id):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Docentes WHERE DocenteID = ?", (docente_id,))
            conn.commit()
            conn.close()
            return True
        return False

    # Buscar docente por nombre
    # Algoritmo: búsqueda secuencial
    def buscar_docente_lineal(self, nombre):
        docentes = self.listar_docentes()
        for docente in docentes:
            if docente.nombre == nombre:
                return docente
        return None

    # GRAFOS
    # Relacionar docentes con cursos
    # Algoritmo: representación con lista de adyacencia
    def relaciones_docente_curso(self):
        # Abrimos conexión
        conn = get_connection()
        # Diccionario para representar grafo
        grafo = {}
        if conn:
            cursor = conn.cursor()  # Creamos cursor
            cursor.execute(
                "SELECT d.DocenteID, d.Nombre, c.CursoID, c.Nombre FROM Docentes d INNER JOIN Cursos c ON d.DocenteID = c.DocenteID "
            )
            rows = cursor.fetchall()  # Obtenemos todas las filas
            for row in rows:  # Recorremos filas
                docente_id, docente_nombre, curso_id, curso_nombre = row
                if docente_nombre not in grafo:  # Si el docente no está en el grafo
                    grafo[docente_nombre] = []  # Inicializamos lista de cursos
                grafo[docente_nombre].append(
                    curso_nombre
                )  # Agregamos curso a lista de adyacencia
            conn.close()  # Cerramos conexión
        return grafo  # Devolvemos grafo docente-curso
