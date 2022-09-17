"""2. Write a python script to update the above Profile class with encapsulation."""
class Profile:
    def __init__(self):
        self.name = "sunny"
        self.email = "yahoo@gmail.com"
        self.age = 21
    def set_name(self,name):
        self.name=name
    def set_email(self,email):
        self.email=email
    def set_age(self,age):
        self.age = age
        
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_age(self):
        return self.age
p1 = Profile ()
p1.set_name("ankit")
p1.set_email("google@gmail.com")
p1.set_age(29)
print(p1.get_name())
print(p1.get_email())
print(p1.get_age())
