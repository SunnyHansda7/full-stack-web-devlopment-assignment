"""8. Write a python script to calculate sum of digits of a given number"""
a=int(input("enter a three digit  number \n"))
sum=0

while a>0:
   
    last=a%10
    sum=sum+last
    a=a//10
    
    
print(sum)
