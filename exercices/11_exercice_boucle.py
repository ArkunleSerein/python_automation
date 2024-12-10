# Soit un capital c placé à un taux t. On veut connaître le nombre
# d'années nécessaire au doublement de ce capital.

c = int(input("Capital actuel : ")) # la variable c la valeur du capital
t = float(input("Le taux : "))  # la variable t le taux associé
n = (c, t)  # la variable n le nombre d'année

Cn = c # valeur du capital * le nombre d'année
n = 0 # valeur initial de n

while Cn < 2 * c: # Si Cn est inférieur à 2*c on continue le calcul Cn *= (1 + t) 
    Cn *= (1 + t)  # On applique le taux d'accroissement chaque année
    n += 1

print(f"Combien de temps la population sera atteinte : {n} années")
