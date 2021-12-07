import unittest
from models.treatment import Treatment


class TestTreatment(unittest.TestCase):
    
    def setUp(self):
        self.treatment = Treatment("kennel cough vaccine", 15.80, 5, 0, 9)

    def test_treatment_has_description(self):
        self.assertEqual("kennel cough vaccine", self.treatment.description)

    def test_treatment_has_price(self):
        self.assertEqual(15.80, self.treatment.price)

    def test_treatment_has_duration(self):
        self.assertEqual(5, self.treatment.duration)

    def test_treatment_has_overnights(self):
        self.assertEqual(0, self.treatment.overnights)

    def test_treatment_has_id(self):
        self.assertEqual(9, self.treatment.id) 