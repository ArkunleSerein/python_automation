# Écrire un algorithme qui déclare et stocke dans un tableau 10
# chiffres, puis affiche le 9éme élément de ma liste.
import random

# Création de la liste
liste = [random.randint(1, 100) for _ in range(10)]
print(f"ma liste = {liste}")

# Affichage du 9éme élément de la liste
print(f"Le 9 ème élément de ma liste = {liste[8]}")