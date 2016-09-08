class Product(object):
    pass

class Building(Product):
    def __init__(self, type):
        self.type = type
        self.floor = None
        self.size = None
    
    def __repr__(self):
        return "Building/{0.type}\n\tFloor: {0.floor}\n\tSize: {0.size}".format(self)
