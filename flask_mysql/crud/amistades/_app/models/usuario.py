from _app.config.connection import connectToMySQL

class Usuario:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO usuarios (first_name , last_name, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,NOW(),NOW());"
        return connectToMySQL('esquema_amistades').query_db( query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL('esquema_amistades').query_db(query)
        usuarios = []
        for usuario in results:
            usuarios.append(usuario)
        return usuarios
    
    @classmethod
    def get_usuarios(cls,data):
        query = "SELECT * FROM usuarios where usuarios.id != %(id)s and usuarios.id not in (select amistades.amigo_id from amistades where amistades.usuario_id = %(id)s);"
        results = connectToMySQL('esquema_amistades').query_db(query,data)
        usuarios = []
        for usuario in results:
            usuarios.append(usuario)
        return usuarios
