# import full module
# Cách 1
# from .func import *       # không nên dùng, không cần "func."
# c = Calculator()
# # c = Calculator("Basic")
# print(c.add(5, 3))
# print(f"{c}")
# print(greet("Alice"))
# print(PI)

# Cách 2
# import Module.Mod1.func as f
# c = f.Calculator()
# print(f.greet("Alice"))
# print(f.PI)

# import particular module
# from .func import PI
# print(PI)
from .func import Calculator, greet
c = Calculator()
print(c.add(5, 3))
print(f"{c}")
print(greet("Alice"))

"""
. : file main cùng folder con với func (Mod1)
.. : file main nằm ở folder con khác (Mod2)
không cần : file main nằm ở folder parent 
"""
# main ở folder con thì python -m Module.Mod1.main1
# cần tạo file empty __init__.py = tạo package