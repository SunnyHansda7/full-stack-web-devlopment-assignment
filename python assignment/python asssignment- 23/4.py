"""4. Create a generator to produce squares of first N natural numbers"""
def naturalgenerator(n):
    num=1
    while n:
        yield num**2
        n-=1
        num+=1
    
a=int(input("enter a number \n"))
it= naturalgenerator(a)
for e in it:
    print(e,end=' ')
