"""3. Write a python program to create a function that prints the even numbers from a
given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]"""
def fun(n):
    for i in n:
        if i%2==0:
            print("number is even",i)
            

List=[1, 2, 3, 4, 5, 6, 7, 8, 9]
fun(List)
