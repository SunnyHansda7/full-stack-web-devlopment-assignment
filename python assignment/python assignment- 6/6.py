"""6. Write a python script to check whether a given number is a three digit number or not"""
a=int(input("enter a number \n"))
count=0
while a>0:
    a=a//10
    count=count+1
    if count<3:
        print(" number is a three digit number",count)
else:
     print(" number is not a three digit number")
