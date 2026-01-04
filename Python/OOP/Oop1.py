class Animal:   
    def __init__ (self, name, age):
        self.__name = name
        self.__age = age
        # print(f"Animal {name} created")
    # Getter and Setter
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age

    # Check
    def __lt__ (self, other):
        return self.__age < other.__age
    
    # Cách 1: print(f"{dog2}")
    # def __str__ (self):
    #     return f"Name: {self.__name} Age: {self.__age}"
    # Cách 2
    def display(self):
        print(f"Name: {self.__name} Age: {self.__age}")

# Inheritance
class Dog (Animal):
    # Cách 1: override __init__ → cần super() 
    # def __init__ (self, name, age, breed):
    #     super().__init__(name, age)      # gọi __init__ của animal
    #     self.__breed = breed
    #     print(f"Dog {self.get_name()} ({breed}) created")
    # Cách 2: không override, dùng luôn __init__ cha (chỉ được thêm attribute mới vào method)
    def set_breed(self, breed):
        # tham số use for current method, unchanged; self.name (attribute) use for all object, changed
        # Cách 1: print dùng tham số breed, rồi define self.__breed = breed
        # Cách 2: define self.__breed = breed trước thì trong print dùng self.__breed
        print(f"Dog {self.get_name()} ({breed}) created")
        self.__breed = breed
    def bark (self, n):
        print(f"{self.get_name()} says: " + "woof " * n)
# Multiple Inheritance

# dog1 = Dog("Begge", 10, "Black")
dog1 = Dog("Begge", 10)
dog1.set_breed("Grey")
dog1.display()
print(dog1)     # print(f"{dog1}")

# dog2 = Dog("Husky", 5, "Pink")
dog2 = Dog("Husky", 5)
dog2.set_breed("Grey")
# print(f"{dog2}")
dog2.set_breed("Grey")
# print(f"dog1 < dog2 ? : {dog1 < dog2}")
# dog1.bark(3)

# Checking
# print(f"dog1 is Dog: {isinstance(dog1, Dog)}")
# print(f"dog1 is Animal: {isinstance(dog1, Animal)}")
# print(f"Dog is Animal: {issubclass(Dog, Animal)}")
# print(f"Animal is Dog: {issubclass(Animal, Dog)}")
