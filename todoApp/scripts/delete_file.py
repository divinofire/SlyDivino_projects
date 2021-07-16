# use this module with caution, it shows no mercy in deletion

import os
import shutil

#delete a file ----------------------------------
def delete_file(file_name):
	try:		
		os.remove(file_name)
		return True
	except:
		return False

#delete a folder -----------------------------------
def delete_folder(folder_name):
	try:
		shutil.rmtree(folder_name)
		return True
	except:
		return False

#test output --------------------------------------------

#file_to_delete = "my_file.txt"
# folder_to_delete = "test"
#print("file [ " + file_to_delete + " ] deleted" if delete_file(file_to_delete) else "file [ "+ file_to_delete +" ] could not be deleted or not found")
# print ("folder [ " + file_to_delete + " ] deleted" if delete_folder(folder_to_delete) else "folder ["+ folder_to_delete +"] could not be deleted or not found")



