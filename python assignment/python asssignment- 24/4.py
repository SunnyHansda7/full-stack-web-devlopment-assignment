"""4. Write a python program to init default values for user object using __init__ method."""
class user:
    def __init__(self):
        self.name="sunny"
        self.age=21
        self.email="yahoo@gmail.com"
        print("hello")
    def set(self,name):
       self.name=name
    def get(self):
       return self.name
        
user1=user()
user2=user()
