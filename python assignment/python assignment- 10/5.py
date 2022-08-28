"""5. Write a python script to print first N odd natural numbers in reverse order"""
for x in range(int(input("enter a number \n")),0,-1):
    if x%2!=0:
        print(x)
    
