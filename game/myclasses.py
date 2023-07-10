#!/usr/bin/python3
class Weapon():
    def __init__(self, name, damage=0):
        self.__name = name
        self.__damage = damage
    
    def get_damage(self):
        return self.__damage
    
    def get_name(self):
        return self.__name


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
    
    def info(self):
        print(f"{self.__name}\nLP: {self.__life}\nCoins: {self.__coin}")

    def gain_life(self, val):
        self.__life += val
        print(f"{self.__name} gained {val} life points!")

    def lose_life(self, val):
        if val > self.__life:
            val = self.__life
        print(f"{self.__name} lost {val} life points!")
        self.__life -= val
        if self.__life == 0:
            self.__is_alive = False
            self.__del__()
    
    def equip_weapon(self, weapon):
         self.__weapon = weapon
    
    def attack(self, enemy):
        print(f"{self.__name} attacks {enemy.get_name()} with {self.__weapon.get_name()}")
        enemy.lose_life(self.__weapon.get_damage())
    
    def get_name(self):
        return self.__name
    
    def __del__(self):
        if self.__is_alive == False:
            Hero.hero_number -= 1
            #Hero.hero_collection.remove(self)
            print(f"{self.__name} is dead!")

    @classmethod
    def glob(cls):
        print("----------------------------")
        print(f"{Hero.hero_number} of heroes")
        for hero in cls.hero_collection:
            hero.info()
        print("----------------------------")

                
sword = Weapon("Sword", 30)
hero1 = Hero("Hero 1")
hero2 = Hero("Hero 2")
Hero.glob()

hero1.gain_life(20)
hero1.equip_weapon(sword)
hero1.attack(hero2)
hero1.attack(hero2)
hero1.attack(hero2)
hero1.attack(hero2)
Hero.glob()