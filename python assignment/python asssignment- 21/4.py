"""4. Write a recursive python function to print first N odd natural numbers in reverse order"""
def fun(num):
    if num>0:
       
        if (num%2)!=0:
            print(num)
            
        fun(num-1)
           
        
n=int(input("enter a number \n"))

fun(n)
