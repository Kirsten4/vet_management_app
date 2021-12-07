import pdb
from models.owner import Owner
from models.animal import Animal
from models.vet import Vet
from models.note import Note
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository
import repositories.note_repository as note_repository
from datetime import date

# Test delete_all()
animal_repository.delete_all()
print(animal_repository.select_all())

owner_repository.delete_all()
print(owner_repository.select_all())

vet_repository.delete_all()
print(vet_repository.select_all())


# Test save()
owner_1 = Owner("Allan", "01410123456", "123 Buchanan Street, Glasgow, G1 3HL", "allan@fake.com")
owner_repository.save(owner_1)

owner_2 = Owner("Kirsten", "01419876543", "32 Sauchiehall Street, G2 3LW", "kirsten@fake.com")
owner_repository.save(owner_2)

owner_3 = Owner("Kirsten", "01419876543", "32 Sauchiehall Street, , G2 3LW", "kirsten@fake.com")
owner_repository.save(owner_3)

vet_1 = Vet("Noel Fitzpatrick", date(1990, 6, 10), "Noel-Fitzpatrick.jpeg")
vet_repository.save(vet_1)

vet_2 = Vet("James Herriot", date(1939,12,14))
vet_repository.save(vet_2)

vet_3 = Vet("James Herriot", date(1939,12,14))
vet_repository.save(vet_3)

animal_1 = Animal("Juneau", date(2011,11,14), "dog", owner_1, "notes...", vet_2, "juneau.jpeg")
animal_repository.save(animal_1)

animal_2 = Animal("Blue", date(2015,3,17), "rabbit", owner_2, "notes...", vet_1, "blue.jpeg")
animal_repository.save(animal_2)

animal_3 = Animal("Plunkett", date(2017,2,13), "bird", owner_1, "notes...", vet_1, "Plunkett.jpeg")
animal_repository.save(animal_3)

animal_4 = Animal("Maclean", date(2017,3,23), "bird", owner_1, "notes...", vet_1, "macleane.jpeg")
animal_repository.save(animal_4)

note_1 = Note("2021,12,3", "cast put on leg", True, animal_1)
note_repository.save(note_1)

# Test select_all()
print(owner_repository.select_all())
print(vet_repository.select_all())
print(animal_repository.select_all())
print(note_repository.select_all())


# Test select(id)
print(owner_repository.select(owner_2.id).name)
print(vet_repository.select(vet_1.id).name)
print(animal_repository.select(animal_4.id).__dict__)
print(note_repository.select(note_1.id).__dict__)


# Test delete(id)
owner_repository.delete(owner_3.id)
vet_repository.delete(vet_3.id)
animal_repository.delete(animal_3.id)


#  Test update
owner_1.email_address = "allan@email.com"
owner_repository.update(owner_1)

vet_2.qualified_date = "1941-09-12"
vet_repository.update(vet_2)

animal_4.name = "Macleane"
animal_repository.update(animal_4)

pdb.set_trace