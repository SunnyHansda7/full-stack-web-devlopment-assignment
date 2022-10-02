"""3.Write a python script to handle the ArithmeticError"""
try:
    a=3
    b=0
    c=a//b
    print(c)
except ArithematicError:
    print("number acanot divisible by zero")

