import random  # Importerer random-modulen for å generere tilfeldige tall


# Definisjon av klassen 'Group' for å representere grupper av elever
class Group:
    def __init__(self, pupils):
        self.pupils = pupils  # En liste som inneholder elever i gruppen
        self.padx = 5  # Padding-verdi for x-aksen (ikke brukt i koden)
        self.pady = 5  # Padding-verdi for y-aksen (ikke brukt i koden)
        self.border = 3  # Border-verdi for rammene rundt gruppen (ikke brukt i koden)


# Definisjon av klassen 'Pupil' for å representere en elev
class Pupil:
    def __init__(self, name):
        self.name = name  # Navnet til eleven
        self.colour = "F0F0F0"  # Farge for visuell representasjon (standard er grå)
        self.selected = False  # Status for om eleven er valgt
        self.label = None  # En widget-etikett som representerer eleven i GUI-en

    def click(self, groups):
        print("Trykk")  # En melding som skrives ut når eleven blir klikket på
        self.selected = (
            True if self.selected is False else False
        )  # Endrer statusen på eleven
        self.colour = (
            "Red" if self.selected is True else "#F0F0F0"
        )  # Endrer fargen basert på valgstatus
        self.label.config(bg=self.colour)  # Oppdaterer fargen til etiketten
        for group in groups:
            for pupil in group.pupils:
                if pupil.selected == True and pupil != self:
                    self.selected = False
                    self.colour = "#F0F0F0"
                    pupil.selected = False
                    pupil.colour = "#F0F0F0"
                    i = pupil.name
                    pupil.name = self.name
                    self.name = i
                    self.label.config(text=self.name, bg=self.colour)
                    pupil.label.config(text=pupil.name, bg=pupil.colour)
                print(pupil.name)


# Funksjon for å lese navnene fra en fil
def read_file():
    global name_list  # En global variabel som inneholder navnelisten
    names = []
    with open("import_elever.txt", "r") as my_file:
        names = my_file.readlines()

    # Oppretter en ny liste for å lagre navnene uten linjeskift
    name_list = [name.strip() for name in names]


# Funksjon for å generere grupper av elever
def generate_groups(names):
    # Blander listen med navn tilfeldig
    random.shuffle(names)

    # Liste for å lagre par eller grupper
    sitting_groups = []

    # Går gjennom de tilfeldig sorterte navnene
    while names:
        # Sjekker om det er minst 2 navn igjen
        if len(names) >= 2:
            # Tar de to første navnene som et par
            group = names[:2]
            names = names[2:]
        else:
            # Tar de gjenværende navnene som en gruppe
            group = names
            names = []

        sitting_groups.append(group)

    groups = []
    for group in sitting_groups:
        temp_group = []
        for name in group:
            temp_group.append(Pupil(name))
        groups.append(Group(temp_group))
    print(groups)

    for i in groups:
        if len(i.pupils) < 2:
            groups[len(groups) - 3].pupils.append(i.pupils[0])
            groups.remove(i)

    return groups
