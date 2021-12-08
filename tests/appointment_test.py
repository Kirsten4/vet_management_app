import unittest
from models.appointment import Appointment
from datetime import date


class TestAppointment(unittest.TestCase):
    
    def setUp(self):
        self.appointment = Appointment(date(2021, 2, 14), "X-ray", "Blue", 6)

    def test_appointment_has_date(self):
        self.assertEqual(date(2021,2,14), self.appointment.date)

    def test_appointment_has_treatment(self):
        self.assertEqual("X-ray", self.appointment.treatment)

    def test_appointment_has_animal(self):
        self.assertEqual("Blue", self.appointment.animal)

    def test_appointment_has_id(self):
        self.assertEqual(6, self.appointment.id)