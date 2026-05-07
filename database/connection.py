import pyodbc

### establecemos la conexion con SQL server.


def get_connection():
    try:
        ### configuraremos los parametros segun nuestra configuracion local
        connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost;"  # nombre del servidor
            "DATABASE=ControlAsistencias;"  # Nombre de la base de datos
            "UID=sa;"  # Usuario de SQL Server
            "PWD=AliceD4fn3!;"  # Contraseña
            "Trusted_Connection=no;"  # Usa 'yes' si estas en  autenticación Windows
        )
        print("Conexión establecida.....")
        return connection
    except Exception as e:
        print("Error al conectar con SQL Server: ", e)
        return None
