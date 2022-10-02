"""4. Write a Python script to store a list of city names in a file ‘cities.txt’"""
def write(filename,text):
    with open(filename,'a') as file:
        file.write(text)
#file.close()
