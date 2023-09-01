import tkinter as tk
import general as ge
import display_class as dc
import name_import
import os
import sys

r = tk.Tk()
r.geometry("400x300")

def main(root):
    ge.clear_window(root)
    button = ge.Button(
        root, text="Generer Klasse", command=lambda: dc.display_class(root)
    )
    button2 = ge.Button(
        root, text="Legg til elever", command=lambda: name_import.all(root)
    )
    button3 = ge.Button(root, text="Avslutt", command=lambda: exit(root), colour="red")

def exit(root):
    root.destroy()

# Determine the path to the images directory
if getattr(sys, 'frozen', False):
    # Running as a PyInstaller executable
    script_dir = sys._MEIPASS
else:
    # Running as a script
    script_dir = os.path.dirname(os.path.abspath(__file__))

home_image_path = os.path.join(script_dir, "images", "home.png")
arrow_image_path = os.path.join(script_dir, "images", "arrow.png")
home_image_path.replace('\','/')
home_button = ge.Photo(
    r, home_image_path, size=(40, 40), position=(40, 0), bind=lambda: main(r)
)
arrow = ge.Photo(
    r, arrow_image_path, size=(40, 40), bind=lambda: ge.load_page(r, ge.prevpage)
)
ge.save_widget(arrow.label)
ge.save_widget(home_button.label)

if __name__ == "__main__":
    # Entry point when running the script directly
    main(r)
    r.mainloop()
