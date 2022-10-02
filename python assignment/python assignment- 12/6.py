"""6. Write a python script to print first N prime numbers"""
a=int(input("enter a number \n"))
for x in range(2,a):
    for i in(2,x):
        if(x%i==0):
            
            break
        
        else:
           print("number is prime",x)
    
