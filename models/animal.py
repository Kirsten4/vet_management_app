class Animal:
    
    def __init__(self, name, date_of_birth, type_of_animal, owner, treatment_notes, vet, photo=None, checked_in_time=None, checked_out_time=None, id=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.type_of_animal = type_of_animal
        self.owner = owner
        self.treatment_notes = treatment_notes
        self.vet = vet
        self.photo = photo
        self.checked_in_time = checked_in_time
        self.checked_out_time = checked_out_time
        self.id = id
        