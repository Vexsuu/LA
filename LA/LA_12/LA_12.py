class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def display(self):
        print(f"Toy: {self.name}, Price: P{self.price}")


my_toy = Toy("Car", 10)
my_toy.display()