age = int(
    input("Quelle âge avez vous ? "))
# On crée une variable qui enregistre les entrées "l'âge de l'enfant" de l'utilisateur
salaire = int(
    input("Salaire souhaité ? "))
# On crée une variable qui enregistre les entrées "l'âge de l'enfant" de l'utilisateur
experience = int(
    input("Combien d'année d'expérience avez vous ? "))
# On crée une variable qui enregistre les entrées "l'âge de l'enfant" de l'utilisateur

a = age
s = salaire
e = experience

if  a <= 30:
    print("La personne n'a pas l'âge minimum pour candidater")
elif s >= 40000:
    print("La personne demande un salaire trop élevé pour candidater")
elif e <= 5:
    print("La personne n'a pas assez d'expérience pour candidater")
else: 
    print("Le profil de cette personne est valable pour une candidature")



