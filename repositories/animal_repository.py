from db.run_sql import run_sql
from models.animal import Animal
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
from datetime import date, datetime, timezone

def save(animal):
    sql = "INSERT INTO animals (name, date_of_birth, type_of_animal, owner_id, vet_id, photo) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.date_of_birth, animal.type_of_animal, animal.owner.id, animal.vet.id, animal.photo]
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
        animal = Animal(row['name'], row['date_of_birth'], row['type_of_animal'], owner, vet, row['photo'], row['checked_in_time'], row['checked_out_time'], row['id'])
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
        animal = Animal(result['name'], result['date_of_birth'], result['type_of_animal'], owner, vet, result['photo'], result['checked_in_time'], result['checked_out_time'], result['id'])
    return animal

def delete(id):
    sql = "DELETE  FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(animal):
    sql = "UPDATE animals SET (name, date_of_birth, type_of_animal, owner_id, vet_id, photo) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.date_of_birth, animal.type_of_animal, animal.owner.id, animal.vet.id, animal.photo, animal.id]
    run_sql(sql, values)

def select_all_by_vet(vet):
    animals = []
    sql = "SELECT * FROM animals WHERE vet_id = %s"
    values = [vet.id]
    results = run_sql(sql,values)
    for result in results:
        owner = owner_repository.select(result['owner_id'])
        animal = Animal(result['name'], result['date_of_birth'], result['type_of_animal'], owner, vet, result['photo'], result['checked_in_time'], result['checked_out_time'], result['id'])
        animals.append(animal)
    return animals

def select_all_by_owner(owner):
    animals = []
    sql = "SELECT * FROM animals WHERE owner_id = %s"
    values = [owner.id]
    results = run_sql(sql,values)
    for result in results:
        vet = vet_repository.select(result['vet_id'])
        animal = Animal(result['name'], result['date_of_birth'], result['type_of_animal'], owner, vet, result['photo'], result['checked_in_time'], result['checked_out_time'], result['id'])
        animals.append(animal)
    return animals

def assign_vet_to_animal(vets):
    selected_vet = vets[0]
    number_of_animals = len(select_all_by_vet(vets[0]))
    for vet in vets:
        if len(select_all_by_vet(vet)) < number_of_animals:
            selected_vet = vet
            number_of_animals = len(select_all_by_vet(vet))
    return selected_vet

def check_in(animal):
    animal.checked_in_time = datetime.now()
    animal.checked_out_time = None
    sql = "UPDATE animals SET (checked_in_time, checked_out_time) = (%s,%s) WHERE id = %s"
    values = [animal.checked_in_time, animal.checked_out_time, animal.id]
    run_sql(sql, values)


def check_out(animal):
    animal.checked_out_time = datetime.now(timezone.utc)
    sql = "UPDATE animals SET checked_out_time = %s WHERE id = %s"
    values = [animal.checked_out_time, animal.id]
    run_sql(sql, values)

def all_animals_currently_in_practice():
    sql = "SELECT animals.name, animals.checked_in_time, treatments.description, vets.name, treatments.overnights, animals.id FROM vets INNER JOIN animals ON animals.vet_id = vets.id INNER JOIN appointments ON appointments.animal_id = animals.id INNER JOIN treatments ON treatments.id = appointments.treatment_id WHERE animals.checked_in_time IS NOT NULL AND animals.checked_out_time IS NULL AND appointments.date <= CURRENT_DATE"
    results = run_sql(sql)
    return results

