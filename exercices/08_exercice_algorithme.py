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
