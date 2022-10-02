"""8. Write a python script to print first N terms of a Fibonacci series"""
n=int(input("enter a number \n"))
a=0
b=1
for x in range(n):
    s=a+b
    print("N terms of a Fibonacci series",s)
    a=b
    b=s
    
    
    
