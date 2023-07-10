#!/usr/bin/python3
import random

class GoldMine():
    pass

class Monster():

    spawn = 0
    monsters = []

    def __init__(self, name="Monster", level=1, XP=None, resistance=0):
        Monster.spawn += 1
        self.__name = name + "#" + str(Monster.spawn)
        self.__level = level
        self.__life = 30 + (level - 1) * 20
        self.__xp = level * random.randint(self.__life // 2, self.__life)
        self.__resistance = resistance + (5 * self.__level)
        self.__steal = False
        self.__is_alive = True
        Monster.monsters.append(self)
        print(f"{self.__name} has just spawned!")

    def attack(self, enemy):
        if self.is_alive() == False:
            return
        if enemy.is_alive() == True:
            print(f"{self.__name} attacks {enemy.get_name()}")
            damage = enemy.lose_life(self.__level * random.randint(11, 20))
            if self.is_steal():
                self.gain_life(damage // 2)

    def is_alive(self):
        return self.__is_alive
    
    def get_name(self):
        return self.__name
    
    def get_restistance(self):
        return self.__resistance
    
    def lose_life(self, val):
        if self.is_alive() == True:
            if self.__resistance > 99:
                self.__resistance = 100
            val = val * (100 - self.__resistance) // 100
            if val > self.__life:
                val = self.__life
            print(f"{self.__name} lost {val} life points!")
            self.__life -= val
            if self.__life == 0:
                self.__is_alive = False
                self.is_dead()
            return val
    
    def gain_life(self, val):
        if self.is_alive() == True:
            self.__life += val
            print(f"{self.__name} gained {val} life points!")
            return val
        
    def info(self):
        print(f"{self.__name}\nLP: {self.__life}\nLvl: {self.__level}\nRes : {self.__resistance}%")   

    def is_dead(self):
        Monster.spawn -= 1
        Monster.monsters.remove(self)
        print(f"{self.__name} is dead!")
    
    def get_xp(self):
        return self.__xp
    
    def set_steal(self):
        self.__steal = True
    
    def is_steal(self):
        return self.__steal
    
    def __str__(self):
        return self.__name
    
    @staticmethod
    def multiple_spawns(val):
        spawn_queue = []
        for i in range(val):
            name = "Monster"
            monster = Monster(name)
            spawn_queue.append(monster)
        return spawn_queue


class Weapon():
    def __init__(self, name, damage=0, wear=10):
        self.__name = name
        self.__damage = damage
        self.__wear = wear
        self.__isequipped = False
        self.__steal = False
        self.__coeff = 0
        self.__host = None

    def get_damage(self):
        return self.__damage

    def get_wear(self):
        return self.__wear

    def get_name(self):
        return self.__name

    def set_wear(self, val):
        self.__wear += val

    def is_equipped(self):
        return self.__isequipped
    
    def equip_status(self, val):
        self.__isequipped = val
    
    def get_host(self):
        return self.__host
    
    def set_host(self, val):
        self.__host = val
    
    def is_steal(self, val):
        self.__steal = True
        self.__coeff = val
        return self.__steal
    
    def get_coeff(self):
        if self.__steal == True:
            return self.__coeff
        return 0
    
    def __str__(self):
        return self.__name

    def destroy(self):
        print(f"{str(self)} is destroyed! {self.get_host()} is without weapon!")
        self.__isequipped = False
        self.__host = None


    def __del__(self):
        #print(f"{self.__name} just disappeared!")
        pass

class Dagger(Weapon):
    pass

class Hero():

    hero_number = 0
    hero_collection = []

    def __init__(self, name=None):
        self.__name = name
        self.__life = 100
        self.__weapon = None
        self.__coin = 0
        self.__level = 1
        self.__xp = 0
        self.__is_alive = True
        Hero.hero_number += 1
        Hero.hero_collection.append(self)
        print(f"{self.__name} created succesfully!")

    def is_alive(self):
        return self.__is_alive

    def info(self):
        print(f"{self.__name}\nLP: {self.__life}\nLvl: {self.__level}\nXP: {str(self.__xp)}")
        print(f"Coins: {self.__coin}\nWeapon: {str(self.__weapon)}")

    def gain_life(self, val):
        if self.is_alive() == True:
            self.__life += val
            print(f"{self.__name} gained {val} life points!")
            return val

    def lose_life(self, val):
        if self.is_alive() == True:
            if val > self.__life:
                val = self.__life
            print(f"{self.__name} lost {val} life points!")
            self.__life -= val
            if self.__life == 0:
                self.is_dead()
            return val

    def equip_weapon(self, weapon):
        if self.is_alive() == True:
            if weapon == None:
                self.__weapon = None
            elif weapon.is_equipped() == False:
                self.__weapon = weapon
                print(f"{self.__name} has now equipped a {str(weapon)}!")
                weapon.equip_status(True)
                weapon.set_host(self)
            else:
                print(f"Cannot equip. {weapon} already equipped to {weapon.get_host()}")

    def attack(self, enemy):
        if self.is_alive() == False:
            return
        if enemy.is_alive() == True:
            if self.__weapon is not None:
                if self.__weapon.get_wear() > 0:
                    print(f"{self.__name} attacks {enemy.get_name()} with {self.__weapon.get_name()}")
                    damage = enemy.lose_life(self.__weapon.get_damage() * self.__level)
                    self.gain_life(damage // 2)
                    if enemy.is_alive() == False:
                        self.gain_xp(enemy.get_xp())
                    self.__weapon.set_wear(-1)
                if self.__weapon.get_wear() == 0:
                    self.__weapon.destroy()
                    self.equip_weapon(None)
            else:
                print(f"No weapons! {self.__name} cannot attack!")
        else:
            print(f"{enemy.get_name()} already dead!")

    def get_name(self):
        return self.__name

    def get_weapon(self):
        return self.__weapon

    def is_dead(self):
        Hero.hero_number -= 1
        Hero.hero_collection.remove(self)
        self.__is_alive = False
        print(f"{self.__name} is dead!")

    def level_up(self, val=1):
        self.__level += val
        print(f"Congratulation! {self.__name} has reached level {self.__level}!")

    def gain_xp(self, val):
        self.__xp += val
        print(f"{self.__name} gained {val} XP!")
        if self.__xp // (self.__level * 100) > 1:
            self.level_up()
    
    def get_xp(self):
        return self.__xp

    def __str__(self):
        return self.__name

    def __del__(self):
        # if self.__is_alive == False:
        pass

    @classmethod
    def glob(cls):
        print("----------------------------")
        print(f"{Hero.hero_number} heroes")
        for hero in cls.hero_collection:
            hero.info()
            print("---")
        print("*********")
        print(f"{Monster.spawn} monsters are roaming around..")
        for monster in Monster.monsters:
            monster.info()
            print("---")
        print("----------------------------")
