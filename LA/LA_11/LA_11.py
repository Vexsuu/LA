class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describePhone(self):
        print(f" (self.brand) and has a (self-model)")

class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)

    def describePhone(self):
        print(f"This is an Android phone: (self.brand) model (self.model) pro")

ad = Android("Realme", 8)
ad.describePhone()
#Ervex LA11