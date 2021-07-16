#----- @Read a particular line from file -------------

#define Filename and line to be read
def readFromFile(file_name,fileLine):

    #locate and open file -------------------------   
    file = open(file_name,'r')

    #hold all the lines after being read
    lines = list()

    #read all lines -----------------------------
    for lineNumber , content in enumerate(file):
        
        #add lines to container
         lines.append(lineNumber)

        #return disired line ---------------
         if lineNumber == fileLine:
            return(content)
    #feedback for non  existing lines
    if fileLine not in lines:
        return ("Line "+str(fileLine)+" Doesn't exist")
       
       


#----------------- OR ------------------



# ------------- @Read the entire file -------------

def readWHoleFile(file_name):
    file = open(file_name,'r')
    return file.read()       

 #test output --------------------------------------
 #print(readFromFile("testfile.txt",4))
 #print(readWHoleFile("testfile.txt"))

