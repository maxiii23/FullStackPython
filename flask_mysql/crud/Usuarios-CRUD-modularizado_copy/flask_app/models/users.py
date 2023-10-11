from flask_app.config.mysqlconnection import connectToMySQL
import re # Importamos expresiones regulares
from flask import flash

# Expresión regular para validar direcciones de correo electrónico
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+[a-zA-Z]+$')

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def read(cls):
        # Consulta para obtener todos los usuarios desde la base de datos
        query = 'SELECT * FROM users'
        results = connectToMySQL('users').query_db(query)
        users = []
        for u in results:
            users.append(cls(u))
        return users
    
    @classmethod
    def create(cls, formulario):
        # Insertar un nuevo usuario en la base de datos
        query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)'
        result = connectToMySQL('users').query_db(query, formulario)
        return result
    
    @classmethod
    def delete(cls, formulario):
        # Eliminar un usuario de la base de datos por su ID
        query = 'DELETE FROM users WHERE id = %(id)s'
        result = connectToMySQL('users').query_db(query, formulario)
        return result
    
    @classmethod
    def update(cls, formulario):
        # Actualizar la información de un usuario en la base de datos
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s"
        result = connectToMySQL('users').query_db(query, formulario)
        return result

    @classmethod
    def mostrar(cls, formulario):
        # Obtener los detalles de un usuario por su ID
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('users').query_db(query, formulario)
        usr = result[0]
        user = cls(usr)
        return user
