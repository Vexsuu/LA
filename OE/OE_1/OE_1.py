

class hero():

    def __init__(self, name, role, dmg_type):

        self.name = name

        self.role = role

        self.dmg_type = dmg_type


    def describe(self):

         return f"{self.name} is {self.role} with a {self.dmg_type} power"

   

hero_mm = hero("claude", "marksman", "attack damage")

hero_exp = hero("yu zhong", "fighter", "attack damage")

hero_mid = hero("pharsa", "mage", "magic damage")

hero_jgl = hero("nolan","assassin", "attack damage")

hero_roam = hero("khaleed", "roam", "attack damage")

 

print(f'''

{hero_mm.name}

{hero_mm.role}

{hero_mm.dmg_type}

{hero_mm.describe()}


{hero_exp.name}

{hero_exp.role}

{hero_exp.dmg_type}

{hero_exp.describe()}


{hero_mid.name}

{hero_mid.role}

{hero_mid.dmg_type}

{hero_mid.describe()}


{hero_jgl.name}

{hero_jgl.role}

{hero_jgl.dmg_type}

{hero_jgl.describe()}


{hero_roam.name}

{hero_roam.role}

{hero_roam.dmg_type}

{hero_roam.describe()}


''')