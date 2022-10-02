"""4. Write a python script to create two Threads. First thread will print all Even numbers
and Second thread will print all Odd numbers till 100."""
from threading import*
n=100
def even():
    i=2
    while(i<=n):
        if(i%2==0):
            print(i)
        i=i+1
           
def odd():    
    i=1
    while(i<=n):
        if(i%2!=0):
            print(i)
        i=i+1
t1=Thread(target=even())
print()
t1=Thread(target=odd())

    
