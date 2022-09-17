"""10. Define a class Employee with instance object variables empid, name, salary. Write
__init__() method in the class to initialize instance object variables. Also define
instance methods to input fields and display field values"""
class Employee:
   
    def __init__(self):
        self.name="sunny"
        self.empid=21
        self.salary=15000
    def setfields(self,department):
        self.department=department
    def getfields(self):
        return self.department   
        
        
        
       
        
emp1=Employee()
emp1.setfields("software developer")
print(emp1.getfields())
