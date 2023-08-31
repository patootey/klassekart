import tkinter as tk
import general as ge
from PIL import Image, ImageTk
import test

r = tk.Tk()
r.geometry("400x300")


def main(root):
    ge.prevpage = ge.keep_page(root)
    ge.clear_window(root)
    button = ge.Button(root, text="Click Me", command=lambda: test.wowow(root))
    root.mainloop()

home_button = ge.Photo(r, "./images/home.png", size=(40,40),position=(40,0) ,bind=lambda: main(r))
arrow = ge.Photo(r, "./images/arrow.png", size=(40,40), bind=lambda: ge.load_page(r, ge.prevpage))
ge.save_widget(arrow.label)
ge.save_widget(home_button.label)
main(r)
