# Création de la variable "ma_recuperation" avec un input de récupération
ma_recuperation = input("Veuillez entrer une valeur : ")
# Affiche la variable avec les données récupérées
print("Vous avez entrer comme valeur :", ma_recuperation)


# Récupération d'une valeur par mon utilisateur :
nb = input("Veuillez saisir un nombre : ")
print(nb)
print(type(nb))

# Le cast de variable ( passer d'un type de variable à un autre) 
nb = int(nb)
print(type(nb))

# Cast et input en une ligne
nb = int(input("Veuillez saisir un autre nombre : "))
print(type(nb))


nb_a = int(nb)
nb_b = int(input("Veuillez saisir un autre nombre : "))
# formater
print(f"le nombre a est de : {nb_a}, le nombre_b est de : {nb_b}")

mon_nombre = int(input("Veuillez entrer un nombre : "))

print(f"Mon nombre vaut {mon_nombre} et est de type {type(mon_nombre)}")