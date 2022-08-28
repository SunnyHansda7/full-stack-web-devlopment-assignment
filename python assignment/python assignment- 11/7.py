"""7. Write a python script to count digits in a given number
"""
a=int(input("enter a three digit  number \n"))
count=0

while a>0:
   
    a=a//10
    count+=1
    
    
print(count)
