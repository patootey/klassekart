import random

#Klasseliste 
names = ["Lukas", "Henrik", "Mathilde", "David", "Morten", "Mari_S", "Mari_R", "Ida", "Sophie", "Hooman", "Morits",
         "Sebastian", "Andreas", "Tor", "Mohammed", "Valeria", "Leo", "Amiin", "Ole", "Benjamin", "Sanna", "Tina", "Yasmina", 
         "Awan", "Hevy", "Erik", "Tjark", "Gustav", "Vebjorn", "Ulrykk", "Even"]

#Stokker navnene tilfeldig
random.shuffle(names)

#Liste av par og grupper
sitting_groups = []

#Løkker rundt navnene
while names:
    #Sjekker om det er minst to navn igjen
    if len(names) >= 2:
        #tar to navn for ett par
        group = names[:2]
        names = names[2:]
    else:
        #Setter de gjennstående navn i grupper
        group = names
        names = []


    sitting_groups.append(group)

#Skriver ut gruppene
for i, group in enumerate(sitting_groups, start=1):
    group_str = ", ".join(group)
    print(f"Group {i}: {group_str}")