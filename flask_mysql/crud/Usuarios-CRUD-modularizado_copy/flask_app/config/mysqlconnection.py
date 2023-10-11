import pymysql.cursors

# Clase para manejar la conexión a MySQL
class MySQLConnection:
    def __init__(self, db):
        # Inicializar la conexión con la base de datos
        connection = pymysql.connect(host='localhost',
                                     user='root',  # Cambiar el usuario y contraseña según sea necesario
                                     password='root',
                                     db=db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor,
                                     autocommit=True)
        self.connection = connection

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print('Ejecutando consulta:', query)
                executable = cursor.execute(query, data)
                if query.lower().find('insert') >= 0:
                    # Si la consulta es una inserción, retornar el ID de la última fila insertada
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find('select') >= 0:
                    # Si la consulta es una selección, retornar todo lo obtenido de la base de datos
                    # El resultado será una lista de diccionarios
                    result = cursor.fetchall()
                    return result
                else:
                    # Si la consulta no es una inserción o una selección, como una actualización o eliminación, 
                    # confirmar los cambios y no retornar nada
                    self.connection.commit()
            except Exception as e:
                # En caso de que la consulta falle, imprimir un mensaje de error
                print('Algo salió mal', e)
                return False
            finally:
                # Cerrar la conexión
                self.connection.close()

# Esta función connectToMySQL crea una instancia de MySQLConnection, que será utilizada por server.py
# connectToMySQL recibe la base de datos que estamos usando y la utiliza para crear una instancia de MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)
