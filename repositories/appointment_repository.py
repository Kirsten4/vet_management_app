from datetime import datetime
from db.run_sql import run_sql
from models.appointment import Appointment
import repositories.treatment_repository as treatment_repository
import repositories.animal_repository as animal_repository

def save(appointment):
    sql = "INSERT INTO appointments (date, treatment_id, animal_id) VALUES (%s, %s, %s) RETURNING *"
    values = [appointment.date, appointment.treatment.id, appointment.animal.id]
    results = run_sql(sql,values)
    id = results[0]['id']
    appointment.id = id
    return appointment

def select_all():
    appointments = []
    sql = "SELECT * FROM appointments"
    results = run_sql(sql)
    for row in results:
        treatment = treatment_repository.select(row['treatment_id'])
        animal = animal_repository.select(row['animal_id'])
        appointment = Appointment(row['date'], treatment, animal, row['id'])
        appointments.append(appointment)
    return appointments

def delete_all():
    sql = "DELETE FROM appointments"
    run_sql(sql)

def select(id):
    appointment = None
    sql = "SELECT * FROM appointments WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    if result is not None:
        treatment = treatment_repository.select(result['treatment_id'])
        animal = animal_repository.select(result['animal_id'])
        appointment = Appointment(result['date'], treatment, animal, result['id'])
    return appointment

def delete(id):
    sql = "DELETE  FROM appointments WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(appointment):
    sql = "UPDATE appointments SET (date, treatment_id, animal_id) = (%s, %s, %s) WHERE id = %s"
    values = [appointment.date, appointment.treatment.id, appointment.animal.id, appointment.id]
    run_sql(sql, values)

def select_all_by_animal(animal):
    appointments = []
    sql = "SELECT * FROM appointments WHERE animal_id = %s"
    values = [animal.id]
    results = run_sql(sql,values)
    for result in results:
        treatment = treatment_repository.select(result['treatment_id'])
        appointment = Appointment(result['date'], treatment, animal, result['id'])
        appointments.append(appointment)
    return appointments







