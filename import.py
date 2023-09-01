import tkinter as tk

root = tk.Tk()
write_list = []

tk.Label(root, text="Input your name: ").grid(column=1, row=0)
name_entry = tk.Entry(root)
name_entry.grid(column=2, row=0)


def write_file():
    name = name_entry.get()
    write_list.extend((name))
    with open("imoport_elever.txt", "w") as my_file:
        for x in range(len(write_list)):
            write = write_list[x]
            my_file.write(write)


tk.Button(root, text="Write to a file", command=write_file, bg="turquoise").grid(
    column=1, row=3
)
root.mainloop()
