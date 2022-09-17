"""3. Write a python script to update 2nd Question, change email and age to __email and
__age."""
class Profile:
    def __init__(self):
        self.name = "sunny"
        self.__email = "yahoo@gmail.com"
        self.__age = 21
    def set_name(self,name):
        self.name=name
    def set_email(self,email):
        self.__email=email
    def set_age(self,age):
        self.__age = age
        
    def get_name(self):
        return self.name
    def get_email(self):
        return self.__email
    def get_age(self):
        return self.__age
p1 = Profile ()
p1.set_name("ankit")
p1.set_email("google@gmail.com")
p1.set_age(29)
print(p1.get_name())
print(p1.get_email())
print(p1.get_age())
