class Treatment:
    
    def __init__(self, description, price, duration, overnights, id=None):
        self.description = description
        self.price = price
        self.duration = duration
        self.overnights = overnights
        self.id = id