class AnimeCharacter: #LA23
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def wrapper(*args, **kwargs):
            print("Introducing...")
            func(*args, **kwargs)
            print("He is amazing!")
        return wrapper

ippo = AnimeCharacter("Ippo Makunouchi", "Dempsey Roll")

@ippo.introduce  
def character_intro():
    print(f"{ippo.name} is using his {ippo.ability}.")

character_intro()