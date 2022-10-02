"""6. Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or
not"""

def read(filename):
    with open(filename,'r') as file:
       print( file.read())
    
def search(filename,word):
    try:
        file = open(filename,'r')
        line_count=0
        for line in file.readlines():
            line_count+=1
            strlist = line.split(' ')
            word_count=0
            for w in strlist:
                word_count+=1
                if word==w:
                    return(line_count,word_count)
        else:
            return None
        file.close()
    except FileNotFoundError:
        print("File not found")
    
