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
    print("Classement :\n")
    for index, concurrent in enumerate(liste, start=1): # Enumération de la liste
        print(f"{index}. {concurrent}") # Affichage de l'index et du concurrent

def panne_moteur(liste):
    if len(liste) > 1:  # Vérifie si la liste contient au moins deux modules
        liste.append(liste.pop(0)) # Ajoute le premier module à la fin de la liste

def passe_en_tete(liste):
    if len(liste) > 1:
        liste[0], liste[1] = liste[1], liste[0] # Echange les deux premiers modules

def sauve_honneur(liste):
    if len(liste) > 1:
        liste[-2], liste[-1] = liste[-1], liste[-2] # Echange les deux derniers modules

def tir_blaster(liste):
    global module_elimine  # Variable globale pour mémoriser le module éliminé
    if liste:
        module_elimine = liste.pop(0) # Enlève le premier module de la liste

def retour_inattendu(liste):
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
