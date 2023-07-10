#!/usr/bin/python3
class Weapon():
    def __init__(self, name, damage=0, wear=10):
        self.__name = name
        self.__damage = damage
        self.__wear = wear
    
    def get_damage(self):
        return self.__damage
    
    def get_wear(self):
        return self.__wear
    
    def get_name(self):
        return self.__name
    
    def set_wear(self ,val):
        self.__wear += val
    
    def __del__(self):
        print(f"{self.__name} just disappeared!")


class Hero():

    hero_number = 0
    hero_collection = []

    def __init__(self, name=None):
        self.__name = name
        self.__life = 100
        self.__weapon = None
        self.__coin = 0
        self.__is_alive = True
        Hero.hero_number += 1
        Hero.hero_collection.append(self)
        print(f"{self.__name} created succesfully!")

    def is_alive(self):
        return self.__is_alive
    
    def info(self):
        print(f"{self.__name}\nLP: {self.__life}\nCoins: {self.__coin}")

    def gain_life(self, val):
        if self.is_alive() == True:
            self.__life += val
            print(f"{self.__name} gained {val} life points!")

    def lose_life(self, val):
        if self.is_alive() == True:
            if val > self.__life:
                val = self.__life
            print(f"{self.__name} lost {val} life points!")
            self.__life -= val
            if self.__life == 0:
                self.__is_alive = False
                self.__del__()
    
    def equip_weapon(self, weapon):
        if self.is_alive() == True:
            self.__weapon = weapon
    
    def attack(self, enemy):
        if enemy.is_alive() == True:
            if self.__weapon is not None:
                if self.__weapon.get_wear() > 0:
                    print(f"{self.__name} attacks {enemy.get_name()} with {self.__weapon.get_name()}")
                    enemy.lose_life(self.__weapon.get_damage())
                    self.__weapon.set_wear(-1)
                if self.__weapon.get_wear() == 0:
                    self.__weapon.__del__()
                    self.equip_weapon(None)
        else:
            print(f"{enemy.get_name()} already dead!")
    
    def get_name(self):
        return self.__name
    
    def __del__(self):
        #if self.__is_alive == False:
            Hero.hero_number -= 1
            Hero.hero_collection.remove(self)
            print(f"{self.__name} is dead!")

    @classmethod
    def glob(cls):
        print("----------------------------")
        print(f"{Hero.hero_number} of heroes")
        for hero in cls.hero_collection:
            hero.info()
        print("----------------------------")

                
sword = Weapon("Sword", 5)
hero1 = Hero("Hero 1")
hero2 = Hero("Hero 2")
Hero.glob()

hero1.gain_life(20)
hero1.equip_weapon(sword)
hero1.attack(hero2)
hero1.attack(hero2)
hero1.attack(hero2)
hero1.attack(hero2)
hero1.attack(hero2)
hero1.attack(hero2)
hero1.attack(hero2)
hero1.attack(hero2)
hero1.attack(hero2)
hero1.attack(hero2)
hero1.attack(hero2)
hero1.attack(hero2)
hero1.attack(hero2)
Hero.glob()