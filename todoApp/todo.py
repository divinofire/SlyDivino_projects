import os
import tkinter  as tk
from tkinter import font
from tkinter import ttk
from UI.ScrollableFrame import ScrollableFrame 
from scripts.file_manager import FileManager
from UI.cool_functions import dict_from_list
todo_database = "scripts/todo_database.sly" # database of our todos
# todo_database_path = os.path.join(os.getcwd(), todo_database)
DBMS = FileManager()
DBMS.use(todo_database)

# root of app, similar to the foundation of a house on which we start laying blocks but in this case we lay widgets
root = tk.Tk() 

# declare some colors to use globally (colorpi)
bg1 = "Light Green"
bg2 = "Light Blue"
bg3 = "black"
bg4 = "#e9c5d3"
bg5 = "#d82382"

initialTask_dict = DBMS.readLines() # load existing todos
initialTask_dict = dict_from_list(initialTask_dict)
task_button_dict = {}


#set window name, initial size,  ------------------------------------------------------------------------
root.title("Todo App")
root.geometry('900x600+300+50')
root.config(bg = "Light Blue")
root.option_add('*Font', '40')
fonts = list(font.families()) # get fronts
fonts.sort() # sort fonts in alphabetical order

#title ------------------------------------------------------------------------------------------
title = tk.Label(root, text="TODO APP", bg = bg2, font=("GOUDY STOUT", 16))
title.pack(pady = 20)

# setup frames --------------------------------------------------------------------------------------
addTaskFrame = tk.Frame(root, bg = bg3) 
addTaskFrame.pack()

#add taskFrame to root (taskFrame will contain taskFrame2, mark as complete button and delete button)
taskFrame = tk.Frame(root)
taskFrame.pack(pady = 10)
taskFrame.configure(height = 500, width=600, bg = bg2)

#add taskFrame2 to taskFrame (taskframe2 will contain the list of tasks as checkbuttons) 
taskFrame2 = ScrollableFrame(taskFrame)  #place taskframe2 in taskframe
taskFrame2.configure(height = 500, width=600, bg = bg4)


# we could have put the tasks directly in taskframe2 but I just created a seperate frame for the tasks below
tasks_check_buttons_Frame = tk.Frame(taskFrame2.scrollable_frame) 
task_numbering_frame = tk.Frame(taskFrame2.scrollable_frame)

#arrange all children of taskframe2
task_numbering_frame.pack(side = tk.LEFT, fill = tk.Y)
tasks_check_buttons_Frame.pack(side = tk.LEFT, fill = tk.Y) # pack tasks to the left of taskFrame2 against number


#new task entry widget --------------------------------------------------------------------------------------
newTask = tk.Entry(addTaskFrame, width = 60)
newTask_label = tk.Label(addTaskFrame, text = "New Task")
addTask_button = tk.Button(addTaskFrame, text = "Add Task", command = lambda: add_task(), fg= "white", bg = bg5 , activebackground = "white", activeforeground="black")


#bind <enter key> press to newTask entry widget
newTask.bind('<Return>', lambda e: add_task())

#arrange widgets in new task frame---------------------------------------------------------------------
newTask_label.pack(side = tk.LEFT, padx = 50)
newTask.pack(side = tk.LEFT)
addTask_button.pack(side = tk.LEFT, padx = 50)

# add delete and mark as complete buttons to taskFrame
delete = tk.Button(taskFrame, text = "Delete", fg= "white", bg = "red" , activebackground = "white", activeforeground="black") 
markAsComplete =  tk.Button(taskFrame, text = "Complete", fg= "white", bg = "green" , activebackground = "white", activeforeground="black")

#arrange all children of taskFrame  (children = delete, markAsComplete and taskFrame2)
markAsComplete.pack(side = tk.LEFT, padx = 20, pady = 50)
taskFrame2.pack(side = tk.LEFT, pady = 10)
delete.pack(side = tk.LEFT, padx = 20, pady = 50)


# refresh tasks  ::  fill task_check_buttons_frame with task labels from list (fonts) -------------------------------------------------

def refresh_tasks():
	i = 0
	but = 0
	if len(initialTask_dict) == 0:
		message_for_empty_list = tk.Label(tasks_check_buttons_Frame, bg=bg4, font=("elephant", 12) ,text = "No todo tasks, add some tasks", anchor="w", height=2, width=50)
		message_for_empty_list.pack(side = "top", fill="both")
	elif("message_for_empty_list" in locals()):
		message_for_empty_list.destroy()


	for font_ in initialTask_dict:
		
		i = i + 1
		if (i%2 == 1):
			number = tk.Label(task_numbering_frame, text=str(i), anchor="w", bg="blue", height=2)
			#number.pack(side = "top", fill="both", pady=2)
			task = tk.Checkbutton(tasks_check_buttons_Frame, command = lambda e=but: remove_task(e),  bg=bg4, font=(font_, 12) ,text = str(i) + ".  " + str(initialTask_dict[font_]), anchor="w", height=2, width=50)
			task.pack(side = "top", fill="both")
			task_button_dict.update({but : task})
		else:
			task = tk.Checkbutton(tasks_check_buttons_Frame, command = lambda e=but: remove_task(e), font=(font_, 12) ,text = str(i) + ".  " + str(initialTask_dict[font_]), anchor="w", height=2, width=50)
			task.pack(side = "top", fill="both")
			number = tk.Label(task_numbering_frame, text=str(i), anchor="w", bg="pink", height=2)
			task_button_dict.update({but : task})
			#number.pack(side = "top", fill="both", pady = 10)
		but +=1

# refresh_tasks when the program starts ------------------------------------------------------------------------
refresh_tasks()


# --------add task to list of tasks and afer that update UI to reflect changes ------------------------------------
def add_task():
	global initialTask_dict
	my_new_task = newTask.get()
	if (my_new_task):
		initialTask_dict.update({"a":my_new_task})
		DBMS.append(my_new_task)
		update_tasks_on_UI()


# -----------remove task from list of tasks then update UI ------------------------------------------------------
def remove_task(task_button_index):
	global task_button_dict
	global initialTask_dict
	print("task_button_index: " + str(task_button_index))
	task_button_dict[task_button_index].destroy()
	task_button_dict.pop(task_button_index)
	initialTask_dict.pop(task_button_index)
	DBMS.removeLine(task_button_index)
	update_tasks_on_UI()
	print(initialTask_dict)

# ---------- update tasks on UI, similar to refresh task but more powerful -------------------------------------------------
def update_tasks_on_UI():
	global initialTask_dict
	temp_list = initialTask_dict
	remove_all_tasks()
	initialTask_dict = numerifyKeysOf(temp_list)
	refresh_tasks()

# ------------ remove all tasks  without updating ui ------------------------------------------------------------------
def remove_all_tasks():
	global task_button_dict
	global initialTask_dict
	for key in task_button_dict:
		task_button_dict[key].destroy()
	task_button_dict = {}
	initialTask_dict = {}

# define a scroll function (this function was not used)----------------------------------------
def scroll_buttons_and_list(*args):
	mylist.yview(*args)
	#buttonFrame.yview(*args)

def numerifyKeysOf(dictionary):
	new_dict = {}
	i = 0
	for key in dictionary:
		new_dict.update({i: dictionary[key]})
		i += 1
	return new_dict
#print(task_button_dict)
#scrollbar.config(command = scroll_buttons_and_list)


# hang program in infinite loop while checking for changes in root------------------------------------------------------------------------------
root.mainloop()


