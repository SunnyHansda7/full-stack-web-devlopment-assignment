"""Write a python script to create a ArithmeticError"""
try:
    a=3
    b=0
    c =a//b
    print(c)
except ArithematicError:
    print("number acanot divisible by zero")
