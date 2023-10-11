from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.users import User

# Ruta principal del sitio web
@app.route('/')
def main():
    # Leer usuarios desde la base de datos
    users = User.read()
    
    return render_template('leer.html', users=users)

# Ruta para crear un nuevo usuario
@app.route('/new')
def new():
    return render_template("nuevo.html")

# Ruta para procesar la creación de un nuevo usuario
@app.route('/create', methods=['POST'])
def create():
    # Crear un nuevo usuario con los datos del formulario
    User.create(request.form)
    return redirect('/')

# Ruta para eliminar un usuario por su ID
@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    # Eliminar el usuario con el ID especificado
    User.delete(data)
    return redirect('/')

# Ruta para editar un usuario por su ID
@app.route('/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    # Mostrar los detalles del usuario con el ID especificado para su edición
    user = User.mostrar(data)
    return render_template('editar.html', user=user)

# Ruta para actualizar la información de un usuario
@app.route('/update', methods=['POST'])
def update():
    # Actualizar los datos del usuario con los datos del formulario
    User.update(request.form)
    id = request.form['id']
    return redirect('/show/' + id)

# Ruta para mostrar los detalles de un usuario por su ID
@app.route('/show/<int:id>')
def show(id):
    data = {
        'id': id
    }
    # Mostrar los detalles del usuario con el ID especificado
    user = User.mostrar(data)
    return render_template('/ver.html', user=user)
