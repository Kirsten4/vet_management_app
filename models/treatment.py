class Treatment:
    
    def __init__(self, description, price, duration, id=None):
        self.description = description
        self.price = price
        self.duration = duration
        self.id = id