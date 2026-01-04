# Module chứa Class , Function
class Calculator:
    def __init__ (self, name = "MyCalc"):       # Default 
        self.name = name
    def add (self, a, b):
        return a + b
    def __str__ (self):
        return f"Calculator: {self.name}"

def greet (name):
    return f"Hello, {name}"

# Global Var
PI = 3.14159
VERSION = "1.0.0"