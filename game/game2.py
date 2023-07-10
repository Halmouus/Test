#!/usr/bin/python3
from myclasses import Hero, Weapon, Monster, Dagger, GoldMine

sword = Weapon("Sword", 5)
hammer = Weapon("Hammer", 30)
hero1 = Hero("Hero 1")
hero2 = Hero("Hero 2")
hammer.is_steal(50)
print(hammer.get_coeff())
hero1.equip_weapon(hammer)
spawns = Monster.multiple_spawns(18)
Hero.glob()
for monster in spawns:
    hero1.attack(monster)
    monster.attack(hero1)
Hero.glob()