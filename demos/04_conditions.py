# crée la variable qui contient l'âge légal
age_legal_fr = 18
age_legal_usa = 21
# Crée la variable qui contient l'âge de la personne
age = (int(input("Saisissez votre âge : ")))


if age >= age_legal_fr:
    print("Vous êtes majeur en France")
elif age >= age_legal_usa:
    print("Vous êtes majeur aux USA")
else:
    print("Vous êtes mineur")
