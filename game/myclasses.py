class weapon():
    def __init__(self, damage=0):
        self.__damage = damage
    
    def get_damage(self):
        return self.__damage


class hero():

    def __init__(self, name=None):
        self.__name = name
        self.__life = 100
        self.__weapon = None
        self.__coin = 0

    def gainLife(self, val):
        self.__life += val
        print(f"{__self.name} gained {val} life points!")ِ

    def loseLife(self, val):
        print(f"{__self.name} lost {val} life points!")ِ
        self.__life -= val
    
    def equip(self, weapon):
         self.__weapon = weapon
    
    def attack(self, enemy, weapon):
        enemy.loseLife(weapon.get_damage())
                