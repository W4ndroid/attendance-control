import tkinter as tk
from tkinter import ttk
from controllers.reportes_controller import ReportesController


class ReportesView:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Reportes de Asistencia")
        self.reportes = ReportesController()

        tab_control = ttk.Notebook(root)

        # Pestañas
        tab_alumnos = ttk.Frame(tab_control)
        tab_control.add(tab_alumnos, text="Asistencias por Alumno")
        self.mostrar_asistencias(tab_alumnos)

        tab_destacados = ttk.Frame(tab_control)
        tab_control.add(tab_destacados, text="Alumnos Destacados")
        self.mostrar_destacados(tab_destacados)

        tab_criticos = ttk.Frame(tab_control)
        tab_control.add(tab_criticos, text="Alumnos Críticos")
        self.mostrar_criticos(tab_criticos)

        tab_cursos = ttk.Frame(tab_control)
        tab_control.add(tab_cursos, text="Cursos por Asistencia")
        self.mostrar_cursos(tab_cursos)

        tab_docentes = ttk.Frame(tab_control)
        tab_control.add(tab_docentes, text="Docente-Curso")
        self.mostrar_docentes(tab_docentes)

        tab_control.pack(expand=1, fill="both")

    # ============================================================
    # MÉTODO: Asistencias por alumno
    # ============================================================
    def mostrar_asistencias(self, frame):
        datos = self.reportes.reporte_asistencias_alumnos()

        label = tk.Label(
            frame,
            text="Reporte de Asistencias",
            font=("Arial", 12, "bold"),
            fg="#003366",
        )
        label.pack(pady=5)

        tree = ttk.Treeview(frame, columns=("Alumno", "Asistencia"), show="headings")
        tree.heading("Alumno", text="Alumno", anchor="center")
        tree.heading("Asistencia", text="Porcentaje (%)", anchor="center")
        tree.column("Alumno", anchor="center", width=200)
        tree.column("Asistencia", anchor="center", width=150)

        for nombre, porc in datos:
            tree.insert("", "end", values=(nombre, f"{porc:.2f}"))

        # Alternar colores de filas
        self._alternar_colores(tree)
        tree.pack(expand=1, fill="both")

    def mostrar_destacados(self, frame):
        datos = self.reportes.alumnos_destacados()

        label = tk.Label(
            frame,
            text="Reporte de Alumnos Destacados",
            font=("Arial", 12, "bold"),
            fg="#006633",
        )
        label.pack(pady=5)

        tree = ttk.Treeview(frame, columns=("Alumno", "Asistencia"), show="headings")
        tree.heading("Alumno", text="Alumno", anchor="center")
        tree.heading("Asistencia", text="Porcentaje (%)", anchor="center")
        tree.column("Alumno", anchor="center", width=200)
        tree.column("Asistencia", anchor="center", width=150)

        for nombre, porc in datos:
            tree.insert("", "end", values=(nombre, f"{porc:.2f}"))

        self._alternar_colores(tree)
        tree.pack(expand=1, fill="both")

    def mostrar_criticos(self, frame):
        datos = self.reportes.alumnos_criticos()

        label = tk.Label(
            frame,
            text="Reporte de Alumnos Críticos",
            font=("Arial", 12, "bold"),
            fg="#990000",
        )
        label.pack(pady=5)

        tree = ttk.Treeview(frame, columns=("Alumno", "Asistencia"), show="headings")
        tree.heading("Alumno", text="Alumno", anchor="center")
        tree.heading("Asistencia", text="Porcentaje (%)", anchor="center")
        tree.column("Alumno", anchor="center", width=200)
        tree.column("Asistencia", anchor="center", width=150)

        for nombre, porc in datos:
            tree.insert("", "end", values=(nombre, f"{porc:.2f}"))

        self._alternar_colores(tree)
        tree.pack(expand=1, fill="both")

    def mostrar_cursos(self, frame):
        datos = self.reportes.reporte_cursos_asistencia()

        label = tk.Label(
            frame, text="Reporte de Cursos", font=("Arial", 12, "bold"), fg="#660066"
        )
        label.pack(pady=5)

        tree = ttk.Treeview(frame, columns=("Curso", "Asistencias"), show="headings")
        tree.heading("Curso", text="Curso", anchor="center")
        tree.heading("Asistencias", text="Total Asistencias", anchor="center")
        tree.column("Curso", anchor="center", width=200)
        tree.column("Asistencias", anchor="center", width=150)

        for curso, asistencias in datos:
            tree.insert("", "end", values=(curso, asistencias))

        self._alternar_colores(tree)
        tree.pack(expand=1, fill="both")

    def mostrar_docentes(self, frame):
        datos = self.reportes.relaciones_docente_curso()

        label = tk.Label(
            frame,
            text="Reporte Docente-Curso",
            font=("Arial", 12, "bold"),
            fg="#663300",
        )
        label.pack(pady=5)

        tree = ttk.Treeview(frame, columns=("Docente", "Cursos"), show="headings")
        tree.heading("Docente", text="Docente", anchor="center")
        tree.heading("Cursos", text="Cursos", anchor="center")
        tree.column("Docente", anchor="center", width=200)
        tree.column("Cursos", anchor="center", width=300)

        for docente, cursos in datos.items():
            tree.insert("", "end", values=(docente, ", ".join(cursos)))

        self._alternar_colores(tree)
        tree.pack(expand=1, fill="both")

    # ============================================================
    # MÉTODO AUXILIAR: Alternar colores de filas
    # ============================================================
    def _alternar_colores(self, tree):
        for i, item in enumerate(tree.get_children()):
            if i % 2 == 0:
                tree.item(item, tags=("even",))
            else:
                tree.item(item, tags=("odd",))
        tree.tag_configure("even", background="#f2f2f2")  # gris claro
        tree.tag_configure("odd", background="#d9d9d9")  # gris más oscuro
