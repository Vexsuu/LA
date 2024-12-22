class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.base_power = power  # Store original power for reset

    def attack(self, target):
        target.health -= self.power
        return f"{self.name} attacks {target.name}! {target.name}'s remaining health: {target.health}"

    def special_move(self):
        return "Base special move"
    
    def defend(self, attacker):
        damage_reduction = attacker.power // 2
        self.health -= (attacker.power - damage_reduction)
        return f"{self.name} defends against {attacker.name} and reduces damage by {damage_reduction}!"

class Warrior(Character):
    def special_move(self):
        self.power = self.base_power * 2
        return f"Warrior uses Shield Bash! Attack power doubled to {self.power}!"

class Mage(Character):
    def special_move(self):
        damage = 100
        return f"Mage casts Fireball! Deals {damage} fixed damage!"

class Archer(Character):
    def special_move(self):
        return "Archer shoots a Piercing Arrow! Defense ignored!"

class Monster(Character):
    def special_move(self):
        health_gain = 50
        self.health += health_gain
        return f"Monster roars and gains extra health! Healed for {health_gain} points!"


def simulate_battle():
    
    warrior = Warrior("Warrior", 200, 30)
    mage = Mage("Mage", 150, 25)
    archer = Archer("Archer", 160, 35)
    monster = Monster("Monster", 300, 40)
    
    characters = [warrior, mage, archer]
    
    
    print("Battle begins!")
    
    
    for char in characters:
        print(char.attack(monster))
        print(char.special_move())
        print(char.attack(monster))
    
    
    for char in characters:
        print(monster.attack(char))
        print(monster.special_move())
    
    
    print("\nDemonstrating polymorphism with special moves:")
    for char in [warrior, mage, archer, monster]:
        print(char.special_move())

if __name__ == "__main__":
    simulate_battle()