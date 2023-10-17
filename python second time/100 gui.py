import tkinter
from tkinter import *

# makes the window
window = Tk() 
window.geometry("950x650")# the size of the window
window.title("slyzoo gui program")

# makes and sets the icon for the window
icon = PhotoImage(file = "discord-avatar-512-RAI1B.png")
window.iconphoto(True, icon)

# chooses the colour for the window
# window.config(background="black") chooses black
window.config(background="#ff75f1")

# runs the window
window.mainloop()#place window on the screen and listen for events


