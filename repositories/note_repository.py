from db.run_sql import run_sql
from models.note import Note
import repositories.animal_repository as animal_repository

def save(note):
    sql = "INSERT INTO notes (date, comment, follow_up, animal_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [note.date, note.comment, note.follow_up, note.animal.id]
    results = run_sql(sql,values)
    id = results[0]['id']
    note.id = id
    return note

def select_all():
    notes = []
    sql = "SELECT * FROM notes"
    results = run_sql(sql)
    for row in results:
        animal = animal_repository.select(row['animal_id'])
        note = Note(row['date'], row['comment'], row['follow_up'], animal, row['id'])
        notes.append(note)
    return notes

def delete_all():
    sql = "DELETE FROM notes"
    run_sql(sql)

def select(id):
    note = None
    sql = "SELECT * FROM notes WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    if result is not None:
        animal = animal_repository.select(result['animal_id'])
        note = Note(result['date'], result['comment'], result['follow_up'], animal, result['id'])
    return note

def select_all_notes_by_animal(animal):
    notes = []
    sql = "SELECT * FROM notes WHERE animal_id = %s"
    values = [animal.id]
    results = run_sql(sql,values)
    for result in results:
        note = Note(result['date'], result['comment'], result['follow_up'], animal, result['id'])
        notes.append(note)
    return notes