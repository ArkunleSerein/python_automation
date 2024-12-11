import random

# print("Bienvenue dans le jeu du Nombre Mystère !")
# minimum = 1
# maximum = 100
# nombre_mystere = random.randint(minimum, maximum)
# essais_restants = 5


# while essais_restants > 0:
#     print(f"Il vous reste {essais_restants} essais.")
    
    # while True:
    #     # try ... except permet de gérer les erreurs afin d'éviter une coupure non désirée de notre application.
    #     try:
    #         proposition = int(input(f"Devinez le nombre mystère entre {minimum} et {maximum} : "))
    #         if minimum <= proposition <= maximum:
    #             break
    #         else:
    #             print(f"Erreur, veuillez saisir un nombre entre {minimum} et {maximum}")
    #     except Exception as e:
    #         print(e)
    
    # if proposition == nombre_mystere:
    #     print("Bravo ! Vous avez deviné le nombre mystère !")
    #     exit()
    # elif proposition < nombre_mystere:
    #     print("Le nombre mystère est plus grand.")
    # else:
    #     print("Le nombre mystère est plus petit.")
    
#     essais_restants -= 1

# if essais_restants == 0:
#     print(f"Vous avez épuisé tous vos essais. Le nombre mystère était {nombre_mystere}.")

# Avec des fonctions :


def choisir_nb_mystere(minimum, maximum):
    # nombre_mystere = random.randint(minimum, maximum)
    return random.randint(minimum, maximum)

def choix_utilisateur(minimum, maximum):
    while True:
        # try ... except permet de gérer les erreurs afin d'éviter une coupure non désirée de notre application.
        try:
            proposition = int(input(f"Devinez le nombre mystère entre {minimum} et {maximum} : "))
            if minimum <= proposition <= maximum:
                return proposition
            else:
                print(f"Erreur, veuillez saisir un nombre entre {minimum} et {maximum}")
        except Exception as e:
            print(e)

def verifier_proposition(proposition, nombre_mystere):
    if proposition == nombre_mystere:
        print("Bravo ! Vous avez deviné le nombre mystère !")
        exit()
    elif proposition < nombre_mystere:
        print("Le nombre mystère est plus grand.")
    else:
        print("Le nombre mystère est plus petit.")

def jeu_nb_mystere():
    print("Bienvenue dans le jeu du Nombre Mystère !")
    minimum = 1
    maximum = 100
    nombre_mystere = choisir_nb_mystere(minimum, maximum)
    essais_restants = 5

    while essais_restants > 0:
        print(f"Il vous reste {essais_restants} essais.")
        proposition = choix_utilisateur(minimum, maximum)

        verifier_proposition(proposition, nombre_mystere)
        essais_restants -= 1
    
    if essais_restants == 0:
        print(f"Vous avez épuisé tous vos essais. Le nombre mystère était {nombre_mystere}.")


jeu_nb_mystere()