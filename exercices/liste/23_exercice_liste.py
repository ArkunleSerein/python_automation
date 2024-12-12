# Exercice 23 : Saisie et gestion des notes

# Fonction pour saisir les notes
def saisie_notes():
    """
    Fonction qui permet de saisir des notes. L'utilisateur peut choisir entre saisir un nombre de note
    définie ou saisir un nombre négatif pour quitter.
    """
    notes = [] 
    
    print("\n\n                Bienvenue dans l'application de saisie et gestion de notes.\n")

    print("\n     MENU : OPTION DE SAISI DE NOTE\n")
    print("1 : Saisir un nombre de note définie")
    print("2 : Saisir un nombre négatif pour quitter\n")
    choix = int(input("Choisissez une option : "))

    if choix == 1:
        # Saisir un nombre de note définie
        nb_notes = int(input("\n1 : Saisir un nombre de note définie\n\nEntrez le nombre de notes que vous souhaitez saisir : "))
        i = 0
        while i < nb_notes:
            note = int(input(f"Veuillez saisir la note n°{f"{i + 1}/{nb_notes}"} (entre 0 et 20): "))
            if note < 0:  
                print("Entrée invalide. La note ne peut pas être négative.")
                continue
            if note > 20:  
                print("Entrée invalide. La note ne peut pas être supérieure à 20.")
                continue
            notes.append(note) 
            i += 1
        return notes


    if choix == 2:
        # Saisir un nombre négatif pour quitter
        print("\n2 : Saisir un nombre négatif pour quitter\n\nSaisissez un nombre négatif pour quitter.")
        while True:
            try:
                note = int(input(f"Veuillez saisir la note n°{len(notes) + 1} (entre 0 et 20): "))
                if note < 0:  
                    break
                if note > 20: 
                    print("Entrée invalide. La note ne peut pas être supérieure à 20.")
                    continue
                notes.append(note)  
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre entier.")
        return notes

# Fonction pour afficher les notes
def affichage_notes(notes):
    """
    Fonction qui permet d'afficher les notes. L'utilisateur peut choisir entre afficher les notes,
    afficher la note maximale, afficher la note minimale, afficher la moyenne des notes ou quitter
    l'application.
    """
    if not notes:  
        print("Aucune note saisie.")
        return

    print("\n    MENU D'AFFICHAGE DE NOTES:\n")
    print("1 : Afficher les notes")
    print("2 : Afficher la note maximale")
    print("3 : Afficher la note minimale")
    print("4 : Afficher la moyenne des notes")
    print("5 : Quitter l'application\n")

    while True:
        try:
            choix = int(input("\nVeuillez choisir une option (1-5) : "))
            if choix == 1:
                print(
                    f"\n1 : Afficher les notes\n\nLes notes saisies sont : {notes}")
            elif choix == 2:
                print(f"\n2 : Afficher la note maximale\n\nLa note maximale est : {
                      max(notes)} / 20")
            elif choix == 3:
                print(f"\n3 : Afficher la note minimale\n\nLa note minimale est : {
                      min(notes)} / 20")
            elif choix == 4:
                moyenne = sum(notes) / len(notes)
                print(f"\n4 : Afficher la moyenne des notes\n\nLa moyenne des notes est : {
                      moyenne:.2f} / 20")
            elif choix == 5:
                print("\n5 : Quitter l'application\n\nMerci d'avoir utilisé l'application ! À bientôt.")
                break
            else:
                print("Option invalide. Veuillez choisir une option entre 1 et 5.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier entre 1 et 5.")


# Programme principal
if __name__ == "__main__":
    notes = saisie_notes()  
    affichage_notes(notes)  

