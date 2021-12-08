from flask import Flask, render_template, Blueprint, request, redirect, url_for
from models.vet import Vet
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository

vets_blueprint = Blueprint("vets", __name__)

# INDEX
# GET '/vets'
@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    animal_dict = {}
    for vet in vets:
        number_animals = len(animal_repository.select_all_by_vet(vet))
        animal_dict[vet.name] = number_animals
    vets.sort(key=lambda x: x.name)
    return render_template("vets/index.html", vets=vets, animal_dict=animal_dict)

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
    photo = request.form['photo']
    vet = Vet(name, qualified_date, photo)
    vet_repository.save(vet)
    return redirect(url_for(".vets"))

# EDIT
# GET '/vets/<id>/edit'
@vets_blueprint.route("/vets/<id>/edit")
def edit_vet(id):
    vet = vet_repository.select(id)
    return render_template("vets/edit.html", vet=vet)

# UPDATE
# PUT '/vets/<id>'
@vets_blueprint.route("/vets/<id>", methods=['POST'])
def update_vet(id):
    name = request.form['name']
    qualified_date = request.form['qualified_date']
    photo = request.form['photo']
    vet = Vet(name, qualified_date, photo, id)
    vet_repository.update(vet)
    return redirect(url_for(".vets"))

# DELETE
# DELETE '/vets/<id>'
@vets_blueprint.route("/vets/<id>/delete", methods=['POST'])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect(url_for(".vets"))