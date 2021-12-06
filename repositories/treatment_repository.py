from db.run_sql import run_sql
from models.treatment import Treatment

def select_all():
    treatments = []
    sql = "SELECT * FROM treatments"
    results = run_sql(sql)
    for row in results:
        treatment = Treatment(row['description'], row['price'], row['duration'], row['overnights'], row['id'])
        treatments.append(treatment)
    return treatments

def select(id):
    treatment = None
    sql = "SELECT * FROM treatments WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    if result is not None:
        treatment = Treatment(result['description'], result['price'], result['duration'], result['overnights'], result['id'])
    return treatment