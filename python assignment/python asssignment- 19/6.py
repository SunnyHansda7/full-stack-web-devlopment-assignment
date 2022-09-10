"""6. Write a python program to create a function that finds a maximum of four numbers."""
def fun(a,b,c,d):
    if a>b:
        if a>c:
            if a>d:
                print("A is greater number",a)
                
    if b>a:
        if b>c:
            if b>d:
                print("b is greater number",b)
                
    if c>b:
        if c>a:
            if c>d:
                print("c is greater number",c)
                
    if d>b:
        if d>c:
            if d>a:
                print("d is greater number",d)
                
    
a=int(input("enter a first number \n"))
b=int(input("enter a second number \n"))
c=int(input("enter a thirs number \n"))
d=int(input("enter a fourth number \n")) 
fun(a,b,c,d) 
