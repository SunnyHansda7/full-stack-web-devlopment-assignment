"""2. Write a python script to create a user account class with 2 instance variables (userid
and balance). Create 3 user objects and add all the users using operator
overloading."""

class account:
   
    def __init__(self,user,bala):
        self.userid = user
        self.balance = bala
    #@staticmethod
    def __add__(self,other):
        total1 = self.userid + other.balance
        total2 =  self.userid +other.balance 
        #total3 = self.userid + other.userid 
        s4 = account(total1 + total2 )
        return s4
        

a1=account(1,50000)
a2=account(2,6000)
#a3=account()
s4 = (a1 + a2 )
print(s4)

        
