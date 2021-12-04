from db.run_sql import run_sql
from models.animal import Animal
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository

def save(animal):
    sql = "INSERT INTO animals (name, date_of_birth, type_of_animal, owner_id, treatment_notes, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.date_of_birth, animal.type_of_animal, animal.owner.id, animal.treatment_notes, animal.vet.id]
    results = run_sql(sql,values)
    id = results[0]['id']
    animal.id = id
    return animal

def select_all():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    for row in results:
        owner = owner_repository.select(row['owner_id'])
        vet = vet_repository.select(row['vet_id'])
        animal = Animal(row['name'], row['date_of_birth'], row['type_of_animal'], owner, row['treatment_notes'], vet, row['id'])
        animals.append(animal)
    return animals

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)