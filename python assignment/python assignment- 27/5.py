"""5.Write a python script to handle multiple Exception in one try"""
a=8
b=0
c=0
try:
    b=int(input("enter a number \n ")) #if user enter string give valueerror
    c=a//b
except ZeroDivisibleError:
    print("you cannot divide by zero")
except ValueError:
    print("enter a number only")
print(c)
