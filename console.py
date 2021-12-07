import pdb
from models.appointment import Appointment
from models.owner import Owner
from models.animal import Animal
from models.treatment import Treatment
from models.vet import Vet
from models.note import Note
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository
import repositories.note_repository as note_repository
import repositories.appointment_repository as appointment_repository
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

owner_4 = Owner("Ross", "01419876543", "111 Argyle Street, , Glasgow, G3 8AD", "ross@fake.com")
owner_repository.save(owner_4)

owner_5 = Owner("Jack", "01419876543", "64 Argyle Street, , Glasgow, G3 8AD", "jack@fake.com")
owner_repository.save(owner_5)

owner_6 = Owner("Sacha", "01419876543", "23 Albion Street, , Glasgow, G5 2DW", "sacha@fake.com")
owner_repository.save(owner_6)

owner_7 = Owner("Tamer", "01419876543", "97 Albion Street, , Glasgow, G5 2DW", "tamer@fake.com")
owner_repository.save(owner_7)

vet_1 = Vet("Noel Fitzpatrick", date(1990, 6, 10), "Noel-Fitzpatrick.jpeg")
vet_repository.save(vet_1)

vet_2 = Vet("James Herriot", date(1939,12,14), "James Herriot.jpeg")
vet_repository.save(vet_2)

vet_3 = Vet("James Herriot", date(1939,12,14))
vet_repository.save(vet_3)

animal_1 = Animal("Juneau", date(2011,11,14), "Dog", owner_1, vet_2, "juneau.jpeg")
animal_repository.save(animal_1)

animal_2 = Animal("Blue", date(2015,3,17), "Rabbit", owner_2, vet_1, "blue.jpeg")
animal_repository.save(animal_2)

animal_3 = Animal("Plunkett", date(2017,2,13), "Bird", owner_1, vet_1, "Plunkett.jpeg")
animal_repository.save(animal_3)

animal_4 = Animal("Maclean", date(2017,3,23), "Bird", owner_1, vet_1, "macleane.jpeg")
animal_repository.save(animal_4)

animal_5 = Animal("Plunkett", date(2017,2,13), "Bird", owner_1, vet_1, "Plunkett.jpeg")
animal_repository.save(animal_5)

animal_6 = Animal("Oslo", date(2018,2,3), "Cat", owner_4, vet_2, "oslo.jpeg")
animal_repository.save(animal_6)

animal_7 = Animal("Archie", date(2019,7,18), "Dog", owner_5, vet_1, "archie.jpg")
animal_repository.save(animal_7)

animal_8 = Animal("Samba", date(2016,4,23), "Dog", owner_7, vet_2, "samba.png")
animal_repository.save(animal_8)

animal_9 = Animal("Fiona", date(2015,8,2), "Cat", owner_7, vet_1, "Fiona.png")
animal_repository.save(animal_9)

animal_10 = Animal("Wilbur", date(2018,10,7), "Dog", owner_6, vet_1, "wilbur.png")
animal_repository.save(animal_10)

animal_11 = Animal("Arwen", date(2014,12,5), "Snake", owner_2, vet_1, "arwen.jpeg")
animal_repository.save(animal_11)

note_1 = Note("2021,12,3", "cast put on leg", True, animal_1)
note_repository.save(note_1)

note_2 = Note("2021,6,15", "nails clipped", False, animal_1)
note_repository.save(note_2)

note_3 = Note("2021,9,24", "teeth checked", False, animal_2)
note_repository.save(note_3)

treatment_1 = Treatment('General health check-up', 62.50, 20,0, 1)
treatment_2 = Treatment('Blood test', 36.00, 10,0, 7)
treatment_3 = Treatment('X-ray', 350.00, 10, 0, 10)
treatment_4 = Treatment('Hip replacement', 3500.00, 180, 5, 8)


appointment_1 = Appointment("2022,3,12", treatment_2, animal_6)
appointment_repository.save(appointment_1)
appointment_2 = Appointment("2022,1,5", treatment_1, animal_2)
appointment_repository.save(appointment_2)
appointment_3 = Appointment(date.today(), treatment_3, animal_4)
appointment_repository.save(appointment_3)
appointment_4 = Appointment(date.today(), treatment_4,animal_1)
appointment_repository.save(appointment_4)

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