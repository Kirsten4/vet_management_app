class Owner:
    
    def __init__(self, name, phone_number, address, email_address, registered=True, id=None):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email_address = email_address
        self.registered =registered
        self.id = id

    def unregister(self):
        self.registered = False