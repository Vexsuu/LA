class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def __str__(self):
        return f"This is a {self.brand} car"


my_car = Car("Toyota")


print("Original object:")
print(my_car)

del my_car

print(my_car)
