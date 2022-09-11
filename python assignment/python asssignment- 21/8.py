"""8. Write a recursive python function to print cubes of first N natural numbers"""
def fun(num):
    
    if num>0:
       fun(num-1)
       print(num**3)
    
n=int(input("enter a number \n"))

fun(n)
