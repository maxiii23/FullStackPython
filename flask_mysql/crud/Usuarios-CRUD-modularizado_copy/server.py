# Importar la aplicación Flask desde el módulo flask_app
from flask_app import app

# Importar el controlador de usuarios desde el módulo flask_app.controllers
from flask_app.controllers import users

# Comprobar si este archivo es el punto de entrada principal
if __name__ == '__main__':
    # Ejecutar la aplicación en modo de depuración (debug) para facilitar la detección de errores
    app.run(debug=True)
