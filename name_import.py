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


def delete_selected_name(name_listbox):
    selected_index = name_listbox.curselection()  # Get the selected item index
    if selected_index:
        index = int(selected_index[0])  # Convert the selected index to an integer
        name_to_delete = name_listbox.get(index)  # Get the name to delete
        name_listbox.delete(index)  # Remove the selected item from the Listbox

        # Remove the deleted name from the file
        with open("import_elever.txt", "r") as my_file:
            lines = my_file.readlines()
        with open("import_elever.txt", "w") as my_file:
            for line in lines:
                if line.strip() != name_to_delete:
                    my_file.write(line)


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

    # Create a Scrollbar to scroll through the existing names
    scrollbar = tk.Scrollbar(frame, orient="vertical")
    scrollbar.grid(row=0, column=4, sticky=tk.NS)

    # Attach the Scrollbar to the Listbox
    name_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=name_listbox.yview)

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

    delete_button = tk.Button(
        frame,
        text="Delete",
        command=lambda: delete_selected_name(name_listbox),
        bg="red",
    )
    delete_button.grid(column=1, row=1)
    tk.Button(frame, text="Write to a file", command=write_file, bg="turquoise").grid(
        column=1, row=3
    )
    frame.place(y=70)
