from flask import Flask, render_template, Blueprint, request, redirect, url_for
from models.vet import Vet
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)

# INDEX
# GET '/vets'
@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets=vets)

# NEW
# GET '/vets/new'
# Return html form to the browser
@vets_blueprint.route("/vets/new")
def new_vet():
    return render_template("vets/new.html")

# CREATE
# POST '/vets'
@vets_blueprint.route("/vets", methods=['POST'])
def create_vet():
    name = request.form['name']
    qualified_date = request.form['qualified_date']
    vet = Vet(name, qualified_date)
    vet_repository.save(vet)
    return redirect(url_for(".vets"))