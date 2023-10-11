'''
from flask import Flask, render_template, request, redirect, url_for

import random

app = Flask(__name__)

# Genera un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Variables para rastrear los intentos y el nombre del ganador
intentos = 0
ganadores = []

@app.route('/', methods=['GET', 'POST'])
def juego():
    print(f"{numero_secreto}")
    global intentos
    
    if request.method == 'POST':
        intento = int(request.form['intento'])
        intentos += 1
        
        if intento < numero_secreto:
            estado = "Demasiado bajo"
        elif intento > numero_secreto:
            estado = "Demasiado alto"
        else:
              ganadores.append({'nombre': request.form['nombre'], 'intentos': intentos})
              return redirect(url_for('ganadores', ganadores=ganadores))
        
        return render_template('juego.html', estado=estado)
    
    return render_template('juego.html', estado="")

@app.route('/ganadores')
def ganadores():
    return render_template('ganadores.html', ganadores=ganadores)

if __name__ == '__main__':
    app.run(debug=True)
    '''

from flask import Flask, render_template, request, redirect, url_for

import random

app = Flask(__name__)

# Genera un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

@app.route('/', methods=['GET', 'POST'])
def juego():
    print(f"{numero_secreto}")
    intentos = 0
    ganadores = []
    
    if request.method == 'POST':
        intento = int(request.form['intento'])
        intentos += 1
        
        if intento < numero_secreto:
            estado = "Demasiado bajo"
        elif intento > numero_secreto:
            estado = "Demasiado alto"
        else:
            ganadores.append({'nombre': request.form['nombre'], 'intentos': intentos})
            return redirect(url_for('ganadores', ganadores=ganadores))
        
        return render_template('juego.html', estado=estado)
    
    return render_template('juego.html', estado="")

@app.route('/ganadores')
def ganadores():
    ganadores = request.args.getlist('ganadores')
    return render_template('ganadores.html', ganadores=ganadores)

if __name__ == '__main__':
    app.run(debug=True)
