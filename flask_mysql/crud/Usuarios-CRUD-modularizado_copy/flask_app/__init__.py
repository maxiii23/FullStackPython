from flask import Flask

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Configurar una clave secreta para la aplicación (necesaria para ciertas funcionalidades)
app.secret_key = 'Mi llave secreta'
