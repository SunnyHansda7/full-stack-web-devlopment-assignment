"""2. Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not."""
def fun(num):
    
    i=1
    count=0
    while i<=num:
        
        if num%i==0:
           count=count+1
        i=i+1
    if count==2:
       print("number is prime")
    else:
       print("number is not prime")
       
    
    
n= int(input("enter a number \n"))
fun(n)
