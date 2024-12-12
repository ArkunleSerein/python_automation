# Écrire un programme se servant d'une fonction retournant, à partir
# de deux nombres lui étant envoyés en paramètres :
# La somme
# La différence
# Le quotient
# Le produit
# Vous testerez cette fonction dans le cadre d'un programme console
# demandant à l'utilisateur deux valeurs et lui permettant d'obtenir
# les 4 résultats en même temps.


def operations(a, b): # Création de la fonction prenant 2 paramètres a, b et renvoyant un tuple
    addition = f"La somme ={(a + b)}"
    soustraction = f"La différence = {(a - b)}"
    division = a / b
    multiplication = a * b
    mon_tuple = (f"La somme = {addition}"), (f"La différence = {soustraction}"), (f"Le quotient = {division}"), (f"Le produit = {multiplication}")
    return (mon_tuple) 


a = int(input("Saisir un nombre : "))
b = int(input("Saisir un deuxième nombre : "))


if __name__ == "__main__":

    print(operations(a, b))



