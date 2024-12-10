# Réaliser un programme permettant à l'utilisateur d'entrer comme
# données:
# Une population initiale.
# Un taux d'accroissement
# Une population visée.
# Ce programme permettra à l'utilisateur de savoir en combien de
# temps la population visée sera atteinte.

p = int(input("Population initial : "))  
t = float(input("Le taux d'accroissement(en %) : "))  
Pv = int(input("Population visée : "))

Tp = t / 100 # Converti le taux en %
n = 2025  # valeur initial de l'année

# Si la population initiale est inférieur à la population visée on continue la boucle
while p < Pv:
    p *= (1 + Tp)  # On applique le taux d'accroissement à la population chaque année
    n += 1

print(f"La population atteindra {Pv} d'individu en {n}")
