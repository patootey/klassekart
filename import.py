# Import
import tkinter as tk

root = tk.Tk()
write_list = []

tk.Label(root, text="Input your name: ").grid(column=1, row=0)
name_entry = tk.Entry(root)
name_entry.grid(column=2, row=0)


def write_file():
    name = name_entry.get()
    write_list.append(name)
    with open("import_elever.txt", "a") as my_file:
        my_file.write(name + "\n")

    name_entry.delete(0, tk.END)  # Fjerner det som står i t


tk.Button(root, text="Write to a file", command=write_file, bg="turquoise").grid(
    column=1, row=3
)


root.mainloop()
