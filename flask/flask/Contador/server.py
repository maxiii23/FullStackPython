from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.config["SECRET_KEY"] = "X1sj3tnJCF5vZ8LOoOfmyZ3SnIHgwDKYwo0_FS2fJ4Y"

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
        print('la llave existe!')
    else:
        session['count'] = 1
        print("la llave 'count' NO existe")
    if 'in_page' in session:
        session['in_page'] +=1
    else:
        session['in_page'] = 1
    return render_template("index.html")

@app.route('/destroy_session')
def delete_session():
    session.pop('count')
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    session.pop('count')
    return redirect('/')

@app.route('/increment_two', methods=['POST'])
def increment_two():
    session['count'] += 1
    return redirect('/')

@app.route('/manual_increment', methods=['POST'])
def manual_increment():
    session['number'] = request.form['number']
    if session['number'].isnumeric() == True:
        session['count'] += (int(session['number'])-1)
    else:
        session['count']-=1
        return "<h1>Valor ingresado no númerico!</h1> <a href='/'>Volver</a>"
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)