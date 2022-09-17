"""7. Write a python script to create a Phone class with 2 methods to print the features
(calling and sms)."""
class Phone:
    @staticmethod
    def calling():
        print("calling.........")
    @staticmethod
    def SMS():
        print("SMS.....")
ph1=Phone()
ph1.calling()
ph1.SMS()
