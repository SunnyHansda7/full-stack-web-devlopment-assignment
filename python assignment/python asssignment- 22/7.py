"""7. Write a recursive python function to calculate sum of the digits of a given number"""
def f1(num):
    if num==0:
        return 0
    
    return num%10+f1(num//10)
    
n=int(input("enter a number \n"))
r=f1(n)
print(r)
