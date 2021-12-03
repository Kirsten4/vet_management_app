from db.run_sql import run_sql
from models.vet import Vet

def save(vet):
    sql = "INSERT INTO vets (name, qualified_date) VALUES (%s,%s) RETURNING *"
    values = [vet.name, vet.qualified_date]
    results = run_sql(sql,values)
    id = results[0]['id']
    vet.id = id
    return vet

def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        vet = Vet(row['name'], row['qualified_date'])
        vets.append(vet)
    return vets

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)