def writeToFile(file_name,content):

     #locate and open file -------------------------  
     file = open(file_name,'a')

     #user input
     content = input("add text here >    ")

     #Add user input to file
     file.write(content+"\n")

# OR --------------------
#enter the content directly
def writeToFile(file_name,content):
    
     #locate and open file -------------------------  
     file = open(file_name,'a')

     #Addto file
     file.write(content+"\n")


    
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

    

#test output --------------------------------------
#writeToFile("testfile.txt","content")

#add_several_items("testfile.txt","content",2)

#file = open("testfile.txt",'r')
#print(file.read())


