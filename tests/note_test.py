import unittest
from models.note import Note
from datetime import date


class TestNote(unittest.TestCase):
    
    def setUp(self):
        self.note = Note(date(2021,12,16), "paw examined, no issue seen", False, 3)

    def test_note_has_date(self):
        self.assertEqual(date(2021,12,16), self.note.date)

    def test_note_has_comment(self):
        self.assertEqual("paw examined, no issue seen", self.note.comment)

    def test_note_has_follow_up(self):
        self.assertEqual(False, self.note.follow_up)

    def test_note_has_id(self):
        self.assertEqual(3, self.note.id)