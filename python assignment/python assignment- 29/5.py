"""5. Write a Python script to append list of city names in a file ‘cities.txt’"""
def append(filename,text):
    with open(filename,'a') as file:
        file.write(text)
#file.close()
