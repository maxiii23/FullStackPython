from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.users import User
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)    

@app.route('/')
def main():
    users = User.read()
    
    return render_template('leer.html',users=users)

@app.route('/new')
def new():
    return render_template("nuevo.html")

@app.route('/create', methods=['POST'])
def create():
    User.create(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/')


@app.route('/edit/<int:id>')
def edit(id):
    data = {
        "id": id
    }
    user = User.mostrar(data)
    return render_template('editar.html', user=user)


@app.route('/update', methods=['POST'])
def update():
    User.update(request.form)
    id=request.form['id']
    return redirect('/show/'+id)

@app.route('/show/<int:id>')
def show(id):
    data={
        'id':id
    }
    user=User.mostrar(data)
    return render_template('/ver.html',user=user)
