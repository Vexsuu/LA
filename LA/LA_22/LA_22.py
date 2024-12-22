class bday:
    def __init__(self, name):
        self.name = name
        
    def __gift(self): 
        print(f"Ang may birthday ay si {self.name}")
    def celebrant(self):
        print("Siya ay si...")
        self.__gift()
        
bday_boy = bday("Vexsu")
bday_boy.celebrant()
bday_boy.__gift() #do not call out like this

