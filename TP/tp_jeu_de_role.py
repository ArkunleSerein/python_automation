# TP JEU DE ROLE
import random

# Les fonctions

personnages = [
    # Donnée de test statique
    {
        "nom": "Yorr",
        "classe": "Barbare",
        "niveau": 1,
        "points_de_vie": 100,
        "inventaire": {
            "objets": [
                {
                    "nom": "potion",
                    "quantité": 3
                }
            ]
        }
    },
    {
        "nom": "Arkun",
        "classe": "mage",
        "niveau": 1,
        "points_de_vie": 100,
        "inventaire": {
            "objets": [
                {
                    "nom": "potion",
                    "quantité": 3
                }
            ]
        }
    }
]

# ===============Affichage=================

def afficher_personnage(personnages):
    """Affiche les informations des personnages."""
    for i, personnage in enumerate(personnages, start=1):
        print(f"\nIndex : {i}")
        print(f"Nom : {personnage['nom']}")
        print(f"Points de vie : {personnage['points_de_vie']}")
        print(f"Classe : {personnage['classe']}")
        print(f"Niveau : {personnage['niveau']}")
        print(f"Inventaire : {', '.join([f'{objet["nom"]} ({objet["quantité"]})' for objet in personnage['inventaire']['objets']])}")
        print("-" * 60)


def afficher_menu_principal():
    """Affiche le menu principal des options disponibles."""
    menu_options = [
        "Menu de combat",
        "Afficher les personnages",
        "Modifier un personnage",
        "Créer un personnage",
        "Ajouter un objet",
        "Quitter",
    ]

    print("\nQuelle option voulez-vous choisir ?\n")
    for i, option in enumerate(menu_options, start=1):
        print(f"{i}. {option}")


def afficher_menu_combat():
    """Affiche le menu de combat avec les options disponibles."""
    options = [
        "Retour au menu principal",
        "Attaquer un personnage",
        "Utiliser une potion de soin",
        "Gagner un niveau",
        "Quitter",
    ]

    print("\nQuelle option voulez-vous choisir ?\n")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")


def creer_personnage(personnages):
    print("\nAjouter un personnage")
    personnage = {
        "nom": input("Nom : "),
        "classe": input("Classe : "),
        "niveau": 1,
        "points_de_vie": 100,
        "inventaire": {
            "objets": [
                {
                    "nom": "potion",
                    "quantité": 3
                },
            ]
        }
    }
    personnages.append(personnage)
    return personnages


def edit_personnage(personnages):
    """Edit a character."""
    index = int(input("Index: ")) - 1
    personnage = personnages[index]

    nom = input("Nom: ") or personnage["nom"]
    classe = input("Classe: ") or personnage["classe"]
    niveau = input("Niveau: ") or personnage["niveau"]

    personnage["nom"] = nom
    personnage["classe"] = classe
    personnage["niveau"] = niveau

    return personnages

# 1. Ajouter des objets à l'inventaire :
# - Créez une fonction qui permet d'ajouter un ou plusieurs objets dans l'inventaire.
def ajout_objet(personnages):
    """Ajoute un ou plusieurs objets à l'inventaire d'un personnage."""
    print("\nAjouter un objet")
    personnage_index = int(input("Index du personnage : ")) - 1
    personnage = personnages[personnage_index]

    while True:
        objet_nom = input("Nom de l'objet : ")
        objet_quantite = int(input("Quantité de l'objet : "))
        
        objet = {
            "nom": objet_nom,
            "quantité": objet_quantite
        }
        personnage["inventaire"]["objets"].append(objet)

        continuer = input("Voulez-vous ajouter un autre objet ? (o/n) : ")
        if continuer.lower() != 'o':
            break

# 2. Modifier les statistiques :
# - Le personnage gagne un niveau et 20 points de vie supplémentaires.
def gain_de_niveau(personnages, tueur_index, victime_index):
    # Vérifie si la victime est morte
    if int(personnages[victime_index]["points_de_vie"]) <= 0:
        personnage = personnages[tueur_index]
        personnage["niveau"] = str(int(personnage["niveau"]) + 1)
        personnage["points_de_vie"] = str(
            int(personnage["points_de_vie"]) + 20)
        for objet in personnage["inventaire"]["objets"]:
            if objet["nom"] == "potion":
                objet["quantité"] = str(int(objet["quantité"]) + 1)
    return personnages


