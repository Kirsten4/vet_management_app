from flask import Flask, render_template, request,redirect,url_for, Blueprint
import repositories.animal_repository as animal_repository
from models.animal import Animal

animals_blueprint = Blueprint("animals", __name__)

