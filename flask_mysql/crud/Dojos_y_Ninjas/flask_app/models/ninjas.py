from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
       
        
    @classmethod
    def get_all(cls):
        
        query = 'SELECT * FROM ninjas'

        results = connectToMySQL('dojos_y_ninjas').query_db('select * from ninjas')
        
        ninjas = []

        for user in results:
            ninjas.append(cls(user))
        
        return ninjas

    @classmethod
    def create_new(cls,form_data):
        query = '''
                INSERT INTO ninjas ( first_name , last_name , age , created_at, updated_at, dojo_id ) 
                VALUES ( %(first_name)s , %(last_name)s , %(age)s , NOW() , NOW(), %(dojo_id)s );
                '''

        data = {
                "first_name": form_data["first_name"],
                "last_name" : form_data["last_name"],
                "age" : int(form_data["age"]),
                "dojo_id" : int(form_data["dojos"])
            }
        

        return connectToMySQL('dojos_y_ninjas').query_db(query,data)

    @classmethod
    def get_one(cls,id):
        
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        data = {
            'id' : id
        }
        results = connectToMySQL('dojos_y_ninjas').query_db(query,data)
        
        
        return results #esto lo saca de la lista para retornar solo el dict.

    @classmethod
    def edit_user(cls,id,form_data):

        query = '''
                UPDATE ninjas  
                SET  first_name  = %(first_name)s,
                last_name  = %(last_name)s,
                age  = %(age)s
                where id = %(id)s
                '''

        data = {
                "first_name": form_data["first_name"],
                "last_name" : form_data["last_name"],
                "age" : form_data["age"],
                "id" : id
            }
        
        results = connectToMySQL('dojos_y_ninjas').query_db(query,data)

        return (data)

    @classmethod
    def delete_user(cls,id):
        query = '''
                DELETE FROM ninjas
                WHERE id = %(id)s;
                '''
        
        data ={
            'id':id
        }

        results = connectToMySQL('dojos_y_ninjas').query_db(query,data)

        return True

    @classmethod
    def join_dojo(cls,dojo_id):
        query = '''
                select * from ninjas
                join dojos on dojos.id = ninjas.dojo_id
                WHERE dojos.id = %(dojo_id)s;
                '''

        data = {
            'dojo_id' : dojo_id
        }

        results = connectToMySQL('dojos_y_ninjas').query_db(query,data)

        return results

    @classmethod
    def join_dojos(cls):
        query = '''
                select dojos.name, first_name, last_name, age from ninjas
                join dojos on dojos.id = ninjas.dojo_id;
                '''


        results = connectToMySQL('dojos_y_ninjas').query_db(query,)
        
        return results
