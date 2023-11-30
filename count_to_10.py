import tkinter as tk

FONT_STYLE = "Lucida Console"
FONT_SIZE = 35

window = tk.Tk()


# Using built-in tkinter methods to get the screen res and set app window size
SCREEN_WIDTH = window.winfo_screenwidth() // 2
SCREEN_HEIGHT = window.winfo_screenheight() // 2


# Initialize window with size and title
window.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
window.title("A Desktop Application made with Python!")
counter = 0


# 
def add_one():
    global counter
    counter += 1
    
    if counter < 10:
        label.configure(text=f"You are currently on number {counter}")
    else:
        button.configure(text="Done!")
        label.configure(text="Congrats! You counted to 10!")


# Puts text (or "label") to the screen
label = tk.Label(window, text=f"You are currently on number {counter}", font=(FONT_STYLE, FONT_SIZE))
label.grid(column=0, row=1)    


# Initialize a button with text. bg = button color, fg = text color.
# command will allow you to configure an 'onpressed' function
button = tk.Button(
    window, 
    text="Press me to count!",
    bg = "black",
    fg = "white",
    command = add_one
    )

#Position button directly under the existing label
button.grid(column=0, row=0) 



if __name__ == "__main__":
    # Starting the loop that allows the window to be displayed until closed
    window.mainloop()