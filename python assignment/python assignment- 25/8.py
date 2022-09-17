"""8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and
Phone Class."""
class Phone:
    @staticmethod
    def calling():
        print("calling.........")
    @staticmethod
    def SMS():
        print("SMS.....")
        
class Calculator2_0:
    @staticmethod
    def multiply(a,b):
       return a*b
    @staticmethod
    def divide(c,d):
        return c/d


class SmartPhone(Phone,Calculator2_0):
     @staticmethod
     def smart_calling():
        print("smart_calling.........")
    




sm1=SmartPhone()
print(sm1.smart_calling())


ph1=Phone()
ph1.calling()
ph1.SMS()

p2=Calculator2_0()
print(p2.multiply(9,4))
print(p2.divide(7,4))
