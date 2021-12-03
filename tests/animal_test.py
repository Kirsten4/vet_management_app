import unittest
from models.animal import Animal
from datetime import date

class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.animal = Animal("Juneau", date(2011,11,14), "Dog", "Allan", "notes...", "Noel Fitzpatrick",4)

    def test_animal_has_name(self):
        self.assertEqual("Juneau", self.animal.name)

    def test_animal_has_date_of_birth(self):
        self.assertEqual(date(2011,11,14), self.animal.date_of_birth)

    def test_animal_has_type(self):
        self.assertEqual("Dog", self.animal.type_of_animal)

    def test_animal_has_owner(self):
        self.assertEqual("Allan", self.animal.owner)

    def test_animal_has_notes(self):
        self.assertEqual("notes...", self.animal.treatment_notes)

    def test_animal_has_vet(self):
        self.assertEqual("Noel Fitzpatrick", self.animal.vet)

    def test_animal_has_id(self):
        self.assertEqual(4,self.animal.id)