# On initialise une liste avec des crochets :
# index :   0  1  2     3     4           5
ma_liste = [3, 2, 6, "test", True, ["a", "b", "c"]]

print(ma_liste)

# Afficher un élément de la liste (elle commence à l'index 0)
print(ma_liste[3])
print(ma_liste[5])

# Pour afficher un élément d'une liste dans une liste :
print(ma_liste[5][1])

# Modifier une élément de ma liste :
ma_liste[4] = 10
print(ma_liste)

list_nb = [5, 2, 4, 7, 1, 18]
# Pour trier une liste :
list_nb.sort()
print(list_nb)

# Pour ajouter une valeur à la fin de ma liste :
list_nb.append(30)
print(list_nb)

# Pour ajouter à un index précis
list_nb.insert(2, 10)
print(list_nb)

# Pour ajouter plusieurs valeurs en une fois :
list_nb.extend([5, 6, 7, 8])
print(list_nb)

# Pour retirer un élément de ma liste via son index
list_nb.pop(2)
print(list_nb)

# Pour retirer un élément avec son contenu (supprime uniquement le premier trouvé)
list_nb.remove(7)
print(list_nb)

# Pour itérer sur une liste
for element in list_nb:
    print(element)