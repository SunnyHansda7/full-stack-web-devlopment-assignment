"""2. Create a generator to produce first n odd natural numbers"""

def naturalgenerator(n):
    num=1
    while n:
        yield 2*num-1
        n-=1
        num+=1
    
a=int(input("enter a number \n"))
it= naturalgenerator(a)
for e in it:
    print(e,end=' ')
