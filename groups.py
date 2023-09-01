import random
import tkinter as tk


class Group:
    def __init__(self, pupils):
        self.pupils = pupils
        self.padx = 5
        self.pady = 5
        self.border = 3


class Pupil:
    def __init__(self, name):
        self.name = name
        self.colour = "F0F0F0"
        self.selected = False
        self.label = None

    def click(self, groups):
        print("Trykk")
        self.selected = True if self.selected is False else False
        self.colour = "Red" if self.selected is True else "#F0F0F0"
        self.label.config(bg=self.colour)
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


def read_file():
    global name_list
    names = []
    with open("import_elever.txt", "r") as my_file:
        names = my_file.readlines()

    # Create a new array to store the names
    name_list = [name.strip() for name in names]


def generate_groups(names):
    # Shuffle the list of names randomly
    random.shuffle(names)

    # list to store pairs or groups
    sitting_groups = []

    # Loop through the shuffled names
    while names:
        # Check if there are at least 2 names remaining
        if len(names) >= 2:
            # Take two names for a pair
            group = names[:2]
            names = names[2:]
        else:
            # Take the remaining names as a group
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
