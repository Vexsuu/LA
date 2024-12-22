
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class Fish(Animal):
    
    def __init__(self, name, type, can_swim):
        
        super().__init__(name, type)
      
        self.can_swim = can_swim

my_fish = Fish("Nemo", "Clownfish", True)


print(f"Fish name: {my_fish.name}")
print(f"Fish type: {my_fish.type}")
print(f"Can the fish swim? {my_fish.can_swim}")