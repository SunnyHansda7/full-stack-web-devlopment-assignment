"""6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
and division of 2 values and inherit it from the Calculator class."""
class Calculator:
    @staticmethod
    def add(a,b):
       return a+b
    @staticmethod
    def subtract(c,d):
        return c-d
    
class Calculator2_0(Calculator):
    @staticmethod
    def multiply(a,b):
       return a*b
    @staticmethod
    def divide(c,d):
        return c/d
    
    
    
p1 = Calculator()
p2=Calculator2_0()


print(p1.add(9,4))
print(p1.subtract(7,4))

print(p2.multiply(9,4))
print(p2.divide(7,4))
