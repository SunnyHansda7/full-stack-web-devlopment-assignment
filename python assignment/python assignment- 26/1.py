"""1. Write a python script to multiple 2 or 3 or 4 numbers with a single multiply method in
a class using method overloading."""
class multiply:
    @staticmethod
    def multi(a,b=None,c=None,d=None):
        if b==None and c==None and d==None:
            return a
        if  c==None and d==None:
            return a*b
        if d==None:
            return a*b*c
        return a*b*c*d
a=int(input("enter a number \n"))
b=int(input("enter a number \n"))
c=int(input("enter a number \n"))
d=int(input("enter a number \n"))
m1=multiply()
print(m1.multi(a,b,c,d))
        
