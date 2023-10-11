from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

#lleva al checkaut
@app.route('/checkout', methods=['POST', 'GET'])         
def checkout():
    print(request.form)
    date = datetime.now()
    sum = int(request.form.get('strawberry')) + int(request.form.get('raspberry')) + int(request.form.get('apple')) 
    print(f"Cobrando : {request.form.get('first_name')} {request.form.get('last_name')} for {sum} fruits")
    return render_template("checkout.html", request = request, date= date, sum = sum)

#lleva a ver todas las frutas
@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    