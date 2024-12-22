class Sinampalukan:
    def __init__(self, chicken, onion, luya, sgmix):
        self.__chicken= chicken
        self.__onion = onion
        self.__luya = luya
        self.__sgmix = sgmix 
    def __str__(self):
        return f"My Sinampalukan has {self.__chicken}, {self._onion}, and {self.__luya}, and most important of all {self.__sgmix}"
        
gsa = Sinampalukan("Chicken", "red onion", "luya", "sgmix")


print(gsa.__onion)