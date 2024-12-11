# Écrire un algorithme permettant de saisir 15 notes et de les afficher.

notes = []
for i in range(15):
    note = int(input(f"Veuillez saisir la note {i+1}/15 : "))
    notes.append(note)

print(f"Les notes saisies sont : {notes}")
