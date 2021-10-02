from homework_02 import base
from homework_02 import exceptions



class Plane(base.Vehicle):

    cargo = 0
    max_cargo = 100

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super(Plane, self).__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, number):
        if self.cargo + number <= self.max_cargo:
            self.cargo = self.cargo + number
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        new_cargo = self.cargo
        self.cargo = 0
        return new_cargo