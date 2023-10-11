from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
@app.route('/play/<int:num_boxes>')
@app.route('/play/<int:num_boxes>/<color>')
def show_boxes(num_boxes=3, color='blue'):
    return render_template('index.html', num_boxes=num_boxes, color=color)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
