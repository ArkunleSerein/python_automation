# Création des variables contenant les inputs avec les fonctions upper(permet de forcer les majuscules) et capitalize(permet de mettre la première lettre en majuscule)
nom = str(input("Veuillez entrer votre nom : ").upper())
prenom = str(input("Veuillez entrer votre prénom : ").capitalize())

# Création de la variable affichage qui va permettre de 
affichage = f"Bonjour M. Ou Mme {nom} {prenom}"

print(affichage)
