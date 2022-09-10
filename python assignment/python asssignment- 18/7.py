"""7. Write a python program to create three dictionaries, then create one dictionary that
will contain the other three dictionaries."""
information={"name":'sunny',"age":21,"gender":'male'}
info={"name":'ankit',"age":23,"gender":'male'}
detail={"name":'aman',"age":25,"gender":'male'}
d1={}
d1[101]=information
d1[102]=info
d1[103]=detail
print(d1)
