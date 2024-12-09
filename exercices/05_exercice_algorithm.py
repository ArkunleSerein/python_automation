# On crée la variable "saisi" avec un input afin de saisir le nombre voulu.
nb_saisi = int(input("Veuillez saisir un nombre entier : "))
# On crée ensuite la variable résutat qui va contenir la formule demandée
resultat = nb_saisi % 3 == 0


# on crée un algorithme qui renvoi la phrase "Le nombre est divisible par 3" si le modulo == 0 
# sinon il renvoit "Le nombre n'est pas divisible par 3".
if resultat:
    print("Le nombre est divisible par 3")
else:
    print("Le nombre n'est pas divisible par 3")