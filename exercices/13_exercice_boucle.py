# Réaliser un programme permettant à l'utilisateur d'entrer comme
# données:
# Une population initiale.
# Un taux d'accroissement
# Une population visée.
# Ce programme permettra à l'utilisateur de savoir en combien de
# temps la population visée sera atteinte.

p = int(input("Population initial : "))  
t = float(input("Le taux d'accroissement: "))  
Pv = int(input("Population visée : "))

n = 0  # valeur initial de l'année

# Si la population initiale est inférieur à la population visée on continue la boucle
while p < Pv:
    p *= (1 + t)  # On applique le taux d'accroissement à la population chaque année
    n += 1

print(
    f"Le nombre d'années nécessaires pour doubler le capital est : {n} années")
