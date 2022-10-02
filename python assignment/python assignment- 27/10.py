"""10. Write a python script to implemented a nested Try Except block"""
a=8
b=0
c=0
try:
    print("outer try block")
    try:
        print("inner try block")
    except :
        print("inner except block")
    finally:
        print("inner finally block")
 
except :
    print("outer except block")

finally:
    print("outer finally lock")
