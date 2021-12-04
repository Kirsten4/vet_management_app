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

def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    if result is not None:
        owner = owner_repository.select(result['owner_id'])
        vet = vet_repository.select(result['vet_id'])
        animal = Animal(result['name'], result['date_of_birth'], result['type_of_animal'], owner, result['treatment_notes'], vet, result['id'])
    return animal

def delete(id):
    sql = "DELETE  FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(animal):
    sql = "UPDATE animals SET (name, date_of_birth, type_of_animal, owner_id, treatment_notes, vet_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.date_of_birth, animal.type_of_animal, animal.owner.id, animal.treatment_notes, animal.vet.id, animal.id]
    run_sql(sql, values)