from flask import Flask, render_template, request, redirect
# importar la clase de users.py


from Users import user


app = Flask(__name__)

@app.route("/")
def get_users():
    # llamar al método de clase get all para obtener todos los amigos
    users = user.get_all()
    print(users)
    return render_template("read_users.html", all_users = users)

@app.route("/users/new", methods=["GET"])
def get_newusers():
    return render_template("new_users.html")


@app.route('/users/new', methods=["POST"])
def post_newusers():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    new_user_id = user.newuser(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect(f'/users/{new_user_id}')

@app.route("/users/<int:id>", methods=['GET'])
def get_user_by_id(id):
   
    # llamar al método de clase get all para obtener todos los amigos
    userone = user.get_one(id)
    return render_template("show_users.html", one_users = userone)
    

@app.route("/users/<int:id>/edit", methods=['GET'])
def get_edit_user_by_id(id):
   
    # llamar al método de clase get all para obtener todos los amigos
    userone = user.get_one(id)
    return render_template("edit_users.html", one_users = userone)

@app.route('/users/<int:id>/edit', methods=["POST"])
def post_edit_user_by_id(id):
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "id": id,
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    user.edituser(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect(f'/users/{id}')

@app.route("/users/<int:id>/destroy", methods=[ 'GET'])
def post_delete_user_by_id(id):
   
    # llamar al método de clase get all para obtener todos los amigos
    user.delete_one_user(id)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
