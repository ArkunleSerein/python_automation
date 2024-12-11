nb = int(input("Choisissez un nombre entre 1 et 3 : "))

# Tant que nb n'est pas entre 1 et 3, on redemande un nombre
while nb < 1 or nb > 3:
    nb = int(input("Erreur ! Choisissez un nombre entre 1 et 3 : "))

print(f"Vous avez choisi le nombre {nb}.")
