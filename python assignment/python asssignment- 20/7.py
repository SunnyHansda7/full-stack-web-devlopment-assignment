"""7. Write a python program to access a function inside a function."""
def fun(num):
    
    if num==1:
        return 1
    
    l= num+fun(num-1)
    return l
            

n=int(input("enter a number \n"))

r=fun(n)
print(r)
