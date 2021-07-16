import os

# create_folder ---------------------------------------------------


def create_folder(folder_path):
	try:
		os.mkdir(folder_path)
		return True
	except:
		return False

# create_file------------------------------------------------------------
def create_file(file_path):
	try:
		file = open(file_path, "w")
		file.close()
		return True
	except:
		return False

#test output -----------------------------------------------------
# folder_to_create = "my_folder"
# file_to_create = "my_file.txt"
# print("file [ " + file_to_create + " ] created" if create_file(file_to_create) else "file [ "+ file_to_create +" ] could not be created or already exist")
#print("folder [ " + folder_to_create + " ] created" if create_folder(folder_to_create) else "file [ "+ folder_to_create +" ] could not be created or already exist") 




