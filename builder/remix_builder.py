class Product(object):
    pass

class Building(Product):
    def __init__(self, type):
        self.type = type
        self.floor = None
        self.size = None
    
    def __repr__(self):
        return "Building/{0.type}\n\tFloor: {0.floor}\n\tSize: {0.size}".format(self)

class Builder(object):
    def __init__(self):
        self.building = None
    
    def new_building(self):
        self.building = Building(self.type)
    
    def build_floor(self):
        raise NotImplementedError
    
    def build_size(self):
        raise NotImplementedError
