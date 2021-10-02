from homework_02 import exceptions

class Vehicle():

    started = False

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == False:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance_mile):
        if self.fuel - distance_mile * self.fuel_consumption >= 0:
            self.fuel = self.fuel - distance_mile * self.fuel_consumption
        else:
            raise exceptions.NotEnoughFuel