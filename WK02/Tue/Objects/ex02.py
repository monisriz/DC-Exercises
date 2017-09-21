# #2 Make your own class

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.year, self.make, self.model)
car = Vehicle('Honda', 'Accord', 2015)
car.print_info()
