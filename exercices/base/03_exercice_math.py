# On importe la bibliothèque math
from math import *

# On crée les variables rayon et hauteur qui vont contenir les nombres
rayon = float(input("Saisir la hauteur du cône : "))
hauteur = float(input("Saisir le rayon du cône : "))

# On crée la variable volume qui va contenir le calcul du volume d'un cône droit
# ajout de la fonction round(,2) qui arondi le résultat 2 chiffres après la virgule
volume = round((pi * pow(rayon, 2)) * (hauteur / 3), 2)

# On crée une variable qui contient le résultat du calcul, contenu dans la variable volume
resultat = f"Le volume du cône est égal à {volume}"

# On appelle la variable volume sour forme d'Integer
print(resultat)