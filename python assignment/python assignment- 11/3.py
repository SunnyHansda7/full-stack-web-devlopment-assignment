"""3. Write a python script to calculate sum of cubes of first N natural numbers"""
a=int(input("enter a number \n"))
sum=0
x=1
for x in range(a):
    sum=sum+((x+1)**3)
print(sum)
