'''this is a third party class I found somewhere online (i have forgotten where, maybe stackexchange),
 I modified it to suit my needs

author: SlyDivino
 '''


import tkinter as tk
from tkinter import ttk

class ScrollableFrame(ttk.Frame):

	

	
	def __init__(self, container, *args, **kwargs):
		super().__init__(container, *args, **kwargs)

	def configure(self, height = 800, width = 400, bg = "white"):
		canvas = tk.Canvas(self, height = height, width = width, bg = bg)
		scrollbar = ttk.Scrollbar(self, orient = "vertical", command = canvas.yview)
		self.scrollable_frame = ttk.Frame(canvas)
		self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

		canvas.create_window((0,0), window=self.scrollable_frame, anchor = "nw")
		canvas.configure(yscrollcommand = scrollbar.set)

		canvas.pack(side = "left", fill="both", expand=True)
		scrollbar.pack(side="right", fill="y")

	# def addSrolls():
	# 	#add scroll handlers here

	



#testing ScrollableFrame class

# root = tk.Tk()

# frame = ScrollableFrame(root)

# for i in range(50):
# 	ttk.Label(frame.scrollable_frame, text = "sample scrollable labels using the scroll class").pack()

# frame.pack() 
# root.mainloop()