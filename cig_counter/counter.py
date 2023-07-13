#!/usr/bin/python3
from myclasses import Pack, Smoker

smoker1 = Smoker("Boss")
pack1 = Pack("Camel", 38)
print(pack1)
smoker1.smoke(pack1)
smoker1.smoke(pack1)
smoker1.smoke(pack1)
print(pack1)