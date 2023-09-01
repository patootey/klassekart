import tkinter as tk
import general as ge
import display_class as dc
import name_import
import os
import sys

r = tk.Tk()  # Oppretter et hovedvindu (root) for GUI-en
r.title("Lag et klassekart")  # Setter tittelen på vinduet
r.geometry("400x300")  # Setter størrelsen på vinduet til 400x300 piksler


# Definerer hovedfunksjonen for programmet
def main(root):
    ge.clear_window(root)  # Kaller en funksjon for å fjerne alle widgets fra vinduet
    # Oppretter en knapp for å generere klassen og knytter den til en funksjon 'display_class'
    button = ge.Button(
        root, text="Generer Klasse", command=lambda: dc.display_class(root)
    )
    # Oppretter en knapp for å konfigurere elever og knytter den til en funksjon 'name_import.all'
    button2 = ge.Button(
        root, text="Konfigurer elever", command=lambda: name_import.all(root)
    )
    # Oppretter en knapp for å avslutte programmet og knytter den til en funksjon 'exit'
    button3 = ge.Button(root, text="Avslutt", command=lambda: exit(root), colour="red")
    root.mainloop()  # Starter GUI-hovedløkka for å vise vinduet


# Definerer en funksjon for å avslutte programmet og lukke vinduet
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
# Oppretter en 'Hjem'-knapp med et bilde og knytter den til hovedfunksjonen 'main'
home_button = ge.Photo(
    r, home_image_path, size=(40, 40), position=(40, 0), bind=lambda: main(r)
)
# Oppretter en 'Pil'-knapp med et bilde og knytter den til en funksjon 'ge.load_page'
arrow = ge.Photo(
    r, arrow_image_path, size=(40, 40), bind=lambda: ge.load_page(r, ge.prevpage)
)

# Lagrer knappene som widgets for senere bruk
ge.save_widget(arrow.label)
ge.save_widget(home_button.label)

if __name__ == "__main__":
    # 
    main(r)
    r.mainloop()
