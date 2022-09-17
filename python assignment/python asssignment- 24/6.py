"""6. Write a python program to create 3 user objects and find the youngest of all."""
class user:
    def __init__(self):
        self.name="sunny"
        self.age=21
        self.email="yahoo@gmail.com"
        
        
    def set(self,age):
       self.age=age
    def get(self):
       return self.age
        
user1=user()
user2=user()
user3=user()

user1.set(22)
user2.set(24)
user3.set(19)
if(user1.get()>user2.get()):
    if(user1.get()>user3.get()):
        print(user1.get())
if(user2.get()>user1.get()):
    if(user2.get()>user3.get()):
        print(user2.get())
if(user3.get()>user2.get()):
    if(user3.get()>user1.get()):
        print(user3.get())

#print(user1.age)
