"""3. Write a python program to create 2 objects of the user class and assign different
values."""
class user:
    def __init__(self):
        self.name="sunny"
        self.age=21
        self.email="yahoo@gmail.com"
    def set(self,name):
       self.name=name
    def get(self):
       return self.name
        
user1=user()
user2=user()
user1.set("aman")
user2.set("ankit")
print(user1.get())
print(user2.get())
