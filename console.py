import pdb
from models.owner import Owner
from models.animal import Animal
from models.vet import Vet
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

owner_repository.delete_all()
print(owner_repository.select_all())

owner_1 = Owner("Allan", "01410123456", "123 Buchanan Street, Glasgow, G1 3HL", "allan@fake.com")
owner_repository.save(owner_1)

owner_2 = Owner("Kirsten", "01419876543", "32 Sauchiehall Street, G2 3LW", "kirsten@fake.com")
owner_repository.save(owner_2)

print(owner_repository.select_all())

# "Peter Wright"
# "Julian Norton"
# "Noel Fitzpatrick"
# James Herriot

pdb.set_trace