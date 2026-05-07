from database.connection import get_connection
from models.asistencia import Asistencia


class AsistenciaController:
    ### Recorrido Lineal para listar las asistencia de la BD
    def listar_asistencias(self):
        conn = get_connection()
        asistencias = []
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                " SELECT AsistenciaID, AlumnoID, CursoID, ProfesorID, Fecha, EstadoID FROM Asistencias"
            )
            rows = cursor.fetchall()
            for row in rows:
                asistencia = Asistencia(row[0], row[1], row[2], row[3], row[4], row[5])
                asistencias.append(asistencia)
            conn.close()
        return asistencias

    # PROGRAMACIÓN DINÁMICA
    # Calcular porcentaje acumulado de asistencia por alumno
    def porcentaje_asistencia(self, alumno_id):
        asistencias = self.listar_asistencias()
        total, presentes = 0, 0

        for a in asistencias:
            if a.alumno_id == alumno_id:
                total += 1
                if a.estado_id == 1:
                    presentes += 1

        if total == 0:
            return 0
        return (presentes / total) * 100

    # Ranking de alumnos por porcentaje de asistencia
    # Algoritmo: cálculo porcentajes  + ordenamiento

    def ranking_asistencia_alumnos(self):
        asistencias = self.listar_asistencias()
        alumnos = set([a.alumno_id for a in asistencias])
        ranking = []

        for alumno_id in alumnos:
            porcentaje = self.porcentaje_asistencia(alumno_id)
            ranking.append((alumno_id, porcentaje))

        return sorted(ranking, key=lambda x: x[1], reverse=True)

    # Contar estados de asistencia por curso
    # Algoritmo: clasificación y conteo

    def conteo_por_curso(self, curso_id):
        asistencias = self.listar_asistencias()
        conteo = {"Presente": 0, "Ausente": 0, "Tardanza": 0}

        for a in asistencias:
            if a.curso_id == curso_id:
                if a.estado_id == 1:
                    conteo["Presente"] += 1
                elif a.estado_id == 2:
                    conteo["Ausente"] += 1
                elif a.estado_id == 3:
                    conteo["Tardanza"] += 1
        return conteo

    # Ranking de alumnos con más inasistencias por curso
    # Algoritmo: recorrido secuencial  + ordenamiento

    def ranking_insistencias(self, curso_id):
        asistencias = self.listar_asistencias()
        conteo = {}

        for a in asistencias:
            if a.curso_id == curso_id:
                if a.alumno_id not in conteo:
                    conteo[a.alumno_id] = 0
                if a.estado_is == 2:
                    conteo[a.alumno_id] += 1
        return sorted(conteo.items(), key=lambda x: x[1], reverse=True)

    # Deshacer la última asistencia registrada
    # Algoritmo: retroceso - BACKTRACKING

    def deshacer_asistencia(self, asistencia_id):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM Asistencias WHERE AsistenciaID = ?", asistencia_id
            )
            conn.commit()
            conn.close()
            return True
        return False

    # REPORTE GENERAL POR CURSO
    # Ranking de cursos con mayor cantidad de asistencias
    # Algoritmo: conteo categorico + ordenamiento
    def ranking_cursos_por_asistencia(self):
        asistencias = self.listar_asistencias()
        reporte = {}

        for a in asistencias:
            if a.curso_id not in reporte:
                reporte[a.curso_id] = 0
            if a.estado_id == 1:
                reporte[a.curso_id] += 1
        return sorted(reporte.items(), key=lambda x: x[1], reverse=True)
