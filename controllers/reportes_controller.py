from controllers.alumno_controller import (
    AlumnoController,
)  # Controlador que maneja CRUD y búsquedas de alumnos
from controllers.asistencia_controller import (
    AsistenciaController,
)  # Controlador que maneja cálculos de asistencia
from controllers.curso_controller import (
    CursoController,
)  # Controlador que maneja CRUD y estadísticas de cursos
from controllers.docente_controller import (
    DocenteController,
)  # Controlador que maneja CRUD y relaciones docente-curso


class ReportesController:
    """
    Controlador de reportes institucionales.
    Integra los resultados de los otros controladores aplicando algoritmos del sílabo:
    - Recorrido secuencial
    - Conteo categórico
    - Greedy (voraz)
    - Ordenamiento
    - Divide y vencerás
    - Grafos
    """

    def __init__(self):
        # Inicializamos los controladores que proveen los datos desde la base de datos
        self.alumno_ctrl = AlumnoController()
        self.asistencia_ctrl = AsistenciaController()
        self.curso_ctrl = CursoController()
        self.docente_ctrl = DocenteController()

    # ============================================================
    # REPORTE DE ASISTENCIAS POR ALUMNO
    # Algoritmo: recorrido secuencial + conteo + ordenamiento
    # Fuente: AsistenciaController (ranking_asistencia_alumnos)
    # Propósito: mostrar porcentaje de asistencia por alumno
    # ============================================================
    def reporte_asistencias_alumnos(self):
        ranking = (
            self.asistencia_ctrl.ranking_asistencia_alumnos()
        )  # Llama al método que calcula asistencia desde BD
        alumnos = (
            self.alumno_ctrl.listar_alumno()
        )  # Obtiene nombres reales desde AlumnoController
        nombres = {a.alumno_id: a.nombre for a in alumnos}  # Diccionario ID → nombre
        # Recorremos secuencialmente y reemplazamos IDs por nombres
        reporte = [
            (nombres.get(alumno_id, "Desconocido"), porcentaje)
            for alumno_id, porcentaje in ranking
        ]
        # Ordenamos de mayor a menor (algoritmo de ordenamiento O(n log n))
        reporte.sort(key=lambda x: x[1], reverse=True)
        return reporte

    # ============================================================
    # ALUMNOS DESTACADOS
    # Algoritmo: filtrado + recorrido secuencial
    # Fuente: Reporte de asistencias (reporte_asistencias_alumnos)
    # Propósito: mostrar alumnos con asistencia > 90%
    # ============================================================
    def alumnos_destacados(self):
        reporte = self.reporte_asistencias_alumnos()  # Reutiliza el reporte anterior
        destacados = [
            (nombre, porc) for nombre, porc in reporte if porc > 90
        ]  # Filtrado secuencial O(n)
        return destacados

    # ============================================================
    # ALUMNOS CRÍTICOS
    # Algoritmo: filtrado + recorrido secuencial
    # Fuente: Reporte de asistencias (reporte_asistencias_alumnos)
    # Propósito: mostrar alumnos con asistencia < 60%
    # ============================================================
    def alumnos_criticos(self):
        reporte = self.reporte_asistencias_alumnos()  # Reutiliza el reporte anterior
        criticos = [
            (nombre, porc) for nombre, porc in reporte if porc < 60
        ]  # Filtrado secuencial O(n)
        return criticos

    # ============================================================
    # REPORTE DE CURSOS POR ASISTENCIA
    # Algoritmo: conteo categórico + ordenamiento
    # Fuente: AsistenciaController (ranking_cursos_por_asistencia)
    # Propósito: mostrar cursos ordenados por cantidad de asistencias
    # ============================================================
    def reporte_cursos_asistencia(self):
        ranking = (
            self.asistencia_ctrl.ranking_cursos_por_asistencia()
        )  # Llama al método que agrupa asistencias por curso
        cursos = self.curso_ctrl.listar_cursos()  # Obtiene nombres reales de cursos
        nombres = {c.curso_id: c.nombre for c in cursos}  # Diccionario ID → nombre
        reporte = [
            (nombres.get(curso_id, "Desconocido"), asistencias)
            for curso_id, asistencias in ranking
        ]
        reporte.sort(key=lambda x: x[1], reverse=True)  # Ordenamiento O(n log n)
        return reporte

    # ============================================================
    # CURSO CON MAYOR ASISTENCIA
    # Algoritmo: greedy (selección del máximo)
    # Fuente: Reporte de cursos (reporte_cursos_asistencia)
    # Propósito: identificar el curso con más asistencias
    # ============================================================
    def curso_top_asistencia(self):
        ranking = self.reporte_cursos_asistencia()  # Reutiliza el ranking de cursos
        return ranking[0] if ranking else None  # Selecciona el máximo (O(1))

    # ============================================================
    # ESTADÍSTICAS DE CURSOS
    # Algoritmo: divide y vencerás O(n log n)
    # Fuente: CursoController (estadisticas_divide_venceras)
    # Propósito: calcular estadísticas por secciones o subconjuntos
    # ============================================================
    def estadisticas_cursos_divide_venceras(self):
        cursos = self.curso_ctrl.listar_cursos()  # Obtiene lista de cursos desde BD
        return self.curso_ctrl.estadisticas_divide_venceras(
            cursos
        )  # Aplica divide y vencerás recursivo

    # ============================================================
    # RELACIONES DOCENTE-CURSO
    # Algoritmo: grafos O(n + m)
    # Fuente: DocenteController (relaciones_docente_curso)
    # Propósito: mostrar lista de adyacencia docente → cursos
    # ============================================================
    def relaciones_docente_curso(self):
        return (
            self.docente_ctrl.relaciones_docente_curso()
        )  # Llama al método que construye el grafo
