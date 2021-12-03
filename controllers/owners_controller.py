from flask import Flask, render_template, Blueprint
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