# LA#15: Animal Sounds Polymorphism
class Dog:
    def speak(self):
        return "Bark!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Chirp!"

def make_animal_sound(animal):
    print(animal.speak())


print("Animal Sounds Demo")
dog = Dog()
cat = Cat()
bird = Bird()

for animal in [dog, cat, bird]:
    make_animal_sound(animal)

print("\n")