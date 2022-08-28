"""2. Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division"""
a=int(input("enter a first  number \n"))
b=int(input("enter second number \n"))
print("Enter 1  for Adition \n")
print("Enter 2  for  Subtraction \n")
print("Enter 3  for  Multiplication \n")
print("Enter 4  for Division \n")
c=int(input("enter any  number given above to perform  \n"))
match c:
     case 1:
        s=a+b
        print(s)
     case 2:
        c=a-b
        print(c)
     case 3:
        print(a*b)
     case 4:
        print(a/b)
     case _:
        print("default")
    
        
