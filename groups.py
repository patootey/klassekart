import random


class Group:
    def __init__(self, pupils):
        self.pupils = pupils
        self.desk_size = (30, 20)
        self.border = 10


# List of classrom
names: list[str] = [
    "Lukas",
    "Henrik",
    "Mathilde",
    "David",
    "Morten",
    "Mari_S",
    "Mari_R",
    "Ida",
    "Sophie",
    "Hooman",
    "Morits",
    "Sebastian",
    "Andreas",
    "Tor",
    "Mohammed",
    "Valeria",
    "Leo",
    "Amiin",
    "Ole",
    "Benjamin",
    "Sanna",
    "Tina",
    "Yasmina",
    "Awan",
    "Hevy",
    "Erik",
    "Tjark",
    "Gustav",
    "Vebjorn",
    "Ulrykk",
    "even",
]


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
    for i in sitting_groups:
        groups.append(Group(i))

    for i in groups:
        if len(i.pupils) < 2:
            groups[len(groups) - 3].pupils.append(i.pupils[0])
            groups.remove(i)

    return groups
