"""4. Write a python script to calculate sum of first N odd natural numbers"""
a=int(input("enter a number \n"))
sum=0

for x in range(a):
    if x%2!=0:
        
        sum=sum+(x)
print(sum)
