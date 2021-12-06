from flask import Flask, render_template, request,redirect,url_for, Blueprint
import repositories.appointment_repository as appointment_repository
import repositories.animal_repository as animal_repository
import repositories.treatment_repository as treatment_repository
from models.appointment import Appointment

appointments_blueprint = Blueprint("appointments", __name__)

# INDEX
# GET '/appointments'
@appointments_blueprint.route("/appointments")
def appointments():
    appointments = appointment_repository.select_all()
    appointments.sort(key=lambda x: x.date)
    return render_template("appointments/index.html", appointments=appointments)

# NEW
# GET '/appointments/new'
# Return html form to the browser
@appointments_blueprint.route("/appointments/new")
def new_appointment():
    treatments = treatment_repository.select_all()
    animals = animal_repository.select_all()
    return render_template("appointments/new.html", treatments=treatments, animals=animals)

# CREATE
# POST '/appointments'
@appointments_blueprint.route("/appointments", methods=['POST'])
def create_appointment():
    date = request.form['date']
    treatemnt_id = request.form['treatment_id']
    animal_id = request.form['animal_id']
    treatment = treatment_repository.select(treatemnt_id)
    animal = animal_repository.select(animal_id)
    appointment = Appointment(date,treatment, animal)
    appointment_repository.save(appointment)
    return redirect(url_for(".appointments"))

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
    place_holder_animal = animal_repository.select(id)
    checked_in_time = place_holder_animal.checked_in_time
    checked_out_time = place_holder_animal.checked_out_time
    photo = request.form['photo']
    animal = Animal(name, date_of_birth, type_of_animal, owner, treatment_notes, vet, photo, checked_in_time, checked_out_time, id)
    animal_repository.update(animal)
    return redirect(url_for(".animals"))

# DELETE
# DELETE '/animals/<id>'
@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect(url_for(".animals"))