# Via l'utilisation d'une variable de type liste, vous devrez réaliser un logiciel permettant à l'utilisateur
# d'entrer une série de notes, dont le nombre possible à entrer sera soit (au choix de l'utilisateur) :
# saisie avant la saisie de notes
# permissif et pourra aller jusqu'à entrer une note négative qui stoppera la saisie des notes.
# Une fois la saisie des notes terminée, l'utilisateur aura à sa disposition un affichage lui permettant
# d'avoir la note max, la note min ainsi que la moyenne (possible de faire un menu pour choisir)

def saisie_notes():
    """
    Fonction qui permet de saisir des notes. L'utilisateur peut entrer une
    note positive, et lorsqu'il entre une note négative, la saisie s'arrête.
    """
    notes = []  # Liste pour stocker les notes
    print("Bienvenue dans l'application de saisie de notes.")
    print("Veuillez entrer les notes une par une. Entrez une note négative pour terminer.\n")

    while True:
        try:
            # Demander une note à l'utilisateur
            note = int(input(f"Veuillez saisir la note n°{len(notes) + 1}: "))
            if note < 0:  # Si la note est négative, on arrête la saisie
                break
            notes.append(note)  # Ajouter la note à la liste
        except ValueError:
            # Gérer l'exception si l'utilisateur entre autre chose qu'un nombre
            print("Entrée invalide. Veuillez entrer un nombre entier.")
    return notes


def affichage_notes(notes):
    """
    Fonction qui affiche un menu pour afficher les notes saisies, la note
    maximale, minimale ou la moyenne, et permet de quitter l'application.
    """
    if not notes:  # Si la liste est vide, on affiche un message
        print("Aucune note saisie.")
        return

    print("\nMenu des options :")
    print("1 : Afficher les notes")
    print("2 : Afficher la note maximale")
    print("3 : Afficher la note minimale")
    print("4 : Afficher la moyenne des notes")
    print("5 : Quitter l'application")

    while True:
        try:
            # Demander à l'utilisateur de choisir une option
            choix = int(input("\nVeuillez choisir une option (1-5) : "))
            if choix == 1:
                print(f"Les notes saisies sont : {notes}")
            elif choix == 2:
                print(f"La note maximale est : {max(notes)}")
            elif choix == 3:
                print(f"La note minimale est : {min(notes)}")
            elif choix == 4:
                moyenne = sum(notes) / len(notes)
                print(f"La moyenne des notes est : {moyenne:.2f}")
            elif choix == 5:
                print("Merci d'avoir utilisé l'application ! À bientôt.")
                break
            else:
                print("Option invalide. Veuillez choisir une option entre 1 et 5.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier entre 1 et 5.")


# Programme principal
if __name__ == "__main__":
    notes = saisie_notes()  # Appel de la fonction pour saisir les notes
    affichage_notes(notes)  # Appel de la fonction pour afficher les options


