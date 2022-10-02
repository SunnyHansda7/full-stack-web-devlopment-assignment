"""Write a python script to print all Prime numbers under 100"""
a=100

if(a<2):
    print("not a prime number")
else:

    for x in range(2,a):
   
        for i in range(2,x):
            if(x%i==0):
               
                break
      

        else:
            print("given number  is  prime",x)
