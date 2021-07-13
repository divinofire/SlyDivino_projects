import tkinter as tk
from tkinter import font
from tkinter import ttk
from ScrollableFrame import ScrollableFrame

root = tk.Tk()

root.geometry("600x400+40+40")
root.title("Fonts")

#setting up frames
fonts_frame = ScrollableFrame(root)
fonts_frame.configure(height = 800, width = 600, bg = "blue")


fonts = list(font.families())
fonts.sort()

i = 0
for font_ in fonts:
	i = i + 1
	#fontlabel = ttk.Label(fonts_frame.scrollable_frame,  anchor = "w",text = str(i) ).pack(side = "top", fill = "y")
	#numberlabel = ttk.Label(fonts_frame.scrollable_frame,  anchor = "w",text = "this is font number" + str(i)).pack(side = "top", fill="both")
	
	label = tk.Label(fonts_frame.scrollable_frame, bg="grey", anchor = "w", text= str(i)+". "+font_, font = (font_, 14)).pack(side = "top", fill="both")
	#label.configure(anchor = "left")


fonts_frame.pack()
root.mainloop()