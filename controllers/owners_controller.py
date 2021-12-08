from flask import Flask, render_template, Blueprint, request, redirect, url_for
from models.owner import Owner
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository

owners_blueprint = Blueprint("owners", __name__)

# INDEX
# GET '/owners'
@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    owners.sort(key=lambda x: x.name)
    return render_template("owners/index.html", owners=owners)

# NEW
# GET '/owners/new'
# Return html form to the browser
@owners_blueprint.route("/owners/new")
def new_owner():
    return render_template("owners/new.html")

# CREATE
# POST '/owners'
@owners_blueprint.route("/owners", methods=['POST'])
def create_owner():
    name = request.form['name']
    phone_number = request.form['phone_number']
    address = f"{request.form['address_1']}, {request.form['address_2']}, {request.form['address_3']}, {request.form['address_4']}"
    email_address = request.form['email_address']
    owner = Owner(name, phone_number, address, email_address)
    owner_repository.save(owner)
    return redirect(url_for(".owners"))

# EDIT
# GET '/owners/<id>/edit'
@owners_blueprint.route("/owners/<id>/edit")
def edit_owner(id):
    owner = owner_repository.select(id)
    address_list = owner.address.split(", ")
    return render_template("owners/edit.html", owner=owner, address_list=address_list)

# UPDATE
# PUT '/owners/<id>'
@owners_blueprint.route("/owners/<id>", methods=['POST'])
def update_owner(id):
    name = request.form['name']
    phone_number = request.form['phone_number']
    address = f"{request.form['address_1']}, {request.form['address_2']}, {request.form['address_3']}, {request.form['address_4']}"
    email_address = request.form['email_address']
    if "registered" in request.form:
        registered = True
    else:
        registered = False
    owner = Owner(name, phone_number, address, email_address, registered, id)
    owner_repository.update(owner)
    return redirect(url_for(".owners"))

# DELETE
# DELETE '/owners/<id>'
@owners_blueprint.route("/owners/<id>/delete", methods=['POST'])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect(url_for(".owners"))

# SHOW
@owners_blueprint.route("/owners/<id>")
def show(id):
    owner = owner_repository.select(id)
    animals = animal_repository.select_all_by_owner(owner)
    return render_template("owners/show.html", owner=owner, animals=animals)

# SHOW OWNER IS NOT REGISTERED
@owners_blueprint.route("/owners/notregistered")
def show_unregistered():
    owners = owner_repository.select_all()
    return render_template("owners/notregistered.html", owners=owners)

# REREGISTER OWNER
@owners_blueprint.route("/owners/register", methods=['POST'])
def re_register_owner():
    owner_id = request.form['owner_id']
    owner = owner_repository.select(owner_id)
    owner_repository.reregister(owner)
    return redirect("/animals/new")