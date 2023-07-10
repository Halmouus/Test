#!/usr/bin/python3
from myclasses import Hero, Weapon, Monster

sword = Weapon("Sword", 5)
hammer = Weapon("Hammer", 100)
hero1 = Hero("Hero 1")
hero2 = Hero("Hero 2")
hero1.equip_weapon(hammer)
spawns = Monster.multiple_spawns(10)
Hero.glob()
for monster in spawns:
    hero1.attack(monster)
    monster.attack(hero1)
Hero.glob()