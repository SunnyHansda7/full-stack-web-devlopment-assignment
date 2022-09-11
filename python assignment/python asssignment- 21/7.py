"""7. Write a recursive python function to print squares of first N natural numbers"""
def fun(num):
    
    if num>0:
       fun(num-1)
       print(num**2)
    
    
           
        
n=int(input("enter a number \n"))

fun(n)
