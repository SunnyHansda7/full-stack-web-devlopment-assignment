"""4.Write a python script to handle a ValueError"""
a=8
b=0
c=0
try:
    b=int(input("enter a number \n ")) #if user enter string give valueerror
    c=a//b
    
except ValueError:
    print("enter a number only")
print(c)
