#!/usr/bin/python3
from myclasses import Pack, Smoker

smoker1 = Smoker("Boss")
pack1 = Pack("LM Blue", 27)
print(pack1)
print(pack1.smoke())
print(pack1.smoke())
print(pack1.smoke())
print(pack1)