import unittest
from models.vet import Vet
from datetime import date

class TestVet(unittest.TestCase):
    
    def setUp(self):
        self.vet = Vet("Noel Fitzpatrick", date(1990, 6, 10))

    def test_vet_has_name(self):
        self.assertEqual("Noel Fitzpatrick", self.vet.name)

    def test_vet_has_qualification_date(self):
        self.assertEqual(date(1990,6,10), self.vet.qualified_date)