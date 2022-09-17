"""5. Write a python script to create a Calculator class with 2 methods for adding and
subtracting 2 values."""
class Calculator:
    @staticmethod
    def add(a,b):
       return a+b
    @staticmethod
    def subtract(c,d):
        return c-d
    
p1 = Calculator()

print(p1.add(9,4))
print(p1.subtract(7,4))

