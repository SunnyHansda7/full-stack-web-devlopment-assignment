"""1. Write a Python script to print the following status of a file:
a. Whether a file is read onsly
b. Whether a file is closeds or not
c. Which file opening mode is used
d. Name of the file"""
file =open('test.txt','w')
file.write("a. Whether a file is read only \n")
file.close()
