# LA#16: Appliance Polymorphism
class Appliance:
    def __init__(self, brand):
        self.brand = brand
    
    def operate(self):
        return "Operating generic appliance"

class WashingMachine(Appliance):
    def operate(self):
        return f"{self.brand} washing machine is washing clothes"

class Refrigerator(Appliance):
    def operate(self):
        return f"{self.brand} refrigerator is keeping food cold"

class Microwave(Appliance):
    def operate(self):
        return f"{self.brand} microwave is heating food"


print("Appliance Demo")
washer = WashingMachine("Samsung")
fridge = Refrigerator("LG")
microwave = Microwave("Whirlpool")

appliances = [washer, fridge, microwave]
for appliance in appliances:
    print(appliance.operate())