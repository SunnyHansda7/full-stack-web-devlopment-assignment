"""10. Write a python program to create a function to check whether a given number is even
or odd."""
def fun(n):
    if n%2==0:
        return print("even number")
    else:
        return print("odd number")
a=int(input("enter a number \n"))    
fun(a)
