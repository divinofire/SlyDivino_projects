# this is a third party class

from cool_functions import numerifyKeysOf
from tkinter import *


class App(object):

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        self.frame.grid()
        self.addFrame = Frame(master)
        self.addFrame.grid(row=0, column=0, columnspan=2, sticky='N')
        self.listFrame = Frame(master)
        self.listFrame.grid(row=1, column=0, columnspan=2, sticky='NW')
        self.todoList = {}
        self.buttonList = {}  #<--- button list is here now
        self.displayUI()


    def displayUI(self):

        self.entryBox = Entry(self.frame, width = 15)
        self.entryBox.grid(row=0, column=0, sticky='N')

        self.addButton = Button(self.frame, text="<-ADD->", command=self.add)
        self.addButton.grid(row=0, column=1, sticky='N')

        self.deleteAll = Button(self.frame, text="Delete All", command=self.delete_all)
        self.deleteAll.grid(row=0, column=2, sticky='N')

        self.fix = Button(self.frame, text="fix bug", command=self.fix_me)
        self.fix.grid(row=0, column=3, sticky='N')


    def removeCheckButton(self, button_no):
        
        print(button_no)
        print(button_no)
        print(button_no)
        self.buttonList[button_no].destroy()
        self.buttonList.pop(button_no) # remove button from button list after destroy
        self.todoList.pop(button_no)
        print(self.todoList)
        
        

    def add(self):
        entry = self.entryBox.get()
        self.entryBox.delete(0, END)
        self.todoList.update({len(todoList), entry})
        print(self.todoList)
        var = IntVar()
        n = len(self.buttonList)
        print(n)
        lx = Checkbutton(self.listFrame,
                         text=self.todoList[n],
                         #variable=self.todoList[n], # not used
                         variable = var,
                         command=lambda n=n: self.removeCheckButton(n)) # couldn't pass argument directly to remove.. without lambda function
                         #command=self.removeCheckButton(n))
        lx.grid(row=n, column=0, sticky='NW')
        self.buttonList.append(lx)
        #n = len(self.buttonList)
        #   print(self.buttonList)

    def delete_all(self):
    	for but in self.buttonList:
    		but.destroy()
    	self.buttonList = []
    	self.todoList = []

    def fix_me(self):
    	tempList = self.buttonList
    	tempTodo = self.todoList
    	for but in self.buttonList:
    		but.destroy()
    	self.buttonList = []
    	self.todoList = []
    	self.todoList = tempTodo

    	nn = len(self.todoList)
    	if (nn != 0):
    		for n in range(nn):
    			lx = Checkbutton(self.listFrame, text=self.todoList[n], variable = self.todoList[n], command=lambda n=n: self.removeCheckButton(n)) 
    			lx.grid(row=n, column=0, sticky='NW')
    			self.buttonList.append(lx)

root = Tk()
app = App(root)
root.mainloop()