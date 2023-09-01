import tkinter as tk
import general as ge
import groups as rg


def display_class(root):
    ge.prevpage = ge.keep_page(root)
    groups = rg.generate_groups(rg.names)
    main_frame =  tk.Frame(root)
    main_frame.place(y=50)
    x, y = 0,0
    for group in groups:
        print(group.pupils)
        frame = tk.Frame(main_frame)
        g = 0
        for i in group.pupils:
            label = tk.Label(frame, text=i, relief='solid')
            label.grid(column=g ,row=0)
            g+=1
        frame.grid(column=x, row=y, padx=10, pady=10)
        x+=1
        if x > 2:
            y+=1
            x = 0



    