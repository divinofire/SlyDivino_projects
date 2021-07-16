# ------------ @ Write User input to File -------------

# --------@ Write to just one line

#define file to be written to 
# define the content(users input) to be written to the file
def writeToFile(file_name):

     #locate and open file -------------------------  
     file = open(file_name,'a')

     #user input
     content = input("add text here >    ")

     #Add user input to file
     file.write("\n"+content)
     file.close()

# ------------------ OR --------------------

# -----------@ Write to several lines

def LinesToFile(file_name):

      #open file
     file = open(file_name,'a+')
     
     #lines to add
     NumberOfLines = int(input("Number of lines to add: "))

     while True:
       
        #user input
        content = input("add text here >    ")

        #Add user input to file
        file.write("\n"+content)
        file.close()

        NumberOfLines -= 1
        if NumberOfLines == 0:
            break

    

#test output --------------------------------------
#writeToFile("testfile.txt")

LinesToFile("testfile.txt")
