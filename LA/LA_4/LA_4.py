print("LA_4")

class Hero:
    def __init__(self, hero, role):
        self.hero = hero
        self.role = role
    
    def __str__(self):
        return f"{self.hero}{self.role}"
        
h1 = Hero("Ember ", "is a Midlane Carry")

print(h1)