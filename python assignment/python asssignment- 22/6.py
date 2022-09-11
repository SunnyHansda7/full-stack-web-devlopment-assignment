"""6. Write a recursive python function to calculate the factorial of a number."""
def f1(num):
    if num==1:
        return 1
    
    return num*f1(num-1)
    
n=int(input("enter a number \n"))
r=f1(n)
print(r)
