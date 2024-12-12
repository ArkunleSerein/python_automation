def hello_world():
    print("Hello world !")

hello_world()

def bonjour(prenom):
    print(f"Bonjour {prenom}")

bonjour("Toto")
bonjour("Tata")
bonjour("Titi")

def bonjour_toto(prenom="toto"): # prenom est facultatif
    print(f"Bonjour {prenom}")

bonjour_toto("test")
bonjour_toto()

def addition(nb1, nb2):
    print(f"Je calcul {nb1} + {nb2}")
    resultat = nb1 + nb2
    return resultat

resultat = addition(10, 50)
resultat2 = addition(58, 15)
print(resultat, resultat2)

def pair_ou_impair(nombre):
    if nombre % 2 == 0:
        return "oui"
    else:
        return "non"
    
print(pair_ou_impair(2))
print(pair_ou_impair(3))