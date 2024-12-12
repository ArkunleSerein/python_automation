
# La liste des adresses
adresses = [{
    # Donnée de test statique
    "num": "1",
    "comp": "A",
    "voie": "Rue de la paix",
    "commune": "Paris",
    "cp": "75000"
    },
    {
    # Donnée de test statique
    "num": "2",
    "comp": "B",
    "voie": "Rue de la paix",
    "commune": "Paris",
    "cp": "75000"
    },
    {
    # Donnée de test statique
    "num": "3",
    "comp": "C",
    "voie": "Rue de la paix",
    "commune": "Paris",
    "cp": "75000"
    }
]

# Affiche les adresses
def affichage_adresse(adresses):
    print("Afficher les adresses")
    for i, adresse in enumerate(adresses, start=1):
        print(f"index n°{i} : {adresse}\n")

# Ajoute une adresse
def ajout_adresse(adresses):
    print("Ajouter une adresse")
    adresse = {
        "num": input("Numéro de voie : "),
        "comp": input("Complément : "),
        "voie": input("Intitulé de voie : "),
        "commune": input("Commune : "),
        "cp": input("Code postal : ")
    }
    adresses.append(adresse)

# Modifie une adresse
def edition_adresse(adresses):
    print("Modifier une adresse")
    index = int(input("index : ")) - 1
    adresse = adresses[index]
    adresse["num"] = input("Numéro de voie : ")
    adresse["comp"] = input("Complément : ")
    adresse["voie"] = input("Intitulé de voie : ")
    adresse["commune"] = input("Commune : ")
    adresse["cp"] = input("Code postal : ")

# Supprime une adresse
def suppression_adresse(adresses):
    print("Supprimer une adresse")
    index = int(input("index : ")) - 1
    del adresses[index]


while True:
    print("\n\n                Bienvenue dans l'application de gestion des adresses.\n")

    print("\n     MENU : OPTION DE GESTION DES ADRESSES\n")
    print("1 : Afficher les adresses")
    print("2 : Ajouter une adresse")
    print("3 : Modifier une adresse")
    print("4 : Supprimer une adresse")
    print("5 : Quitter l'application\n")
    choix = int(input("Choisissez une option : "))
    if choix == 1:
        affichage_adresse(adresses)
    elif choix == 2:
        ajout_adresse(adresses)
    elif choix == 3:
        edition_adresse(adresses)
    elif choix == 4:
        suppression_adresse(adresses)
    elif choix == 5:
        break
    else:
        print("Entrée invalide. Veuillez choisir une option valide.")

print("\nAu revoir !")
