import tkinter as tk
import ttkbootstrap as ttkb
from random import randint


def new_number():
    changer.config(text=f"{randint(1, 100)}")

# Lots of cool themes available. This one looks cool to me
# Takes the place of the old tkinter root = tk.Tk()
root = ttkb.Window(themename="solar")


# Default reusable stylings and dimensions
SCREEN_WIDTH = root.winfo_screenwidth() // 2
SCREEN_HEIGHT = root.winfo_screenheight() // 2
FONT_STYLE = "Verdana"
button_styling = ttkb.Style().configure(".", font=(FONT_STYLE, 20))

root.title("Bootstrap for desktop? WITH PYTHON?!")
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")


# Make a label
label_one = ttkb.Label(
    text = "Random Number Generator",
    font = (FONT_STYLE, 28),
    bootstyle = "default"
).pack(pady=25)


# Button
button = ttkb.Button(
    text = "Get a random number between 1-100",
    bootstyle = "success-outline",
    cursor = "hand2",
    style = button_styling,
    command = new_number
)
button.pack(pady=100)

changer = ttkb.Label(
    text = "",
    font = (FONT_STYLE, 28),
    bootstyle = "default"
)
changer.pack(pady=25)

if __name__ == "__main__":
    root.mainloop()