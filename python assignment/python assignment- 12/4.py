"""4.Write a python script to print all Prime numbers between two given numbers (both
values inclusive)"""
a=int(input("enter a number \n"))
b=int(input("enter another number \n"))

for x in range(a,b+1):
    for i in(2,x+1):
        if(x%i==0):
            
            break
        
    else:
       print("number is prime",x)
    
