# On importe le module random
import random

# On crée la fonction soustraire
# On crée une variable qui contient les paramètres de la fonction
def soustraire(a, b):
    return print((f"Je soustrais {a} à {b} = "), a - b)

soustraire(random.randint(1, 100), random.randint(1, 100))