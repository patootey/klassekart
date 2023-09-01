import random

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

# Print the groups
for i, group in enumerate(sitting_groups, start=1):
    group_str = ", ".join(group)
    print(f"Group {i}: {group_str}")