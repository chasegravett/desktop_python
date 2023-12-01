import tkinter as tk
import sqlite3
from PIL import ImageTk

# initiallize app
root = tk.Tk()
root.title("Recipe Picker")

# Settings for the frames
SCREEN_HEIGHT = root.winfo_screenheight()
SCREEN_WIDTH = root.winfo_screenwidth()
APP_WIDTH = 500
APP_HEIGHT = 600
X_OFFSET = SCREEN_WIDTH //2
Y_OFFSET = int(SCREEN_HEIGHT * 0.2)
BACKGROUND_COLOR = "#3d6466"

root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{X_OFFSET}+{Y_OFFSET}")

def fetch_db():
    connection = sqlite3.connect("data/recipes.db")
    cursor = connection.cursor()
    cursor.execute()



def load_title_frame():
    title_frame = tk.Frame(
        root, 
        width  = APP_WIDTH, 
        height = APP_HEIGHT, 
        bg     = BACKGROUND_COLOR
        )
    title_frame.grid(row=0, column=0)
    title_frame.pack_propagate(False)   #No child widgets can alter parent frame now. Background color, etc

    # Widgets for title frame 
    logo_image = ImageTk.PhotoImage(file="assets\RRecipe_logo.png")
    logo_widget = tk.Label(
        title_frame,
        image        = logo_image,
        bg           = BACKGROUND_COLOR
    )
    logo_widget.image = logo_image
    logo_widget.pack()

    tk.Label(
        title_frame,
        text          = "Choose a random recipe?",
        bg            = BACKGROUND_COLOR,
        fg            = "white",
        font          = ("TkMenuFont", 14)
    ).pack()

    tk.Button(
        title_frame,
        text             = "Roll a Random Recipe",
        font             = ("TkHeadingFont", 20),
        bg               = "#28393a",
        fg               = "white",
        cursor           = "hand2",
        activebackground = "#badee2",
        activeforeground = "black",
        command          = load_recipe_frame
    ).pack(pady=25)


def load_recipe_frame():
    recipe_frame = tk.Frame(
        root,
        bg     = BACKGROUND_COLOR
        )
    recipe_frame.grid(row=0, column=0)
    recipe_frame.pack_propagate(False)   #No child widgets can alter parent frame now. Background color, etc

    # Widgets for recipe frame 
    logo_image = ImageTk.PhotoImage(file="assets\RRecipe_logo.png")
    logo_widget = tk.Label(
        recipe_frame,
        width=100,
        height=100,
        image        = logo_image,
        bg           = BACKGROUND_COLOR
    )
    logo_widget.image = logo_image
    logo_widget.pack()

    tk.Label(
        recipe_frame,
        text          = "Welcome to the Recipe!",
        bg            = BACKGROUND_COLOR,
        fg            = "white",
        font          = ("TkMenuFont", 14)
    ).pack()

    tk.Button(
        recipe_frame,
        text             = "Back to main screen?",
        font             = ("TkHeadingFont", 20),
        bg               = "#28393a",
        fg               = "white",
        cursor           = "hand2",
        activebackground = "#badee2",
        activeforeground = "black",
        command          = load_title_frame
    ).pack(pady=25)



if __name__ == "__main__":
    # run app
    load_title_frame()
    root.mainloop()
    