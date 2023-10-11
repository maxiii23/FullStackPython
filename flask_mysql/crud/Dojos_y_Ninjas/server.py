from flask_app import app 

from flask_app.controllers.dojos import dojos
from flask_app.controllers.ninjas import ninjas

app.register_blueprint(dojos)
app.register_blueprint(ninjas)

if __name__ == "__main__":
    app.run(debug=True)