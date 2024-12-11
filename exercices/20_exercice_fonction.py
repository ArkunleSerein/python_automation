# Écrire un programme qui permet de saisir une chaîne d’ADN ainsi qu’une séquence d’ADN
# et qui retourne le d’occurrences de la séquence dans la chaîne
# Cette séquence sera composée uniquement de la combinaison de lettre suivante 'a', 't', 'c',
# 'g'.
#       1. Écrire une fonction vérification_adn qui permet de renvoyer la valeur True si la chaîne
#       d’ADN est valide, False si elle est invalide
#       2. Écrire une fonction saisie_adn qui récupère une saisie, vérifie sa validité et renvoie une
#       chaîne d’ADN valide sous forme de chaîne
#       3. Écrire une fonction proportion qui reçoit deux paramètres une chaîne d’ADN et une
#       séquence d’ADN Elle renverra le d’occurrences de la séquence dans la chaîne
#       4. Créer des instructions pour pouvoir tester le programme

def verification_adn(adn):
    # Vérifie si la chaîne ADN ne contient que des caractères valides 'a', 't', 'c', 'g'.
    chaine_adn = adn.lower()  # Convertir la chaîne en minuscules
    for char in chaine_adn:
        if char not in 'atcg':  # Vérifier que chaque caractère est valide
            return False
    return True


def saisie_adn():
    #Demande à l'utilisateur de saisir une chaîne d'ADN valide
    while True:
        # Utiliser strip pour enlever les espaces autour
        adn = input("Saisir une chaîne d'ADN : ").strip()
        if verification_adn(adn):
            return adn
        else:
            print("La chaîne d'ADN est invalide. Elle doit contenir uniquement 'a', 't', 'c' ou 'g'.")


def proportion(adn, sequence):
    #Retourne le nombre d'occurrences de la séquence dans la chaîne d'ADN
    # Enlever les espaces de la séquence avant de la vérifier
    # Enlever les espaces et convertir en minuscules
    sequence = sequence.replace(" ", "").lower()
    if sequence == "":  # Vérifier si la séquence est vide
        return 0
    return adn.lower().count(sequence)  # Ignorer la casse


# Test du programme
adn = saisie_adn()  # Saisie de la chaîne d'ADN
# Saisie de la séquence d'ADN
sequence = input("Saisir une séquence d'ADN : ").strip()

if verification_adn(sequence):  # Vérification de la validité de la séquence
    print(f"Le nombre d'occurrences de la séquence dans l'ADN est : {
          proportion(adn, sequence)}")
else:
    print("La séquence d'ADN est invalide. Elle doit contenir uniquement 'a', 't', 'c' ou 'g'.")
