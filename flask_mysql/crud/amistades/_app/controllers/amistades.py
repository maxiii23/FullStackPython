from flask import jsonify, render_template, request, redirect
from _app.models.amistad import Amistad
from _app.models.usuario import Usuario
from _app import app

@app.route("/")
def index():
    return redirect('/friendships')

@app.route("/friendships")
def show():
    usuarios = Usuario.get_all()
    amistades = Amistad.get_all()
    return render_template('index.html', usuarios = usuarios, amistades = amistades)

@app.route('/create_usuario', methods=["POST"])
def NewUsuario():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"]
    }
    Usuario.save(data)
    return redirect('/')

@app.route('/create_amistad', methods=["POST"])
def NewAmistad():
    data = {
        "usuario_id": int(request.form["usuario_id"]),
        "amigo_id": int(request.form["amigo_id"])
    }
    Amistad.save(data)
    return redirect('/')


@app.route('/usuario/<id>')
def showUsuarios(id):
    idUsuario = id
    data = {
        "id": int(idUsuario)
    }
    usuarios = Usuario.get_usuarios(data)
    return jsonify({'friend': usuarios})
