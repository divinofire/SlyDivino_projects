

# remove a EOL character a the end of a string of text
def remove_new_line_char(line):
    if (line[-1] == "\n") or (line == "\r"):  #check if last item of line is the \n character for windows or \r for linux
            return(line[:-1]) # return all but the last character of the line 
    else:
        return line


# read all lines from file----------------------------------------------------------------------------
def readLinesFrom(file_name):
    
    #locate and open file -------------------------   
    file = open(file_name,'r')

#   #read and return all lines as a list, one line per list item -----------------
    lines = file.readlines()

    #remove empty lines -----------------------------
    lines = [line for line in lines if line != "\n"]

    #remove \n at the end of each line-------------------------
    clean_lines = []                
    for line in lines:               
        clean_lines.append(remove_new_line_char(line))


#   for content in enumerate(file):

#         #return first line
#         #if lineNumber == 0:
#         #    return(content)
#         return content
    
       #close file and return lines (it's very important to close files to prevent possible file corruption)
    file.close()
    return clean_lines

# #test output --------------------------------------
#print(readLinesFrom("testfile.sly"))

# read a particular line from file (line number starts at 0)
def readLineFrom(file_name, lineNumber): 

    # lineNumber may be out of index, return empty string if any exception occurs
    try:
        line = readLinesFrom(file_name)[lineNumber]
        return line
    except:
        return ''


# test output ----------------------------------

#print(readLineFrom("testfile.sly", 2))