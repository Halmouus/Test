#!/usr/bin/python3
import inspect
from myclasses import *

classes = [name for name in dir() if inspect.isclass(globals().get(name, None)) and issubclass(globals()[name], Weapon)
           and (globals()[name] != Weapon)]
print(classes)
for cl in classes:
    print(cl)
