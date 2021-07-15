
def readFromFile(file_name):
    
    #locate and open file -------------------------   
    file = open(file_name,'r')

    #read and return desired line -----------------
    for lineNumber , content in enumerate(file):

        #return first line
        if lineNumber == 0:
            return(content)
    
    #close file
    file.close

#test output --------------------------------------
print(readFromFile("testfile.txt"))
