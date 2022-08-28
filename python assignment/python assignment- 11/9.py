"""9. Write a python script to print binary equivalent of a given decimal number. (do not
use bin() method)"""
a=int(input("enter a three digit  number \n"))
sum=0
i=1

while a>0:
   
    last=a%2
    sum=sum+(last*i)
    a=a//2
    i=i*10
    
print(sum)
