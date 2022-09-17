"""3. Create a generator to produce first n even natural numbers"""
def evengenerator(n):
    num=1
    while n:
        yield num*2
        n-=1
        num+=1
    
a=int(input("enter a number \n"))
it= evengenerator(a)
for e in it:
    print(e,end=' ')
