from read_from_file import readLinesFrom

# Write to A file :: lines should be a list of strings --------------------------------------------
def writeLinesTo(file_name, lines):
    
     #locate and open file
     file = open(file_name,'w')

     #Addto file
     for line in lines:
        if line != '':
            file.write(line + "\n")
     file.close()


# Write a string to a particular line in a file (NB: the line number must exist, index starts at 0) ----------------------------------
def writeLineTo(file_name, lineNumber, line):
    lines = readLinesFrom(file_name)
    lines[lineNumber] = line
    writeLinesTo(file_name, lines)




# write a string to file (string will overwrite contents of file) :: use with caution --------------------------------------------------------------------
def writeContentTo(file_name,content):

     #locate and open file 
     file = open(file_name,'w')

     # #user input
     # content = input("add text here >    ")

     #Add content to file
     file.write(content+"\n")
     file.close()

# append a line of text at the end to a file --------------------------------------------------------------------------
def appendTo(file_name, line):
    file = open(file_name, 'a')
    file.write(line + "\n")
    file.close()



'''    
def add_several_items(file_name,content,number_of_items):

    #desired number of inputs to be made
    number_of_items = int(input("Number of items to add: "))

    while True:
        #open file
        file = open(file_name,'a')

        #user input
        content = input("add text here >    ")

        #Add user input to file
        file.write(content+"\n")

        number_of_items -= 1
        if number_of_items == 0:
            break

'''

#test output --------------------------------------
# file = "todo_database.sly"
# todos = readLinesFrom("testfile.sly")

# writeLinesTo(file, todos)
# print(readLinesFrom(file))

# writeLineTo(file, 2, "go for a sprint")
# print(readLinesFrom(file))

# appendTo(file, "complete the tasks above")
# print(readLinesFrom(file))