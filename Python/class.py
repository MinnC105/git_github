class person:
    def print(self):
        print("Name:", self.name)
        print("Age:", self.age)
    def __init__(self, n, a):
        self.name = n
        self.age = a