class Appointment:

    def __init__(self, date, treatment, animal, total_bill=None, id=None):
        self.date = date
        self.treatment = treatment
        self.animal = animal
        self.total_bill = total_bill
        self.id = id
        