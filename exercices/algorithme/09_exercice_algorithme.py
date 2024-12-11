# Écrire un programme qui permet de tester si un profil est valable pour une
# candidature ou non selon ces trois critères:
# L'âge minimum pour le poste est 30 ans
# Le salaire maximum possible est 40 000 euros.
# Le nombre d'années d'expérience minimum est de 5 ans.
# On affichera différents messages pour chaque condition non respectée.
# Il est possible de réaliser cet exercice avec une seule structure conditionnelle
# ne comportant qu'une condition par clause (pas de and/or)

age = int(
    input("Quelle est l'âge du candidat ? "))
if  age < 30:
    print("La personne n'a pas l'âge minimum pour candidater")
    exit()
salaire = int(
    input("Salaire souhaité du candidat : "))
if salaire > 40000:
    print("La personne demande un salaire trop élevé pour candidater")
    exit()
experience = int(
    input("Année d'expérience du candidat : "))
if experience < 5:
    print("La personne n'a pas assez d'expérience pour candidater")
    exit()
else: 
    print("Le profil de cette personne est valable pour une candidature")




