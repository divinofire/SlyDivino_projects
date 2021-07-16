# I modified this color picker app to enable me to copy color to clipboard after I pick my color
# this was used to select colors for the todo app

# author: SlyDivino  

from tkinter import *
from tkinter import colorchooser

choosen_color = "select color"
def pick_color():
    color = colorchooser.askcolor(title ="Choose color")
    color_me.config(bg=color[1])
    choosen_color = color[1]
    #color_me.config(text=color)
    color_me.config(state = "normal")
    color_me.delete(1.0, "end")
    color_me.insert(1.0, choosen_color)
    color_me.config(state = "disabled")
   
 
ws = Tk()
ws.title('SlyDivino color picker')
ws.geometry('500x400')

color_me = Text(
    ws,
    height = 1,
    font = ('Times', 20),
    relief = SOLID,
    padx=20, 
    pady=20
)

color_me.insert(1.0, choosen_color)
color_me.pack(expand=True)
color_me.configure(state = "disabled", inactiveselectbackground = color_me.cget("selectbackground"))

button = Button(
    ws, 
    text = "Choose Color",
    command = pick_color,
    padx=10,
    pady=10,
    font=('Times', 18),
    bg='#4a7a8c'
    )
button.pack()

ws.mainloop()