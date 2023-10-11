from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def chess_board():
    return render_template('index.html', rows=8, columns=8)

@app.route('/<int:x>')
def custom_chess_board_rows(x):
    return render_template('index.html', rows=x, columns=8)

@app.route('/<int:x>/<int:y>')
def custom_chess_board_with_default_colors(x, y):
    return render_template('index.html', rows=x, columns=y, color1='#FFFFFF', color2='#000000', is_columns_color=True)

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def custom_chess_board_with_columns_color(x, y, color1, color2):
    return render_template('index.html', rows=x, columns=y, color1=color1, color2=color2, is_columns_color=True)

if __name__ == '__main__':
    app.run(debug=True)
