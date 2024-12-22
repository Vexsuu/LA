class Cars:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
bz = Cars("benz","black")
print(bz.brand,bz.color)
bz.color = "green"
print(bz.brand,bz.color)

qw = Cars("bmw", "yellow")
print(qw.brand,qw.color)
