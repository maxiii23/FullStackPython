from flask import Flask, render_template, request, redirect
# importar la clase de users.py
from users import User

app = Flask(__name__)

@app.route("/")
def get_users():
    # llamar al método de clase get all para obtener todos los amigos
    users = User.get_all()
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
        "first_name": request.form["fname"],
        "last_name" : request.form["lname"],
        "email" : request.form["email"]
    }
    # Pasamos el diccionario de datos al método save de la clase user
    User.newuser( data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
