"""4. Write a recursive python function to calculate sum of squares of first N natural
numbers"""
def f1(num):
    if num==1:
        return 1
    
    return (num**2)+f1(num-1)
    
n=int(input("enter a number \n"))
r=f1(n)
print(r)
