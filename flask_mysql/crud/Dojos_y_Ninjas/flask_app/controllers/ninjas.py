from flask import Flask, render_template, request, redirect, Blueprint
from flask_app.models.ninjas import Ninja
from flask_app.models.dojos import Dojo


ninjas = Blueprint('ninjas', __name__, template_folder='templates')


@ninjas.route('/ninjas')
def show_create():
    dojos = Dojo.get_all()


    return render_template('create.html',ninjas=ninjas,dojos = dojos)


@ninjas.route('/ninjas',methods=["POST"])
def create_ninja():
    print(f'EL ID ES: {request.form["dojos"]}')
    dojos = Dojo.get_all()

    for dojo in dojos:
        print(dojo.name, dojo.id)
    Ninja.create_new(request.form)
    
    return redirect('/dojos')