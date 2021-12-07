from datetime import datetime
from flask import Flask, render_template, request,redirect,url_for, Blueprint
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.note_repository as note_repository
from models.animal import Animal
from models.note import Note

animals_blueprint = Blueprint("animals", __name__)

# INDEX
# GET '/animals'
@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all()
    animals.sort(key=lambda x: x.name)
    checked_in_animals = animal_repository.all_animals_currently_in_practice()
    return render_template("animals/index.html", animals=animals, checked_in_animals=checked_in_animals)

# NEW
# GET '/animals/new'
# Return html form to the browser
@animals_blueprint.route("/animals/new")
def new_animal():
    owners = owner_repository.select_all()
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
    owner = owner_repository.select(owner_id)
    vets = vet_repository.select_all()
    vet = animal_repository.assign_vet_to_animal(vets)
    photo = request.form['photo']
    if owner.registered:
        animal = Animal(name, date_of_birth,type_of_animal, owner, vet, photo)
        animal_repository.save(animal)
        return redirect(url_for(".animals"))
    else:
        return redirect("owners/notregistered") 

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
    vet_id = request.form['vet_id']
    owner = owner_repository.select(owner_id)
    vet = vet_repository.select(vet_id)
    place_holder_animal = animal_repository.select(id)
    checked_in_time = place_holder_animal.checked_in_time
    checked_out_time = place_holder_animal.checked_out_time
    photo = request.form['photo']
    animal = Animal(name, date_of_birth, type_of_animal, owner, vet, photo, checked_in_time, checked_out_time, id)
    animal_repository.update(animal)
    return redirect(url_for(".animals"))

# DELETE
# DELETE '/animals/<id>'
@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect(url_for(".animals"))

# CHECK IN
# POST '/animals/<id>/check_in'
@animals_blueprint.route("/animals/<id>/check_in", methods=['GET', 'POST'])
def check_in_animal(id):
    animal = animal_repository.select(id)
    animal_repository.check_in(animal)
    return redirect(url_for(".animals"))

# CHECK OUT
# POST '/animals/<id>/check_out'
@animals_blueprint.route("/animals/<id>/check_out", methods=['GET','POST'])
def check_out_animal(id):
    animal = animal_repository.select(id)
    animal_repository.check_out(animal)
    return redirect(url_for(".animals"))

# SHOW ANIMAL NOTES
@animals_blueprint.route("/animals/<id>/notes")
def show(id):
    animal = animal_repository.select(id)
    notes = note_repository.select_all_notes_by_animal(animal)
    return render_template("animals/show.html", notes=notes, animal=animal)

# CREATE ANIMAL NOTES
# POST '/animals/<id>/notes'
@animals_blueprint.route("/animals/<id>/notes", methods=['POST'])
def create_note(id):
    date = datetime.today()
    comment = request.form['comment']
    if "follow_up" in request.form:
        follow_up = True
    else:
        follow_up = False
    animal = animal_repository.select(id)
    note = Note(date, comment, follow_up, animal)
    note_repository.save(note)
    # url = "/animals/" + id + "/notes"
    return show(id)

