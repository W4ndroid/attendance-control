from ttkthemes import ThemedTk
from tkinter import ttk
from views.reportes_view import ReportesView


def main():
    root = ThemedTk(theme="arc")
    root.title("Sistema de Reportes de Asistencia")

    style = ttk.Style(root)
    style.theme_use("clam")

    # Estilo para filas
    style.configure(
        "Treeview",
        background="#f2f2f2",  # gris claro
        foreground="black",
        rowheight=28,
        fieldbackground="#f2f2f2",
        font=("Arial", 11),
        borderwidth=1,
        relief="solid",
    )

    # Estilo para encabezados
    style.configure(
        "Treeview.Heading",
        font=("Arial", 12, "bold"),
        foreground="white",
        background="#003366",  # azul institucional
        borderwidth=1,
        relief="solid",
    )

    # Mantener azul al pasar el mouse
    style.map(
        "Treeview.Heading",
        background=[("active", "#003366")],
        foreground=[("active", "white")],
    )

    # Color de selección de filas
    style.map(
        "Treeview",
        background=[("selected", "#347083")],
        foreground=[("selected", "white")],
    )

    # Estilo de pestañas
    style.configure("TNotebook.Tab", font=("Arial", 11, "bold"), padding=(10, 5))

    style.configure("TLabel", font=("Arial", 11))

    app = ReportesView(root)
    root.mainloop()


if __name__ == "__main__":
    main()
