"""2. Write a Python script to create a new file ‘myfile.txt’ and store user entered text."""
file = open('myfile.txt','w')
b=input("enter text here \n")
file.write(b)
file.close()
