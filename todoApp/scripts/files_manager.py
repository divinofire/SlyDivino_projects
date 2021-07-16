import os
import shutil

class FileManager:
	#file_name = file_name
	# create folder -------------------------------------------------------------------------------
	def __init__(self):
		pass

	# create folder -------------------------------------------------------------------------------
	def create_folder(self,folder_name):
		try:
			os.mkdir(folder_name)
			return True
		except:
			return False

	# create_file------------------------------------------------------------------------------------


	def create_file(self,file_name):
		try:
			file = open(os.path.join(file_path, ), "w")
			file.close()
			return True
		except:
			return False


	#delete a file -----------------------------------------------------------------------------------
	def delete_file(self,file_name):
		try:		
			os.remove(file_name)
			return True
		except:
			return False

	#delete a folder ----------------------------------------------------------------------------------
	def delete_folder(self, folder_name):
		try:
			shutil.rmtree(folder_name)
			return True
		except:
			return False


	# remove a EOL character a the end of a string of text ---------------------------------------------
	def remove_new_line_char(self, line):
		#check if last item of line is the \n character for windows or \r for linux
	    if (line[-1] == "\n") or (line == "\r"): 
	            return(line[:-1]) # return all but the last character of the line 
	    else:
	        return line


	# read all lines from file----------------------------------------------------------------------------
	def readLinesFrom(self, file_name):
	     
	    # open file in read mode
	    file = open(file_name,'r')

	#   #read and return all lines as a list, one line per list item 
	    lines = file.readlines()

	    #remove empty lines 
	    lines = [line for line in lines if line != "\n"]

	    #remove \n at the end of each line
	    clean_lines = []                
	    for line in lines:               
	        clean_lines.append(self.remove_new_line_char(line))
	    
	     #close file and return lines (it's very important to close files to prevent possible file corruption)
	    file.close()
	    return clean_lines

	# read a particular line from file (line number starts at 0)--------------------------------------------------------
	def readLineFrom(self, file_name, lineNumber): 

	    # lineNumber may be out of index, return empty string if any exception occurs
	    try:
	        line = self.readLinesFrom(file_name)[lineNumber]
	        return line
	    except:
	        return ''

	# Write to A file :: lines should be a list of strings --------------------------------------------
	def writeLinesTo(self, file_name, lines):
	    
	     #locate and open file
	     file = open(file_name,'w')

	     #Addto file
	     for line in lines:
	        if line != '':
	            file.write(line + "\n")
	     file.close()


	# Write a string to a particular line in a file (NB: the line number must exist, index starts at 0) ----------------------------------
	def writeLineTo(self, file_name, lineNumber, line):
	    lines = self.readLinesFrom(file_name)
	    lines[lineNumber] = line
	    self.writeLinesTo(file_name, lines)

	# write desire formatted content to file --------------------------------------------------------------------------
	def writeContentTo(self, file_name,content):

	     #locate and open file 
	     file = open(file_name,'w')

	     file.write(content+"\n")
	     file.close()

# append a line of text at the end to a file --------------------------------------------------------------------------
	def appendTo(self, file_name, line):
	    file = open(file_name, 'a')
	    file.write(line + "\n")
	    file.close()


	# --empty the file -------------------------------------------------------------------------------------------------------
	def removeLinesFrom(self, file_name):
		self.writeContentTo(file_name, '')

	# remove a particular line from file ------------------------------------------------------------------------------------
	def removeLineFrom(self, file_name, lineNumber):
		lines = self.readLinesFrom(file)
		try:
			lines[lineNumber] = ''
			self.writeLinesTo(file_name, lines)
		except:
			pass




