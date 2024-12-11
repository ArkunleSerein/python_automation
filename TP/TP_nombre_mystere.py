import random

# Générer un nombre mystère entre 1 et 100
nb_mystere = random.randint(1, 100)
nb_essai = 10

print("Devine le nombre mystère entre 1 et 100.")
print(f"Tu as {nb_essai} essais pour deviner le nombre.")

# Initialiser la variable pour suivre l'écart précédent
ancien_ecart = None

# Boucle principale du jeu
while nb_essai > 0:
    # Demander au joueur d'entrer un nombre
    try:
        nb_joueur = int(input("Fais ton choix : "))
    except ValueError:
        print("Entre un nombre valide.")
        continue  # Si l'utilisateur entre autre chose qu'un nombre, on recommence l'itération

    # Vérification de la réponse du joueur
    if nb_joueur == nb_mystere:
        print(f"Bravo avec {
              nb_joueur} ! Tu as trouvé le nombre mystère {nb_mystere}.")
        break
    elif nb_joueur < nb_mystere:
        print("Trop petit !")
    else:
        print("Trop grand !")

    # Calcul de la différence absolue entre l'essai du joueur et le nombre mystère
    ecart = abs(nb_joueur - nb_mystere)

    # Si l'on a un essai précédent, comparer l'écart avec celui-ci
    if ancien_ecart is not None:
        if ecart < ancien_ecart and nb_mystere - 5 <= nb_joueur <= nb_mystere + 5:
            # L'écart a diminué et on est dans l'intervalle de 5
            print("Tu te réchauffes !")
        elif ecart > ancien_ecart and nb_mystere - 5 <= nb_joueur <= nb_mystere + 5:
            # L'écart a augmenté et on est dans l'intervalle de 5
            print("Tu te refroidis !")

    # Mémoriser l'écart actuel pour le comparer au prochain essai
    ancien_ecart = ecart

    # Décrémenter le nombre d'essais restants
    nb_essai -= 1

    # Afficher le nombre d'essais restants
    if nb_essai > 0:
        print(f"Il te reste {nb_essai} essais.")
    else:
        print(f"Tu as perdu ! Le nombre mystère était {nb_mystere}.")
