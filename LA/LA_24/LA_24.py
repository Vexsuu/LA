from abc import ABC, abstractmethod

class GameCharacter(ABC): #LA24
    @abstractmethod
    def attack(self):
        pass

class Warrior(GameCharacter):
    def attack(self):
        print("Swings sword!")

class Mage(GameCharacter):
    def attack(self):
        print("Casts a fireball!")

class Archer(GameCharacter):
    def attack(self):
        print("Shoots an arrow!")

class Support(GameCharacter):
    def attack(self):
        print("Heals an ally")

warrior = Warrior()
mage = Mage()
archer = Archer()
support = Support()

warrior.attack()  
mage.attack()     
archer.attack()  
support.attack()