from read_from_file import readLinesFrom
from write_to_file import writeContentTo
from write_to_file import writeLinesTo

# --empty the file ---------------------------------
def removeLinesFrom(file_name):
	writeContentTo(file_name, '')

# remove a particular line from file -----------------------------------
def removeLineFrom(file_name, lineNumber):
	lines = readLinesFrom(file)
	try:
		lines[lineNumber] = ''
		writeLinesTo(file_name, lines)
	except:
		pass


# test output -------------------------------------
# file = "todo_database.sly"
# todos = readLinesFrom("testfile.sly")

# writeLinesTo(file, todos)

# print(readLinesFrom(file))

# removeLineFrom(file, 1)
# print(readLinesFrom(file))

# removeLinesFrom(file)
# print(readLinesFrom(file))
