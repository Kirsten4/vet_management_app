from flask import Flask, render_template, Blueprint, request, redirect, url_for
from models.owner import Owner
import repositories.owner_repository as owner_repository

owners_blueprint = Blueprint("owners", __name__)

# INDEX
# GET '/owners'
@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
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
