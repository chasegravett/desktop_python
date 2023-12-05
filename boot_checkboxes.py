import tkinter as tk
import ttkbootstrap as ttkb


root = ttkb.Window(themename="darkly")

# Default reusable stylings and dimensions
SCREEN_WIDTH = root.winfo_screenwidth() // 2
SCREEN_HEIGHT = root.winfo_screenheight() // 2
FONT_STYLE = "Cascadia Code Light"
button_styling = ttkb.Style().configure(".", font=(FONT_STYLE, 16))

root.title("Checking these boxes out")
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

def checker():
    if var1.get() == 0:
        my_checkbtn.config(text="Not checked :(")
    else:
        my_checkbtn.config(text="Checked!")

title = ttkb.Label(
    text = "Check these boxes out!",
    font = (FONT_STYLE, 40),
    bootstyle = "info"
)
title.pack(pady=(30, 10))

var1 = tk.IntVar()
my_checkbtn = ttkb.Checkbutton(
    text="Yes?",
    bootstyle = "info",
    variable = var1,
    onvalue = 1,
    offvalue = 0,
    style = button_styling,
    command = checker
)
my_checkbtn.pack(pady=30)


root.mainloop()