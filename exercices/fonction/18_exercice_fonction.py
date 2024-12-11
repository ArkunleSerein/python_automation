# Écrire une fonction quelle_heure.
# Cette fonction aura un paramètre heure de type str.
# Ce paramètre aura "12h00" comme valeur par défaut.
# La fonction ne retournera aucun résultat mais affichera l'heure
# avec la fonction print()
# exemple : quelle_heure() # résultat : "il est 12h00"
# exemple : quelle_heure("14h00") # résultat : "il est 14h00"
import datetime

# Fonction quelle_heure avec un paramètre par défaut
def quelle_heure(heure="12h00"):
    print(f"Il est {heure} ?")

# Exécute la fonction
quelle_heure()

# Fonction heure_actuelle pour obtenir l'heure actuelle au format 24h
def heure_actuelle():
    # Retourne l'heure actuelle sous la forme HHhMM
    maintenant = datetime.datetime.now()
    return f"{maintenant.hour:02d}h{maintenant.minute:02d}"

# Fonction question_reponse qui compare l'heure actuelle avec celle fournie par quelle_heure
def question_reponse():
    # On récupère l'heure actuelle
    actuelle = heure_actuelle()

    # Si l'heure fournie par quelle_heure est différente de l'heure actuelle
    if actuelle != "12h00":  
        print("Non ! il est", actuelle)
    else:
        print("Oui ! il est", actuelle)

# Exécute la fonction
question_reponse()
