""" tree /F
├───Draft
└───Module              
    │   main.py
    │
    ├───Mod1            # Package 1
    │       func.py     # Muốn import
    │       main1.py
    │
    └───Mod2            # Package 2
            main2.py
"""
# khác package: from ..package.module     
from ..Mod1.func import greet
print(greet("Alice"))
# import Module.Mod1.func as m
# print(m.greet("Alice"))


