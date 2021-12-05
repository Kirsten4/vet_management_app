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
    animals.sort(key=lambda x: x.name)
    return render_template("animals/index.html", animals=animals)

# NEW
# GET '/animals/new'
# Return html form to the browser
@animals_blueprint.route("/animals/new")
def new_animal():
    owners = owner_repository.select_all()
    vets = vet_repository.select_all()
    vets = vet_repository.select_all()
    vet = animal_repository.assign_vet_to_animal(vets)
    return render_template("animals/new.html", owners=owners, vets=vets, vet=vet)

# CREATE
# POST '/animals'
@animals_blueprint.route("/animals", methods=['POST'])
def create_animal():
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    type_of_animal = request.form['type_of_animal']
    owner_id = request.form['owner_id']
    treatment_notes = request.form['treatment_notes']
    # vet_id = request.form['vet_id']
    owner = owner_repository.select(owner_id)
    # vet = vet_repository.select(vet_id)
    vets = vet_repository.select_all()
    vet = animal_repository.assign_vet_to_animal(vets)
    animal = Animal(name, date_of_birth,type_of_animal, owner, treatment_notes, vet)
    animal_repository.save(animal)
    return redirect(url_for(".animals"))

# EDIT
# GET '/animals/<id>/edit'
@animals_blueprint.route("/animals/<id>/edit")
def edit_animal(id):
    owners = owner_repository.select_all() 
    vets = vet_repository.select_all()
    animal = animal_repository.select(id)
    return render_template("animals/edit.html", animal=animal, owners=owners, vets=vets)

# UPDATE
# PUT '/animals/<id>'
@animals_blueprint.route("/animals/<id>", methods=['POST'])
def update_animal(id):
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    type_of_animal = request.form['type_of_animal']
    owner_id = request.form['owner_id']
    treatment_notes = request.form['treatment_notes']
    vet_id = request.form['vet_id']
    owner = owner_repository.select(owner_id)
    vet = vet_repository.select(vet_id)
    animal = Animal(name, date_of_birth, type_of_animal, owner, treatment_notes, vet, id)
    animal_repository.update(animal)
    return redirect(url_for(".animals"))

# DELETE
# DELETE '/animals/<id>'
@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect(url_for(".animals"))