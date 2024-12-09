# On demande à l'utilisateur d'entrer le nombre de photocopie souhaité
nb_copy_todo = int(input("Veuillez saisir le nombre de copie que vous souhaitez : "))
i = nb_copy_todo

if  i <= 0:
    price = 0
    # Si le nombre de copie est <= 0 alors le price sera = à 0
elif i < 10:
    price = 0.5 * i 
    # Si le nombre de copie est inférieur à 10 alors le nombre de copie est * par 0.5€
elif 10 >= i <= 20: 
    price = 0.4 * i
    # Si le nombre de copie est compris entre 10 et 20  alors le nombre de copie est * par 0.4€
elif i > 20: 
    price = 0.3 * i 
    # Si le nombre de copie est supérieur à 20 alors le nombre de copie est * par 0.3€
print(f"Vous devez payez la somme de : {price} €")# affiche le prix 

