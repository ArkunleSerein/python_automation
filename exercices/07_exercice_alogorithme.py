# Écrire un algorithme qui demande l'âge d'un enfant à l'utilisateur,
# ensuite, il l'informe de sa catégorie pour une licence sportive :
# 'Baby' entre 3 et 6 ans.
# 'Poussin' entre 7 et 8 ans.
# 'Pupille' entre 9 et 10 ans.
# 'Minime' entre 11 et 12 ans.
# 'Cadet' à partir de 13 ans.

age_enfant = int(
    input("Quelle âge à votre enfant ? "))
# On crée une variable qui enregistre les entrées "l'âge de l'enfant" de l'utilisateur

a = age_enfant
# On crée une variable qui copie age_enfant pour la lisibilité du code

if 0 <= a < 3:
    cat = "Votre enfant est encore trop jeune pour s'inscrire"
# Si l'âge de l'enfant est inférieur à 3 alors le message "Votre enfant est encore trop jeune pour s'inscrire" s'affichera
elif a <= 6:
    cat = "Baby"
# Si l'âge de l'enfant est inférieur à 6 alors la catégorie "Baby" s'affichera
elif a <= 8:
    cat = "Poussin"
# Si l'âge de l'enfant est inférieur à 8 alors la catégorie "Poussin" s'affichera
elif a <= 10:
    cat = "Pupille"
# Si l'âge de l'enfant est inférieur à 10 alors la catégorie "Pupille" s'affichera
elif a <= 12:
    cat = "Minime"
# Si l'âge de l'enfant est inférieur à 12 alors la catégorie "Minime" s'affichera
elif a >= 13:
    cat = "Cadet"
# Si l'âge de l'enfant est inférieur à 12 alors la catégorie "Cadet" s'affichera

print(f"Votre enfant est dans la catégorie sportive : {cat}") 
# On affiche la catégorie de l'enfant selon son âge.
