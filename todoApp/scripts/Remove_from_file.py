# --------- @ Remove content from file ----
# ------@ remove single content

from os import write


def removeSingleContent(file_name):

    # open File ---------------
    file = open(file_name,'r+')

    #line to be deleted ie content to remove
    del_line = int(input("Line number to delete: "))

    #read all file lines into list
    file_lines = file.readlines()

    #compare line to be deleted and file_lines
    for line , item in enumerate(file_lines):
        if del_line == line:
            file_lines.remove(item)
            file.close

    
    #Write modified lines back to file
    file = open(file_name,'w')
    for i in file_lines:
        file.write(i)
        file.close

# -------- @test output

print(removeSingleContent("testfile.txt"))