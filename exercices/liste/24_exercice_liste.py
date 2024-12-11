# Une année s'est écoulée et la nouvelle édition de la course de module de Tatooine est encore plus captivante.
# Cette année, la position de chaque concurrent est stockée dans une liste. (on y mettre le nom des concurrents)
# Parmi les moments phares de cette édition il y a :
# Une panne moteur fait passer le premier concurrent à la dernière position.
# Le second concurrent accélère et prend la tête de la course.
# Le dernier concurrent sauve l'honneur et dépasse l'avant-dernier module de la course.
# Un tir de blaster élimine le module en tête de la course.
# Dans un spectaculaire retournement de situation, un module qu'on pensait éliminé fait son grand retour à la dernière
# position.
# Créer la fonction panne_moteur, modifiant la liste passée en argument de manière à ce que le premier module passe
# dernier, le deuxième premier et ainsi de suite.
# Créer la fonction passe_en_tete, modifiant la liste passée en argument de manière à ce que le premier module passe
# deuxième et le deuxième premier.
# Créer la fonction sauve_honneur, modifiant la liste passée en argument de manière à ce que le dernier module passe avant
# dernier et l'avant dernier dernier.
# Créer la fonction tir_blaster, enlevant le premier concurrent de la liste passée en argument.
# Compléter la fonction retour_inattendu , ajoutant un concurrent à la fin de la liste passée en argument.

def afficher_classement(liste):
    """
    Affiche le classement de la course avec des numéros de position.
    """
    print("Classement actuel :")
    for index, concurrent in enumerate(liste, start=1):
        print(f"{index}. {concurrent}")


def panne_moteur(liste):
    """
    Déplace le premier module à la dernière position de la liste.
    Si la liste est vide ou ne contient qu'un élément, rien n'est fait.
    """
    if len(liste) > 1:
        liste.append(liste.pop(0))


def passe_en_tete(liste):
    """
    Échange le premier et le deuxième module de la liste.
    Si la liste ne contient pas au moins deux éléments, rien n'est fait.
    """
    if len(liste) > 1:
        liste[0], liste[1] = liste[1], liste[0]


def sauve_honneur(liste):
    """
    Échange les positions du dernier et de l'avant-dernier module.
    Si la liste contient moins de deux éléments, rien n'est fait.
    """
    if len(liste) > 1:
        liste[-2], liste[-1] = liste[-1], liste[-2]


def tir_blaster(liste):
    """
    Supprime le premier module de la liste et le sauvegarde comme module éliminé.
    Si la liste est vide, rien n'est fait.
    """
    global module_elimine  # Variable globale pour mémoriser le module éliminé
    if liste:
        module_elimine = liste.pop(0)


def retour_inattendu(liste):
    """
    Fait revenir le module éliminé en l'ajoutant à la fin de la liste.
    Si aucun module n'a été éliminé, rien n'est fait.
    """
    global module_elimine
    if 'module_elimine' in globals():  # Vérifie si un module a été éliminé
        liste.append(module_elimine)
        del module_elimine  # Supprime la variable après le retour du module


# Programme principal
if __name__ == "__main__":
    # Liste initiale des concurrents
    liste = ["Luke", "Leia", "Han", "Chewbacca", "R2-D2"]

    # Affichage initial du classement
    print("Avant la course :")
    afficher_classement(liste)

    # Exécution des actions de la course

    # Exemple d'utilisation de la fonction panne_moteur
    print("\nAction: panne moteur (le premier module passe en dernier)")
    panne_moteur(liste)
    afficher_classement(liste)

    # Exemple d'utilisation de la fonction passe_en_tete
    print("\nAction: passe en tête (le deuxième module prend la tête)")
    passe_en_tete(liste)
    afficher_classement(liste)

    # Exemple d'utilisation de la fonction sauve_honneur
    print("\nAction: sauve honneur (le dernier module dépasse l'avant-dernier)")
    sauve_honneur(liste)
    afficher_classement(liste)

    # Exemple d'utilisation de la fonction tir_blaster
    print("\nAction: tir de blaster (le premier module est éliminé)")
    tir_blaster(liste)
    afficher_classement(liste)

    # Exemple d'utilisation de la fonction retour_inattendu
    print("\nAction: retour inattendu (le module qui a subi le tir fait son grand retour)")
    retour_inattendu(liste)
    afficher_classement(liste)
