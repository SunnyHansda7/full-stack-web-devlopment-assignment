"""10. Write a python script to print the octal equivalent of a given decimal number. (do not
use oct() method)"""
a=int(input("enter a three digit  number \n"))
sum=0
i=1

while a>0:
   
    last=a%8
    sum=sum+(last*i)
    a=a//8
    i=i*10
    
print(sum)
