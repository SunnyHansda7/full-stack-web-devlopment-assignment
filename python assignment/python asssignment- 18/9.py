"""9. Write a python program to merge two python dictionaries into one dictionary."""
info={"name":'ankit',"age":23,"gender":'male'}
detail={"names":'aman',"ages":25,"genders":'male'}
#info.merge(detail)
for e in detail:
    info[e]=detail[e]
    
print(info)
