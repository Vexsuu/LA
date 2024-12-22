class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    
    
    def describeVehicle(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Fuel Type: {self.fuel_type}")

 
class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

if __name__ == "__main__":
    
    my_car = Car("Toyota", "Camry", "gasoline")
    print("Car Details:")
    my_car.describeVehicle()
    
    print("\n" + "="*20 + "\n") 
    
    
    my_motorcycle = Motorcycle("Harley-Davidson", "Sportster", "diesel")
    print("Motorcycle Details:")
    my_motorcycle.describeVehicle()