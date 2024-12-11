# Écrire un programme qui prend en entrée une température temp et qui
# renvoie l'état de l'eau à cette température c'est-à-dire "SOLIDE", "LIQUIDE"
# ou "Gazeux".
# On prendra comme conditions les suivantes :
# Si la température est strictement négatives alors l'eau est à l'état solide.
# Si la température est entre 0 et 100 (compris) l'eau est à l'état liquide.
# Si la température est strictement supérieur à 100 l'eau est à l'état gazeux.
# Il est possible de réaliser cet exercice sans if imbriqué grâce au elif

temp = float(
    input("Entrer la température de l'eau : "))
# On crée une variable qui enregistre les entrées "la température de l'eau" de l'utilisateur

if temp < 0:
    etat = "solide"
# Si la température de l'eau est strictement inférieur à 0 alors le message "solide" s'affichera
elif temp <= 100:
    etat = "liquide"
# Si la température de l'eau est compris entre 0 et 100 alors l'état "liquide" s'affichera
else:
    etat = "gazeux"
# Si la température de l'eau est strictement supérieur à 100 alors la catégorie "gazeux" s'affichera

print(f"L'état de l'eau à {temp}°C est {etat}")
# On affiche l'état de l'eau' à la température donnée.
