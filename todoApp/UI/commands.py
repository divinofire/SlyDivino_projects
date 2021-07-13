from tkinter import *
from tkinter import font

root = Tk()

#set window name and initial size
root.title("todo App")
root.geometry('600x400+50+50')
root.option_add('*Font', '40')
fonts = list(font.families())
fonts.sort()

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

mylist = Listbox(root, yscrollcommand = scrollbar.set, width=400, selectmode = EXTENDED)

for font_ in fonts:
	mylist['font'] = (font_, 12)
	mylist.insert(END, "this is font " + str(font_))

mylist.pack(side = LEFT, fill = BOTH)
scrollbar.config(command = mylist.yview)


mainloop()


