from flask_app.config.mysqlconnection import connectToMySQL
import re #Importamos expresiones regulares

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+[a-zA-Z]+$')

from flask import flash

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
        query = 'SELECT * FROM users'
        results = connectToMySQL('users').query_db(query)
        # [
        #	{'id': '1','first_name': 'Cynthia','last_name': 'Apellido','email': 'c@cd.com','created_at': '2002-02'}
        # ] 
        users = []
        for u in results:
            users.append(cls(u))
        return users
    
    @classmethod
    def create(cls, formulario):
        #data = {'first_name': 'C','last_name': 'X','email': 'c@cd.com'}
        query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)'
        result = connectToMySQL('users').query_db(query, formulario)
        return result
    
    @classmethod
    def delete(cls, formulario):
        query = 'DELETE FROM users WHERE id = %(id)s'
        result = connectToMySQL('users').query_db(query, formulario)
        return result
    
    @classmethod
    def update(cls, formulario):
        #formulario = {"id": "1", "first_name": "C", "last_name": "X", "email": "c@cd.com"}
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s"
        result = connectToMySQL('users').query_db(query, formulario)
        return result

    @classmethod
    def mostrar(cls, formulario):
        #formulario = {"id": "1"}
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('users').query_db(query, formulario)
        # [
        #     {'3','Juana','De Arco','juana@codingdojo.com','2022-03-09 14:50:58','2022-03-09 14:50:58'}
        # ]
        usr = result[0]
        user = cls(usr)
        return user
