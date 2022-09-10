"""3. Write a python program to reverse the tuple."""
tuple1=(1,2,3,4,5,6)
l=list(tuple1)
list.reverse(l)
tuple1=tuple(l)
print("print reverse tuple :",tuple1)
