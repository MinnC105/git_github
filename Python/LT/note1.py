'''
# import math
# math.pi
# math.pow(4, 2)  # floating point
# pow(4, 2)       # co gi khac
# math.sqrt(123)
# 3**(0.5)
# # python docs
# math.gcd(25, 5)
# gcd(25, 5)      # khong co

# ==============
import numpy as np
# a = np.array([1, 2, 3, 4])
# a.ndim          # 1
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a.ndim)          # 2 ?
np.sort(a, axist = 0)   # sort by column
np.sort(a, axist = 1)   # sort by row
# pip list
# pip install numpy
d = {"Duong": 32, "T": 4, "Dung": 24}
d.items()
sorted(d.items(), key = lambda i: i[1])  # sort theo value
# numpy co khac gi binh thuong khong ?
# array khong sort theo row, col duoc, con numpy cho them tinh nang ay
# EG
# map(function, iteration)
a = [4, 16, 9, 25]
def sqrt(n):
    return math.sqrt(n) 
map(sqrt, a)    # tao gi ?
list(map(sqrt, a))  # 2 4 3 5
# ap value vao function roi print ra

list(map(lambda _: _ + 2, a))  # 6 18 11 27
b = 9
# a = [4, 16, 9, 25]
a = 1 if b > 8 else 0   # a 1

# a = np.zeros(n)
'''

b = [1, 2, 3, 4]
c = b
c[0] = 0        # b, c deu thay doi
c = b.copy()    # c thay doi, b khong thay doi
c = b[::]       # c = b.copy()
