from pdb import run
from db.run_sql import run_sql
from models.owner import Owner

def save(owner):
    sql = "INSERT INTO owners (name, phone_number, address, email_address) VALUES (%s,%s,%s,%s) RETURNING *"
    values = [owner.name, owner.phone_number, owner.address, owner.email_address]
    results = run_sql(sql,values)
    id = results[0]['id']
    owner.id = id
    return owner

def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for row in results:
        owner = Owner(row['name'], row['phone_number'], row['address'], row['email_address'], row['id'])
        owners.append(owner)
    return owners

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)