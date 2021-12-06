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
# GET '/appointments/<id>/edit'
@appointments_blueprint.route("/appointments/<id>/edit")
def edit_appointment(id):
    treatments = treatment_repository.select_all()
    animals = animal_repository.select_all()
    appointment = appointment_repository.select(id)
    return render_template("appointments/edit.html", treatments=treatments, animals=animals, appointment=appointment)

# UPDATE
# PUT '/appointments/<id>'
@appointments_blueprint.route("/appointments/<id>", methods=['POST'])
def update_appointment(id):
    date = request.form['date']
    treatemnt_id = request.form['treatment_id']
    animal_id = request.form['animal_id']
    treatment = treatment_repository.select(treatemnt_id)
    animal = animal_repository.select(animal_id)
    place_holder_appointment = appointment_repository.select(id)
    total_bill = place_holder_appointment.total_bill
    appointment = Appointment(date, treatment, animal, total_bill, id)
    appointment_repository.update(appointment)
    return redirect(url_for(".appointments"))

# DELETE
# DELETE '/appointments/<id>'
@appointments_blueprint.route("/appointments/<id>/delete", methods=['POST'])
def delete_appointment(id):
    appointment_repository.delete(id)
    return redirect(url_for(".appointments"))

