# --------- @ Remove content from file ----
# ------@ remove single content

def removeSingleContent(file_name):

    # open File ---------------
    file = open(file_name,'r+')

    del_line = int(input("Line number to delete: "))

    for line,content in enumerate(file):

        #del desired line --------------
        if del_line == line:
            print(content) #ensure that line is reached


      

# test output ---------------------
removeSingleContent("testfile.txt")
