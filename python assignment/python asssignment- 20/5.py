"""5. Write a python program to create a function to find the Min of three numbers."""
def fun(a,b,c):
    if a<b:
        if a<c:
            
            print("A is MIn number",a)
                
    if b<a:
        if b<c:
            
                print("b is MIN number",b)
                
    if c<b:
        if c<a:
            
                print("c is MIN number",c)
                
    
    
a=int(input("enter a first number \n"))
b=int(input("enter a second number \n"))
c=int(input("enter a thirs number \n"))

fun(a,b,c) 
