"""Write a Python script to create a list of first N odd natural numbers."""
n=int(input("enter how many odd natural number you want to print \n"))
list_natural_number=[ i for i in range(1,n*2) if(i%2 !=0)]
    
print(list_natural_number)
