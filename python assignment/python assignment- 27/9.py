"""9. Write a python script to raise a ValueError."""
a=8
b=0
c=0
try:
    b=int(input("enter a number \n ")) #if user enter string give valueerror
    if (b==a):
        raise ValueError()
    c=a//b
except ZeroDivisionError:
    print("you cannot divide by zero")
except ArithmeticError:
    print("number cannot be same")
except ValueError:
    print("enter a number only")
else:
    print(c)
