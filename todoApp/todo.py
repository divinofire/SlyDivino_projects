import tkinter  as tk
from tkinter import font
from tkinter import ttk
from UI.ScrollableFrame import ScrollableFrame

root = tk.Tk()

bg1 = "Light Green"
bg2 = "Light Blue"
bg3 = "black"
bg4 = "#e9c5d3"


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
addTaskFrame = tk.Frame(root, bg = "black") 
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
tasks_check_buttons_Frame.pack(side = tk.LEFT, fill = tk.Y) # pack tasks to the left of taskFrame2


#new task entry widget --------------------------------------------------------------------------------------
newTask = tk.Entry(addTaskFrame, width = 60)
newTask_label = tk.Label(addTaskFrame, text = "New Task")
addTask_button = tk.Button(addTaskFrame, text = "Add Task", fg= "white", bg = "#d82382" , activebackground = "white", activeforeground="black")

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


# fill task_check_buttons_frame with task labels from list (fonts) -------------------------------------------------
i = 0
for font_ in fonts:
	task = tk.Checkbutton(tasks_check_buttons_Frame, text = str(i) + ". this is font " + str(font_), anchor="w", height=2).pack(side = "top", fill="both")
	i = i + 1


# define a scroll function (this function was not used)----------------------------------------
def scroll_buttons_and_list(*args):
	mylist.yview(*args)
	#buttonFrame.yview(*args)

#scrollbar.config(command = scroll_buttons_and_list)


# hang program in infinite loop while checking for changes in root------------------------------------------------------------------------------
root.mainloop()


