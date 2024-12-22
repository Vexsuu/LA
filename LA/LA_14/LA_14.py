# LA#14: Spider-man Polymorphism
class Spiderman:
    def __init__(self, name):
        self.name = name
    
    def describe(self):
        return f"I am Spider-man called {self.name}"

class Toby(Spiderman):
    def describe(self):
        return f"{super().describe()} - The Original Trilogy Spider-man"

class Andrew(Spiderman):
    def describe(self):
        return f"{super().describe()} - The Amazing Spider-man"

class Tom(Spiderman):
    def describe(self):
        return f"{super().describe()} - The MCU Spider-man"

# Testing Spider-man classes
toby = Toby("Tobey Maguire")
andrew = Andrew("Andrew Garfield")
tom = Tom("Tom Holland")

print("=== Spider-man Demo ===")
for spidey in [toby, andrew, tom]:
    print(spidey.describe())

print("\n")