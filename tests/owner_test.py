import unittest
from models.owner import Owner


class TestOwner(unittest.TestCase):
    
    def setUp(self):
        self.owner = Owner("Allan", "01410123456", "123 Buchanan Street, Glasgow, G1 3HL", "allan@fake.com",8)

    def test_owner_has_name(self):
        self.assertEqual("Allan", self.owner.name)

    def test_owner_has_phone_number(self):
        self.assertEqual("01410123456", self.owner.phone_number)

    def test_owner_has_address(self):
        self.assertEqual("123 Buchanan Street, Glasgow, G1 3HL", self.owner.address)

    def test_owner_has_email_address(self):
        self.assertEqual("allan@fake.com", self.owner.email_address)

    def test_owner_has_id(self):
        self.assertEqual(8, self.owner.id)