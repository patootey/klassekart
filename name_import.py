import tkinter as tk  # Importerer tkinter-biblioteket for GUI
import general as ge  # Importerer en egenlagd modul 'general' som inneholder navigasjonssystem


# Funksjon for å lese eksisterende navn fra en fil
def read_existing_names():
    existing_names = []
    try:
        with open("import_elever.txt", "r") as my_file:
            existing_names = my_file.read().splitlines()
    except FileNotFoundError:
        pass
    return existing_names


# Funksjon for å slette det valgte navnet fra Listbox og filen
def delete_selected_name(name_listbox):
    selected_index = name_listbox.curselection()  # Få indeksen til det valgte elementet
    if selected_index:
        index = int(selected_index[0])  # Konverter indeksen til en integer
        name_to_delete = name_listbox.get(index)  # Få navnet som skal slettes
        name_listbox.delete(index)  # Fjern det valgte elementet fra Listbox

        # Fjern det slettede navnet fra filen
        with open("import_elever.txt", "r") as my_file:
            lines = my_file.readlines()
        with open("import_elever.txt", "w") as my_file:
            for line in lines:
                if line.strip() != name_to_delete:
                    my_file.write(line)


# Hovedfunksjon for konfigurering av elever
def all(root):
    ge.prevpage = ge.keep_page(root)  # Lagrer nåværende side
    frame = tk.Frame(root)  # Oppretter en ny rammekomponent

    # Oppretter et inndatafelt og en etikett for å legge inn navn
    tk.Label(frame, text="Skriv inn navn: ").grid(column=1, row=0)
    name_entry = tk.Entry(frame)
    name_entry.grid(column=2, row=0)

    # Oppretter en Listbox for å vise navnene
    name_listbox = tk.Listbox(frame)
    name_listbox.grid(column=3, row=0)

    # Oppretter en scrollbar for å bla gjennom eksisterende navn
    scrollbar = tk.Scrollbar(frame, orient="vertical")
    scrollbar.grid(row=0, column=4, sticky=tk.NS)

    # Kobler scrollbar til Listbox
    name_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=name_listbox.yview)

    # Fyller Listbox med eksisterende navn fra filen
    existing_names = read_existing_names()
    for name in existing_names:
        name_listbox.insert(tk.END, name)

    # Funksjon for å legge til et navn i Listbox og filen
    def write_file():
        name = name_entry.get()
        write_list.append(name)
        with open("import_elever.txt", "a") as my_file:
            my_file.write(name + "\n")

        name_entry.delete(0, tk.END)  # Fjerner det som står i tekstboksen

        # Oppdaterer Listbox med det nye navnet
        name_listbox.insert(tk.END, name)

    # Knapp for å legge til en elev
    tk.Button(frame, text="Legg til elev", command=write_file, bg="turquoise").grid(
        column=1, row=3
    )
    # Knapp for å slette et navn
    delete_button = tk.Button(
        frame,
        text="Slett navn",
        command=lambda: delete_selected_name(name_listbox),
        bg="red",
    )
    delete_button.grid(column=3, row=1)
    frame.place(y=70)  # Plasserer rammekomponenten i vinduet
