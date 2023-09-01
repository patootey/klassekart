import tkinter as tk
import general as ge
import display_class as dc
import name_import

r = tk.Tk()
r.title("Lag et klassekart")
r.geometry("400x300")


def main(root):
    ge.clear_window(root)
    button = ge.Button(
        root, text="Generer Klasse", command=lambda: dc.display_class(root)
    )
    button2 = ge.Button(
        root, text="Konfigurer elever", command=lambda: name_import.all(root)
    )
    button3 = ge.Button(root, text="Avslutt", command=lambda: exit(root), colour="red")
    root.mainloop()


def exit(root):
    root.destroy()


home_button = ge.Photo(
    r, "./images/home.png", size=(40, 40), position=(40, 0), bind=lambda: main(r)
)
arrow = ge.Photo(
    r, "./images/arrow.png", size=(40, 40), bind=lambda: ge.load_page(r, ge.prevpage)
)
ge.save_widget(arrow.label)
ge.save_widget(home_button.label)
main(r)
