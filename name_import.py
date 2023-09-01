import tkinter as tk
import general as ge


def read_existing_names():
    existing_names = []
    try:
        with open("import_elever.txt", "r") as my_file:
            existing_names = my_file.read().splitlines()
    except FileNotFoundError:
        pass
    return existing_names


def all(root):
    ge.prevpage = ge.keep_page(root)
    frame = tk.Frame(root)
    write_list = []

    tk.Label(frame, text="Input your name: ").grid(column=1, row=0)
    name_entry = tk.Entry(frame)
    name_entry.grid(column=2, row=0)

    # Create a Listbox to display names
    name_listbox = tk.Listbox(frame)
    name_listbox.grid(column=3, row=0)

    # Populate the Listbox with existing names
    existing_names = read_existing_names()
    for name in existing_names:
        name_listbox.insert(tk.END, name)

    def write_file():
        name = name_entry.get()
        write_list.append(name)
        with open("import_elever.txt", "a") as my_file:
            my_file.write(name + "\n")

        name_entry.delete(0, tk.END)  # Fjerner det som står i textboksen

        # Update the Listbox with the new name
        name_listbox.insert(tk.END, name)

    tk.Button(frame, text="Write to a file", command=write_file, bg="turquoise").grid(
        column=1, row=3
    )
    frame.place(y=70)
