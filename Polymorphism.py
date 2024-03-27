class Animal:
    def __init__(self,name):
        self.name = name
    def talk(self):
        raise NotImplementedError("Error")
class Cat(Animal):
    def talk(self):
        return "meow"
class Dog(Animal):
    def talk(self):
        return "bow bow"
obj = Cat("Billi1")
print(obj.name," - ",obj.talk())
'''
animals = [Cat("Billi2"),Cat("Billi2"),Dog("Moti"),Cat("Billi3"),Dog("gabbar")]
for animal in animals:
    print(animal.name," - ",animal.talk())
'''