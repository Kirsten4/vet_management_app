from flask import Flask, render_template

from controllers.animals_controller import animals_blueprint
from controllers.owners_controller import owners_blueprint
from controllers.vets_controller import vets_blueprint
from controllers.treatments_controller import treatments_blueprint
from controllers.appointments_controller import appointments_blueprint

app = Flask(__name__)

app.register_blueprint(animals_blueprint)
app.register_blueprint(owners_blueprint)
app.register_blueprint(vets_blueprint)
app.register_blueprint(treatments_blueprint)
app.register_blueprint(appointments_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)