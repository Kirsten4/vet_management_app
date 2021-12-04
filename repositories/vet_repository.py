from db.run_sql import run_sql
from models.vet import Vet

def save(vet):
    sql = "INSERT INTO vets (name, qualified_date, photo) VALUES (%s,%s,%s) RETURNING *"
    values = [vet.name, vet.qualified_date, vet.photo]
    results = run_sql(sql,values)
    id = results[0]['id']
    vet.id = id
    return vet

def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        vet = Vet(row['name'], row['qualified_date'], row['photo'], row['id'])
        vets.append(vet)
    return vets

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    if result is not None:
        vet = Vet(result['name'], result['qualified_date'], result['photo'], result['id'])
    return vet

def delete(id):
    sql = "DELETE  FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(vet):
    sql = "UPDATE vets SET (name, qualified_date, photo) = (%s, %s, %s) WHERE id = %s"
    values = [vet.name, vet.qualified_date, vet.photo, vet.id]
    run_sql(sql, values)