# Écrire une fonction compter_lettre_a.
# Cette fonction prendra en paramètre une chaîne
# Créer une boucle qui parcourt les lettres de la chaîne et compte le
# nombre de lettres égales à "a".
# La fonction renverra un entier.
# exemple: compter_lettre_a("abba")  # résultat : 2
# exemple: compter_lettre_a("mixer")  # résultat : 0
# Écrire une autre fonction sans boucle qui utilisera count à la place.


def compter_lettre_a(chaine):
    return f"il y a {chaine.lower().count('a')} lettre(s) 'a' dans la chaine {chaine}"


input = input("Saisir une chaîne : ")
print(compter_lettre_a(f"{input}"))
