from flask import Flask, render_template, Blueprint
from models.treatment import Treatment
import repositories.treatment_repository as treatment_repository

treatments_blueprint = Blueprint("treatments", __name__)

@treatments_blueprint.route("/treatments")
def treatments():
    treatments = treatment_repository.select_all()
    return render_template("treatments/index.html", treatments=treatments)