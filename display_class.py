import tkinter as tk
import general as ge
import groups as rg


def display_class(root):
    rg.read_file()
    ge.prevpage = ge.keep_page(root)
    groups = rg.generate_groups(rg.name_list)
    main_frame = tk.Frame(root)
    main_frame.place(y=50)
    x, y = 0, 0
    for group in groups:
        frame = tk.Frame(main_frame)
        g = 0
        for i in group.pupils:
            label = tk.Label(
                frame, text=i.name, relief="solid", borderwidth=group.border
            )
            label.bind(
                "<Button-1>",
                lambda event, groups=groups, label=label: i.click(label, groups),
            )
            label.grid(column=g, row=0)
            g += 1
        frame.grid(column=x, row=y, padx=group.padx, pady=group.padx)
        x += 1
        if x > 2:
            y += 1
            x = 0
