from flask import Flask, render_template, request,redirect,url_for, Blueprint
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
from models.animal import Animal

animals_blueprint = Blueprint("animals", __name__)

# INDEX
# GET '/animals'
@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", animals=animals)

# NEW
# GET '/animals/new'
# Return html form to the browser
@animals_blueprint.route("/animals/new")
def new_animal():
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("animals/new.html", owners=owners, vets=vets)

# CREATE
# POST '/animals'
@animals_blueprint.route("/animals", methods=['POST'])
def create_animal():
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    type_of_animal = request.form['type_of_animal']
    owner_id = request.form['owner_id']
    treatment_notes = request.form['treatment_notes']
    vet_id = request.form['vet_id']
    owner = owner_repository.select(owner_id)
    vet = vet_repository.select(vet_id)
    animal = Animal(name, date_of_birth,type_of_animal, owner, treatment_notes, vet)
    animal_repository.save(animal)
    return redirect(url_for(".animals"))