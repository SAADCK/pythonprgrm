from abc import ABC,abstractmethod
class Animal(ABC):
          
          @abstractmethod
          def sound(self):          
                    pass
class Dog(Animal):
                    def sound(self):
                              return "Woof!"
                   
class cat(Animal):
          def sound(self):
                    return "Meow!"
def animal_sound(animal:Animal):
          print(animal.sound())
dog = Dog() 
cat = cat()
animal_sound(dog)
animal_sound(cat)     