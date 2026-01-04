# Wild
class Animal:   
    def __init__ (self, name, age):
        self.__name = name
        self.__age = age
        print(f"Animal {name} created")
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    def display(self):
        print(f"Name: {self.__name} Age: {self.__age}")
# Having owner
class Pet:
    def __init__ (self, owner_name):
        self.__owner_name = owner_name
        print(f"Pet having owner: {owner_name}")
    def get_owner(self):
        return self.__owner_name
    def set_owner (self, owner_name):
        self.__owner_name = owner_name
    def display(self):
        print(f"Owner: {self.__owner_name}")
# Multiple Inheritance
class Dog (Animal, Pet): 
    def __init__ (self, name, age, owner_name, breed):
        Animal.__init__ (self, name, age)
        Pet.__init__ (self, owner_name)      
        self.__breed = breed
        print(f"Created !")

    def bark (self, n):
        print(f"{self.get_name()} says: " + "woof " * n)
    def __str__ (self):
        return f"Dog: {self.get_name()}, Breed: {self.__breed} Age: {self.get_age()} Owner: {self.get_owner()}"
    
    # 2 display thì sẽ bị redefine = display sau
    def display(self):
        print("=== Dog Display ===")
        # Animal.display() 
        super().display()
        # Pet.display()
        super(Animal, self).display()  # skip Animal, gọi Pet.display() 
    # Method overrided
    def display(self):
        super().display()   # gọi theo thứ tự MRO của Dog [Animal, Pet]
        print("Overrided !")

dog1 = Dog("Begge", 10, "Min", "Black")
dog1.display()
dog1.bark(3)

# muốn display như ban đầu thì nnao ? 
# nếu không override display() trong Dog, vẫn có thể gọi trực tiếp display() trong Pet, Animal
dog1.display()  # lấy từ Animal
Animal.display(dog1)
Pet.display(dog1)

# print(f"{dog1}")
# print(dog1)

