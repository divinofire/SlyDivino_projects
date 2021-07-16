#this is a reflica of the file manager file



import os
import shutil
join = os.path.join

class FileManager:

	#initialise working directory with current directory is no directory path is passed ---------------------------
	def __init__(self, directory = os.getcwd()):
		self.directory = os.getcwd() 
		self.file_name = ""

		self.no = 1 # a global variable to keep track of recursion in 
		self.temp = self.directory # global variable to watch self.directory

	# change working directory ----------------------------------------------------------------------

	def change_directory(self, directory_path):
		self.directory = directory_path
		self.temp = self.directory # global variable to watch self.directory


	# change current files to do file operations on -------------------------------------------------
	def use(self, file_name):
		self.file_name = join(self.directory, file_name)


#=========================================================================================================================
#                              						initial base methods
#=========================================================================================================================


	# remove a EOL character a the end of a string of text ---------------------------------------------
	def remove_new_line_char(self, line):
		#check if last item of line is the \n character for windows or \r for linux
	    if (line[-1] == "\n") or (line == "\r"): 
	            return(line[:-1]) # return all but the last character of the line 
	    else:
	        return line


	# read all lines from file----------------------------------------------------------------------------
	def readLines(self):
	     
	    # open file in read mode
	    file = open(self.file_name,'r')

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
	def readLine(self, lineNumber): 

	    # lineNumber may be out of index, return empty string if any exception occurs
	    try:
	        line = self.readLines()[lineNumber]
	        return line
	    except:
	        return ''

	# Write to A file :: lines should be a list of strings --------------------------------------------
	def writeLines(self, lines):
	    
	     #locate and open file
	     file = open(self.file_name,'w')

	     #Addto file
	     for line in lines:
	        if (line != ''):
	            file.write(line + "\n")
	     file.close()


	# Write a string to a particular line in a file (NB: the line number must exist, index starts at 0) ----------------------------------
	def writeLine(self, lineNumber, line):
	    lines = self.readLines()
	    lines[lineNumber] = line
	    self.writeLines(lines)


	# write desire formatted content to file --------------------------------------------------------------------------
	def writeContent(self, file_name,content):

	     #locate and open file 
	     file = open(self.file_name,'w')

	     file.write(content+"\n")
	     file.close()

# append a line of text at the end to a file --------------------------------------------------------------------------
	def append(self, line):
	    file = open(self.file_name, 'a')
	    file.write(line + "\n")
	    file.close()




	# --empty the file -------------------------------------------------------------------------------------------------------
	def removeLines(self):
		self.writeContentTo(self.file_name, '')

	# remove a particular line from file ------------------------------------------------------------------------------------
	def removeLine(self, lineNumber):
		lines = self.readLines()
		try:
			lines[lineNumber] = ''
			self.writeLines(lines)
		except:
			pass



#=========================================================================================================================
#                              						extra useful methods
#=========================================================================================================================

	


	# get list of files --------------------------------------------------------------------------
	def get_files(self):
		file_list = []

		for root, directories, files in os.walk(self.directory):
			for file in files:
				file_list.append(join(root,file))

		return file_list

	# get list of directories --------------------------------------------------------------------
	def get_dirs(self): 
		folder_list = []
		for root, directories, files in os.walk(self.directory):
			for folder in directories:
				file_list.append(join(root, folder))
		return folder_list

	#check if an item is a directory----------------------------------------------------------------
	def isDirectory(self, item):
		return os.path.isdir(item)

	#check if an item is a file ----------------------------------------------------------------
	def isFile(self, item):
		return os.path.isfile(item)


	#returns a list of folders and files------------------------------------------------------------
	def iterate(self):
		file_and_folders = self.get_dirs() + self.get_files()
		return file_and_folders

	# get tree of files (dictionary of files and folders) --------------------------------------------------------
	def print_file_tree(self):
		#print(self.directory)
		space = ' '
		for root, directories, files in os.walk(self.directory):
			for folder in directory:
				print( space * self.no + folder)
				self.change_directory(join(root, folder))
				space += 1
				self.print_file_tree()
			for file in files:
				print( space* (self.no + 1) + directory)
		self.no = 1
		self.directory = self.temp


		
	
	# get list of files that ends with a particular extension ------------------------------------------------
	def get_files_with_extension(self, extension): # example: extension = ".py"
		file_list = []
		for root, directories, files in os.walk(self.directory):
			for file in files:
				if file.endswith(extension):
					file_list.append(join(root, folder))
	
	#get file name -------------------------------------------------------------------------------------------------
	def get_file_name(self, file):
		return os.path.basename(file)

	#get extension name ----------------------------------------------------------------------------------
	def get_file_extension(self, file):
		return os.path.splitext(file)[-1]



	#get directory name --------------------------------------------------------------------------------
	def get_directory_name(self, directory):
		return os.path.dirname(directory)


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



