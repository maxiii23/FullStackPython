from flask import Flask, render_template, request, redirect, Blueprint
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja


dojos = Blueprint('dojos', __name__, template_folder='templates')


@dojos.route('/dojos')
def show_dojos():
    dojos = Dojo.get_all()
    for dojo in dojos:
        print(dojo.name, dojo.id)
    return render_template('landing.html',dojos=dojos)

@dojos.route('/dojos', methods=["POST"])
def add_dojo():
    new_dojo = Dojo.create_new(request.form)
    print(new_dojo)
    dojos = Dojo.get_all()
    for dojo in dojos:
        print(dojo.name, dojo.id)
    return redirect('/dojos')


@dojos.route('/dojos/<id>')
def show_dojo(id):
    single_dojo = Dojo.get_one(id)
    dojo_students = Ninja.join_dojo(id)
    return render_template('dojolist.html', single_dojo = single_dojo,dojo_students = dojo_students)


@dojos.route('/dojos/show_all')
def show_all():
    dojos_and_ninjas = Ninja.join_dojos()
    return render_template('all_dojos.html', dojos_and_ninjas = dojos_and_ninjas)
