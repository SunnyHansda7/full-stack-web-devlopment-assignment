"""2. Write a python script to check whether a given number is Prime or not"""
a=int(input("enter a   number \n"))

if(a<2):
    print("not a prime number")
else:

    for x in range(2,a):
   
    
        if(a%x==0):
            print("given number  is not prime",a)
            break
        

    else:
        print("given number  is  prime",a)
