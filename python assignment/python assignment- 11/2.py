"""2. Write a python script to calculate sum of squares of first N natural numbers"""
a=int(input("enter a number \n"))
sum=0
x=1
for x in range(a):
    sum=sum+((x+1)**2)
print(sum)
    
