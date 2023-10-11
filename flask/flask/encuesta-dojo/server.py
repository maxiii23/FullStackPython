from flask import Flask, request, render_template, redirect, session, url_for

app = Flask(__name__)

# Configura una clave secreta para la sesión (puedes cambiarla)
app.secret_key = 'mi_clave_secreta'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtén los datos del formulario
        nombre = request.form['nombre']
        lugar = request.form['lugar']
        lenguaje = request.form['lenguaje']
        comentario = request.form['comentario']

        # Guarda los datos en la sesión
        session['nombre'] = nombre
        session['lugar'] = lugar
        session['lenguaje'] = lenguaje
        session['comentario'] = comentario

        return redirect(url_for('result'))

    return render_template('index.html')

@app.route('/result')
def result():
    # Obtén los datos de la sesión
    nombre = session.get('nombre')
    correo = session.get('correo')
    opciones = session.get('opciones')
    casillas = session.get('casillas')
    castillaleon = session.get('castillaleon')

    return render_template('result.html', nombre=nombre, correo=correo, opciones=opciones, casillas=casillas)

if __name__ == '__main__':
    app.run(debug=True)
