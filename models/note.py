class Note:
    
    def __init__(self, date, comment, follow_up, animal, id=None):
        self.date = date
        self.comment = comment
        self.follow_up = follow_up
        self.animal = animal
        self.id = id