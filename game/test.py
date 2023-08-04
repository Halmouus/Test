#!/usr/bin/python3
from myclasses import *

hero1 = Hero("Disaster")
hero2 = Hero("Misty")
print (Hero.hero_names)
print (Hero.hero_collection)
print (Hero.hero_number)
name = input()
if name and name in Hero.hero_names:
    for h in Hero.hero_collection:
        if  h.name == name:
            h.info()
else:
    print("Not found!")