def combat(personnages):
    """
    Fait combattre deux personnages entre eux.

    Args:
        personnages (list): La liste des personnages.

    Returns:
        list: La liste des personnages après le combat.
    """
    # Afficher les personnages et leurs points de vie
    for index, personnage in enumerate(personnages, start=1):
        print(f"{index}. {personnage['nom']}: {personnage['points_de_vie']} points de vie")

    # Choisir l'attaquant
    attaquant_nom = input("Quel personnage voulez-vous faire attaquer : ")
    attaquant = next((p for p in personnages if p["nom"] == attaquant_nom), None)
    if attaquant is None:
        print("Personnage introuvable")
        return personnages

    # Choisir la cible
    cible_nom = input("Quel personnage voulez-vous attaquer : ")
    cible = next((p for p in personnages if p["nom"] == cible_nom), None)
    if cible is None:
        print("Personnage introuvable")
        return personnages

    # Calculer les dégâts infligés
    niveau = int(cible["niveau"])
    degats = random.randint(1, 50) + (10 * niveau)
    cible["points_de_vie"] = int(cible["points_de_vie"]) - degats

    # Vérifier si le personnage est mort
    if cible["points_de_vie"] <= 0:
        print(f"{cible['nom']} est mort")
        # l'attaquant prend les objets de l'inventaire de la cible
        for objet in cible["inventaire"]["objets"]:
            existe = next((o for o in attaquant["inventaire"]["objets"] if o["nom"] == objet["nom"]), None)
            if existe:
                existe["quantité"] = str(int(existe["quantité"]) + int(objet["quantité"]))
            else:
                objet["quantité"] = str(int(objet["quantité"]))
                attaquant["inventaire"]["objets"].append(objet)

        personnages.remove(cible)
    else:
        cible["points_de_vie"] = str(cible["points_de_vie"])
        print(f"\n{cible['nom']} a subi {degats} points de dégâts\n")

    # Afficher l'état des personnages après le combat
    for personnage in personnages:
        print(f"{personnage['nom']} a {personnage['points_de_vie']} points de vie")

    return personnages


# 3. Utiliser une potion de soin :
# Le personnage utilise une "potion de soin".
# - Supprimez cet objet de l'inventaire.
# - Ajoutez des points de vie aléatoires entre **1** et **50**.
def utilisation_potion(personnages):
    print("\nChoisissez le personnage à soigner : ")
    for i, personnage in enumerate(personnages, start=1):
        print(f"{i}. {personnage['nom']}: {
              personnage['points_de_vie']} points de vie")
    choix = input("Entrez le numéro ou le nom du personnage : ")
    if choix.isdigit():
        index = int(choix) - 1
        personnage = personnages[index]
    else:
        for personnage in personnages:
            if personnage["nom"] == choix:
                break
        else:
            print("Personnage introuvable")
            return personnages
    for objet in personnage["inventaire"]["objets"]:
        if objet["nom"] == "potion":
            if int(objet["quantité"]) > 0:
                objet["quantité"] = str(int(objet["quantité"]) - 1)
                personnage["points_de_vie"] = str(
                    int(personnage["points_de_vie"]) + random.randint(1, 50))
            for i, personnage in enumerate(personnages, start=1):
                print(f"{i}. {personnage['nom']}: {
                      personnage['points_de_vie']} points de vie")
            else:
                print("Vous n'avez plus de potion.")
            break


def mort(personnages):
    for i, personnage in enumerate(personnages):
        if int(personnage["points_de_vie"]) <= 0:
            print(f"{personnage['nom']} est mort.")
            del personnages[i]
            break


def menu_principal(personnages):
    while True:
        afficher_menu_principal()
        choix = input("\nChoisissez une option : ")
        
        if choix.isdigit():
            choix = int(choix)
            
            if choix == 1:
                menu_combat(personnages)
            elif choix == 2:
                afficher_personnage(personnages)
                while True:
                    retour = input("\nVoulez-vous sortir ? (o/n) : ")
                    if retour.lower() == "o":
                        break
            elif choix == 3:
                edit_personnage(personnages)
            elif choix == 4:
                creer_personnage(personnages)
            elif choix == 5:
                ajout_objet(personnages)
            elif choix == 6:
                break
            else:
                print("Entrée invalide. Veuillez choisir une option valide.")
        else:
            print("Entrée invalide. Veuillez choisir une option valide.")


def menu_combat(personnages):
    while True:
        afficher_menu_combat()
        choix = int(input("\nChoisissez une option : "))
        if choix == 1:
            menu_principal(personnages)
        elif choix == 2:
            personnages = combat(personnages)
        elif choix == 3:
            personnages = utilisation_potion(personnages)
        elif choix == 4:
            personnages = gain_de_niveau(personnages)
        elif choix == 5:
            break
        else:
            print("Entrée invalide. Veuillez choisir une option valide.")


if __name__ == "__main__":
    menu_principal(personnages)
    print("\nAu revoir !")

