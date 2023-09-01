# Import
import tkinter as tk
import general as ge


def all(root):
    ge.prevpage = ge.keep_page(root)
    frame = tk.Frame(root)
    write_list = []

    tk.Label(frame, text="Input your name: ").grid(column=1, row=0)
    name_entry = tk.Entry(frame)
    name_entry.grid(column=2, row=0)

    def write_file():
        name = name_entry.get()
        write_list.append(name)
        with open("import_elever.txt", "a") as my_file:
            my_file.write(name + "\n")

        name_entry.delete(0, tk.END)  # Fjerner det som står i textboksen

    tk.Button(frame, text="Write to a file", command=write_file, bg="turquoise").grid(
        column=1, row=3
    )
    frame.place(y=70)
