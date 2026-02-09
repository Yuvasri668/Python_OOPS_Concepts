from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def sleep(self):
        print("Animal is sleeping")

class Dog(Animal):
    def sound(self):
        print("Bark")
    
class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Moo")

D=Dog()
D.sound()
D.sleep()

c1=Cat()
c1.sound()
c1.sleep()

c2=Cow()
c2.sound()
c2.sleep()
    

