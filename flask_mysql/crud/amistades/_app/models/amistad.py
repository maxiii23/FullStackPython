from _app.config.connection import connectToMySQL

class Amistad:
    def __init__( self , data ):
        self.id = data['id']
        self.usuario_id = data['usuario_id']
        self.amigo_id = data['amigo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO amistades (usuario_id, amigo_id, created_at, updated_at) VALUES (%(usuario_id)s,%(amigo_id)s,NOW(),NOW());"
        return connectToMySQL('esquema_amistades').query_db( query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT concat(usuarios.first_name,' ',usuarios.last_name) as user, concat(amigo.first_name,' ',amigo.last_name) as friend FROM usuarios JOIN amistades ON usuarios.id = amistades.usuario_id LEFT JOIN usuarios as amigo ON amigo.id = amistades.amigo_id;"
        results = connectToMySQL('esquema_amistades').query_db(query)
        amitades = []
        for amistad in results:
            amitades.append(amistad)
        return amitades