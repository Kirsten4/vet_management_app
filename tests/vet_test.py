import unittest
from models.vet import Vet
from datetime import date

class TestVet(unittest.TestCase):
    
    def setUp(self):
        self.vet = Vet("Noel Fitzpatrick", date(1990, 6, 10),"photo.jpeg",6)

    def test_vet_has_name(self):
        self.assertEqual("Noel Fitzpatrick", self.vet.name)

    def test_vet_has_qualification_date(self):
        self.assertEqual(date(1990,6,10), self.vet.qualified_date)

    def test_vet_has_photo(self):
        self.assertEqual("photo.jpeg", self.vet.photo)

    def test_vet_has_id(self):
        self.assertEqual(6, self.vet.id)

