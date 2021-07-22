
#file manager class
#Author: SlyDivino

import os
import shutil
join = os.path.join

class FileManager:

	#initialise working directory with current directory is no directory path is passed ---------------------------
	def __init__(self, directory = os.getcwd()):
		self.directory = directory
		self.file_name = ""

		self.no = 1 # a global variable to keep track of recursion in 
		self.temp = self.directory # global variable to watch self.directory
		self.mylist = []


	# change working directory (provide absolute path) ----------------------------------------------------------------------

	def change_directory(self, directory_path):
		self.directory = directory_path

	# go to a directory relative to current directory ------------------------------------------------------------------------
	def change_to_relative_dir(self, relative_path):
		self.directory = join(self.directory, relative_path)

	#go to home directory of the script running FileManager -------------------------------------------------------------
	def go_to_home_dir(self):
		self.change_directory(os.getcwd());


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
	# read content from file as a whole string -------------------------------------------------------------------------
	def readContent(self):
		file = open(self.file_name,'r')
		content_list = file.readlines()
		content = ''
		for con in content_list:
			content += con
		file.close()
		return content



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
	

	def writeContent(self, content):

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
		self.writeContent('')

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
		try:
			for item in os.listdir(self.directory):
				if self.isFile(join(self.directory, item)):
					file_list.append(item)
					#print(item)
		except:
			pass
		return file_list

	# get list of directories --------------------------------------------------------------------
	def get_dirs(self): 
		folder_list = []
		try:
			for item in os.listdir(self.directory):
				if self.isDirectory(join(self.directory, item)):
					folder_list.append(item)
					#print(item)
		except:
			pass

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


	# generate file tree by populating self.mylist with the file tree ------------------------------------------------------------------
	def generate_file_tree(self):
		space = '	'
		for file in self.get_files():
			self.mylist.append( space* self.no + file)

		for folder in self.get_dirs():
			self.mylist.append( space * self.no + '**'+folder)
			self.change_to_relative_dir(folder)
			self.no += 1
			self.generate_file_tree()

		self.no = 1
		self.directory = self.temp

	# return file tree as a list ------------------------------------------------------------------------------------------
	def get_file_tree_list(self):

			self.generate_file_tree()
			temp = self.mylist
			self.mylist = []
			return temp

	# print file tree to console ----------------------------------------------------------------------------------------------------
	def print_file_tree(self):
		for item in self.get_file_tree_list():
			print(item)

	# print file tree to console with all files and folders having absolute paths
	def print_file_tree_R(self):
		for root, directories, files in os.walk(self.directory, topdown = False):
			for file in files:
				print(join(root, file))
			for folder in directories:
				print(join(root, folder))

		
	
	# get list of files that ends with a particular extension ------------------------------------------------
	def get_files_with_extension(self, extension): # example: extension = ".py"
		file_list = []
		for root, directories, files in os.walk(self.directory):
			for file in files:
				if file.endswith(extension):
					file_list.append(join(root, file))
		return file_list
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
			os.mkdir(join(self.directory, folder_name))
			return True
		except:
			return False

	# create_file------------------------------------------------------------------------------------

	def create_file(self,file_name):
		try:
			file = open(join(self.directory, file_name), "w")
			file.close()
			return True
		except:
			return False


	#delete a file -----------------------------------------------------------------------------------
	def delete_file(self,file_name):
		try:		
			os.remove(join(self.directory,file_name))
			return True
		except:
			return False

	#delete a folder ----------------------------------------------------------------------------------
	def delete_folder(self, folder_name):
		try:
			shutil.rmtree(join(self.directory,folder_name))
			return True
		except:
			return False



#test output

# put some 5 or more lines of text in test.txt in todo app before running this code
# test this code by uncommenting one section at a time inorder to understand what is happening


# db = FileManager()
# db.change_directory("../")
# db.use("test.txt")


# def printDB():
# 	print(db.readLines())

# print("readlines")
# printDB()

# print("read content")
# print(db.readContent())

# print("readLine - read line 1")
# print(db.readLine(0))

# print("writeLine - line 1")
# db.writeLine(0, "I changed this line")
# printDB()

# print("writeLines")
# a = ["new line 1", "new line 2", "new line 3", "new line 4"]
# db.writeLines(a)
# printDB()

# print("writeContent")
# db.writeContent("this is content 1\n this is content 2\n this is content 3\n this is content 4")
# printDB()

# print("append")
# db.append("this is line was appended")
# printDB()

# print("removeLine")
# db.removeLine(-1)
# printDB()

# print("removeLines")
# db.removeLines()
# printDB()


#test output 2


# print("get files")
# print(db.get_files())

# print("get dirs")
# print(db.get_dirs())

# print("iterate")
# print(db.iterate())

# print("print file tree of " + db.get_directory_name(db.directory)) # this did not work as expected
# db.print_file_tree()

# print("print_file_tree recursively using os.walk()")
# db.print_file_tree_R()


# print("get_files_with_extension('.py') in current working directory")
# db.go_to_home_dir()
# for file in db.get_files_with_extension(".py"):
# 	print(db.get_file_name(file))

# db.change_directory(db.temp)

# print("get directory name")
# db.go_to_home_dir()
# for file in db.get_files_with_extension(".py"):
# 	print(db.get_directory_name(file))

# print("get file extension")
# for file in db.get_files():
# 	print(db.get_file_extension(file))

# print("create file")
# db.create_file("new_file.txt")

# print("create folder")
# db.create_folder("new_folder")
# db.change_directory(join(db.directory, "./new_folder"))
# db.create_file("new_file_in_folder.txt")

# print("change to relative dir")
# db.change_to_relative_dir("./new_folder")
# db.create_file("file_to_delete.txt")

# print("delete file")
# db.change_to_relative_dir("./new_folder")
# db.delete_file("file_to_delete.txt")

# print("delete folder")
# db.delete_folder("new_folder")

#all methods worked except print_file_tree (but print_file_tree_R worked!)

#delete folder only if folder is empty
# db.create_folder("folder")
# db.change_to_relative_dir("./folder")
# db.create_file("file.xlsx")
# db.change_to_relative_dir("./folder")
# noFiles = db.get_files() == []
# noDirs = db.get_dirs() == []
# if (noDirs and noFiles):
# 	db.change_to_relative_dir("../")
# 	db.delete_folder("folder")


manager = FileManager("../../../SlyDivino_projects/todoApp/")
print(manager.directory)
#manager.change_to_relative_dir("todoApp/")
print(manager.directory)

# print(manager.get_dirs())
# print("---file tree----")
manager.print_file_tree()

# for folder in manager.get_dirs():
# 	try:
# 		manager.change_directory(join("../../../arduino_proteus_projects/.git", folder))
# 		manager.print_file_tree()
# 	except:
# 		pass





