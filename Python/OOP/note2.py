class Student:
    # EG
    # def __init__(self):
    #     print("Hello from constructor")
    # def Hello(self):
    #     print("Hello from object")
    # EG
    def __init__(self, id, name):
        self.name = name
        self.id = id
    def Hello(self):
        print(f"Hello from {self.name}")
    def __str__(self):
        return f"{self.name} [{self.id}]"

# Inheritance
# subclass for student
class chatGPTStudent(Student):
    def beDumb (self):
        print(f"I have no idea what you are talking about")

# s = Student("23BA12345", "Chou")
t = chatGPTStudent("23BA13579", "Dumber")

# s.Hello()
t.Hello()
# print(s)    # address (not) / return (use when have def str)

class Father:
    def drink(self):
        print("I'm drunk")
    def drive(self):
        print("I'm driving very fast")
class Mother:
    def cook(self):
        print("I'm preparing for dinner")
    def drive(self):
        print("I'm driving slooowwlyy")
    def drive(self, speed):
        print(f"I'm driving slooowwlyy {speed}")
class You(Father, Mother):
    def chatGPT(self):
        print("I'm dumb")

dumber = You()
dumber.chatGPT()
dumber.drink()
dumber.cook()
dumber.drive()