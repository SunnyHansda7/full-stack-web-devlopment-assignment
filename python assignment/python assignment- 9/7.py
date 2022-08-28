"""7. Write a python script to print first N even natural numbers in reverse order"""
i=int(input("enter a number \n"))
x=1
while x<=i:
    if i%2==0:
        
        print(i)
    i-=1
