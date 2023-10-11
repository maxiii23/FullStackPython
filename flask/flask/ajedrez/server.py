from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', row=8, col=8, color_1="red", color_2="black") 

@app.route('/<int:fila>')
def fila(fila):
    return render_template('index.html', row=fila, col=8, color_1="red", color_2="black")                    
       
@app.route('/<int:fila>/<int:columna>')
def fila_columna(fila,columna):
    return render_template('index.html', row=fila, col=columna, color_1="red", color_2="black")         

@app.route('/<int:fila>/<int:columna>/<string:color_1>/<string:color_2>')
def fila_columna_color(fila,columna,color_1,color_2):
    return render_template('index.html', row=fila, col=columna, color_1=color_1, color_2=color_2)         

if __name__ == '__main__':
    app.run(debug=True)