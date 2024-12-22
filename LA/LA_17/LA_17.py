class Player:
    def __init__(self, name, hp, atk_pwr):
        self.name = name
        self.hp = hp
        self.atk_pwr = atk_pwr
   
    def attack(self, target):
        if target.hp <= 0:
            print(f"{target.name} has already been defeated!")
            return  
       
        target.hp -= self.atk_pwr
        print(f"{self.name} attacked {target.name} for {self.atk_pwr} damage")
       
       
        if target.hp <= 0:
            print(f"{target.name} has been defeated!")
       
    def heal(self, amount):
        if self.hp > 0:
            self.hp += amount
            print(f"{self.name} healed for {amount} health. Current HP: {self.hp}")
        else:
            print(f"{self.name} cannot heal because they're already dead")

eudora = Player("Eudora", 1250, 1200)
nana = Player("Nana", 6000, 250)


while eudora.hp > 0 and nana.hp > 0:
    eudora.attack(nana)
   
    if nana.hp > 0:  
        nana.attack(eudora)
   

if eudora.hp > 0:
    eudora.heal(5)

if nana.hp > 0:  
    nana.heal(5)