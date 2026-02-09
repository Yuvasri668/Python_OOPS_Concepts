from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod  #decorator
    def start_engine(self):
        pass

class car(vehicle):
    def start_engine(self):
        print("The car engine started")

class bike(vehicle):
    def start_engine(self):
        print("The car engine started")

class bus(vehicle):
    def start_engine(self):
        print("The bus engine started")

c=car()
c.start_engine()

