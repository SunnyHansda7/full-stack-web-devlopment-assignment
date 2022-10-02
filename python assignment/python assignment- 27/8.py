"""8. Write a python script to implement try except and else block for division"""
a=8
b=0
c=0
try:
    b=int(input("enter a number \n ")) #if user enter string give valueerror
    c=a//b
except ZeroDivisionError:
    print("you cannot divide by zero")
except ValueError:
    print("enter a number only")
else:
    print(c)
