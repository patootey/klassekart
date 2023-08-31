import tkinter as tk
import general as ge


def wowow(root):
    ge.prevpage = ge.keep_page(root)

    def key_pressed(event):
        print(ge.prevpage)

    # Bind the key event to the function
    root.bind("<KeyPress-A>", key_pressed)

    button = ge.Button(
        root,
        text="Tilbake",
        colour="red",
        command=lambda: ge.load_page(root, ge.prevpage),
    )
