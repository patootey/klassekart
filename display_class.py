import tkinter as tk  # Importerer tkinter-biblioteket for GUI
import general as ge  # Importerer en egenlagd modul 'general'
import groups as rg  # Importerer en egenlagd modul 'groups' for gruppebehandling


# Hovedfunksjonen for å vise klassen i GUI-en
def display_class(root):
    rg.read_file()  # Leser navn fra en fil ved hjelp av funksjonen fra 'groups' modulen
    ge.prevpage = ge.keep_page(
        root
    )  # Lagrer nåværende side i 'prevpage' ved hjelp av funksjoner fra 'general' modulen
    groups = rg.generate_groups(
        rg.name_list
    )  # Genererer grupper av elever ved hjelp av funksjonen fra 'groups' modulen

    main_frame = tk.Frame(root)  # Oppretter en hovedramme for å vise gruppene
    main_frame.place(y=50)  # Plasserer hovedrammen i GUI-en

    x, y = (
        0,
        0,
    )  # Initialisering av x- og y-koordinater for plassering av grupper i rutenettet

    for group in groups:
        frame = tk.Frame(main_frame)  # Oppretter en ramme for hver gruppe
        g = 0  # Variabel for å spore kolonnen innenfor gruppen

        # Går gjennom elevene i gruppen
        for i in group.pupils:
            i.label = tk.Label(
                frame, text=i.name, relief="solid", borderwidth=group.border
            )  # Oppretter en etikett for hver elev med navn og egenskaper
            i.label.bind(
                "<Button-1>",
                lambda event, pupil=i, groups=groups: pupil.click(groups),
            )  # Binder en klikk-hendelse til hver elev

            i.label.grid(
                column=g, row=0
            )  # Plasserer etiketten i rutenettet innenfor rammen
            g += 1  # Øker kolonnetelleren

        frame.grid(
            column=x, row=y, padx=group.padx, pady=group.padx
        )  # Plasserer rammen i rutenettet
        x += 1  # Øker x-koordinaten

        if x > 2:  # Sjekker om vi har nådd maksimalt antall kolonner
            y += 1  # Øker y-koordinaten for å gå til neste rad
            x = 0  # Nullstiller x-koordinaten for å starte på ny kolonne
