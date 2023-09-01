# Export/Show
import tkinter as tk

root = tk.Tk()


def read_file():
    names = []
    with open("import_elever.txt", "r") as my_file:
        names = my_file.readlines()

    # Create a new tkinter window to display the names
    display_window = tk.Toplevel(root)
    display_window.title("Names from File")

    for i, name in enumerate(names):
        tk.Label(display_window, text=f"Name {i+1}: {name.strip()}").pack()


tk.Button(root, text="Read from file", command=read_file, bg="orange").grid(
    column=2, row=3
)

root.mainloop()
