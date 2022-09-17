"""6. Create a generator to produce first n prime numbers"""
def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
        return True
def primegenerator(n):
    num=2
    while n:
        if isprime(num):
            yield num
            n-=1
        num+=1
    return
a=int(input("enter a number \n"))
it= primegenerator(a)
for e in it:
    print(e,end=' ')
