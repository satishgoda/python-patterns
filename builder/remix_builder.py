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

class HouseBuilder(Builder):
    type = "House"
    
    def build_floor(self):
        self.building.floor = "One"
    
    def build_size(self):
        self.building.size = "Big"

class FlatBuilder(Builder):
    type = "Flat"
    
    def build_floor(self):
        self.building.floor = "Three"
    
    def build_size(self):
        self.building.size = "Small"

class Director(object):
    def __init__(self):
        self.builder = None
    
    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()
    
    def get_building(self):
        return self.builder.building

if __name__ == '__main__':
    director = Director()
    
    director.builder = HouseBuilder()
    
    director.construct_building()
    
    building = director.get_building()
    
    print building

    director.builder = FlatBuilder()
    
    director.construct_building()
    
    building = director.get_building()
    
    print building
