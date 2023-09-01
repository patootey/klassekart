import tkinter as tk
from PIL import Image, ImageTk


class Button:
    def __init__(self, root, text="", colour="white", command="boolean"):
        self.colour = colour
        self.text = text
        self.command = command
        self.clicked = False
        self.create_button(root)

    def click(self):
        if self.command:
            self.command()
        self.clicked = True if self.clicked == False else False

    def create_button(self, root):
        self.button = tk.Button(
            root, text=self.text, bg=self.colour, command=self.click
        )
        self.button.pack()


class Photo:
    def __init__(
        self,
        root,
        image_path,
        size=(50, 50),
        bind=None,
        position=(0, 0),
        button="<Button-1>",
    ):
        self.image_path = image_path
        self.size = size
        self.position = position
        self.bind = bind
        self.button = button
        self.image = None
        self.label = None
        self.create_image(root)

    def create_image(self, root):
        photo = Image.open(self.image_path)
        photo = photo.resize(self.size, Image.ADAPTIVE)
        self.image = ImageTk.PhotoImage(photo)
        self.label = tk.Label(root, image=self.image)

        if self.bind is not None:
            self.label.bind(self.button, lambda event: self.bind())

        self.label.place(x=self.position[0], y=self.position[1])


prevpage = []


def clear_window(root, page=[]):
    for widget in root.winfo_children():
        if widget not in page and widget not in savedWidgets and widget not in prevpage:
            widget.destroy()


def keep_page(root):
    page = []
    for widget in root.winfo_children():
        if widget.winfo_ismapped() and widget not in savedWidgets:
            page.append(widget)
            widget.forget()
    return page


def load_page(root, page):
    if page is not None:
        clear_window(root, page=page)
        for widget in page:
            widget.pack()


savedWidgets = []


def save_widget(widget):
    global savedWidgets
    savedWidgets.append(widget)
