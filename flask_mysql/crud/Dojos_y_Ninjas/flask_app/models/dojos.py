from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        
      
        
    
    @classmethod
    def get_all(cls):
        
        query = 'SELECT * FROM dojos'

        results = connectToMySQL('dojos_y_ninjas').query_db('select * from dojos')
        
        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))
        
        return dojos

    @classmethod
    def create_new(cls,form_data):
        query = '''
                INSERT INTO dojos( name, created_at, updated_at ) 
                VALUES ( %(name)s, now() , now() );
                '''

        data = {
                "name": form_data["name"],
            }
        
        print('Created succesfully')

        return connectToMySQL('dojos_y_ninjas').query_db(query,data)

    @classmethod
    def get_one(cls,id):
        
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = {
            'id' : id
        }
        results = connectToMySQL('dojos_y_ninjas').query_db(query,data)
        selected_dojo = results[0]
        
        return selected_dojo #esto lo saca de la lista para retornar solo el dict.

    
    
    @classmethod
    def edit_dojo(cls,id,form_data):

        query = '''
                UPDATE dojos  
                SET  name  = %(name)s,
                where id = %(id)s
                '''

        data = {
                "name": form_data["name"],
                "id" : id
            }
        
        results = connectToMySQL('dojos_y_ninjas').query_db(query,data)

        return (data)

    @classmethod
    def delete_dojo(cls,id):
        query = '''
                DELETE FROM dojos
                WHERE id = %(id)s;
                '''
        
        data ={
            'id':id
        }

        results = connectToMySQL('dojos_y_ninjas').query_db(query,data)

        return True