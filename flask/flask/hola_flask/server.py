from flask import Flask 


app = Flask(__name__)


@app.route('/')        
def hola_mundo():
    return '¡hola Mundo!' 
    
@app.route('/Dojo')
def Dojo():
  return "Dojo"

@app.route('/say/<name>')
def hola(name):
    print(name)
    return "Hola, " + name
 

@app.route('/users/<int:count>/<username>')
def palabra_repetida(username, count):
    print(username)
    print(count)
    repeated = username * count
    return repeated

@app.errorhandler(404)
def page_not_found(error):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404

if __name__=="__main__":
    app.run(debug=True) 