import csv
import os

# Écrire un script qui demande les informations d'un produit :
# Titre
# Prix
# Stock
# Il les ajoute ensuite dans un fichier produits.csv

def creation_fichier():
    if not os.path.exists(path_file):
        with open(path_file, "w", newline="", encoding="UTF-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Nom", "Prix", "Stock"])

def ajout_produit():
    with open(path_file, "a", newline="", encoding="UTF-8") as file:
        writer = csv.writer(file)
        nom = input("Quel est le nom du produit ? ")
        prix = input("Quel est le prix du produit ? ")
        stock = input("Quel est le stock du produit ? ")
        writer.writerow([nom, prix, stock])
    print("Le produit a bien été ajouté.")

def modifier():
    nom = input("Quel est le nom du produit à modifier ? ")
    prix = input("Quel est le nouveau prix du produit ? ")
    stock = input("Quel est le nouveau stock du produit ? ")
    
    with open(path_file, "r", newline="", encoding="UTF-8") as file:
        reader = csv.reader(file)
        produits = list(reader)

    with open(path_file, "w", newline="", encoding="UTF-8") as file:
        writer = csv.writer(file)
        for produit in produits:
            if produit[0] == nom:
                produit[1] = prix
                produit[2] = stock
            writer.writerow(produit)
    print("Le produit a bien été modifié.")

def supprimer():
    nom = input("Quel est le nom du produit à supprimer ? ")
    
    with open(path_file, "r", newline="", encoding="UTF-8") as file:
        reader = csv.reader(file)
        produits = list(reader)

    with open(path_file, "w", newline="", encoding="UTF-8") as file:
        writer = csv.writer(file)
        for produit in produits:
            if produit[0] != nom:
                writer.writerow(produit)
    print("Le produit a bien été supprimé.")
    
def affichage_produits():
    with open(path_file, "r", newline="", encoding="UTF-8") as file:
        reader = csv.reader(file)
        produits = list(reader)

    for produit in produits:
        print(f"Nom : {produit[0]}")
        print(f"Prix : {produit[1]}")
        print(f"Stock : {produit[2]}")
        print("------------------")

def affichage_menu():
    print("Bienvenue dans le menu de gestion des produits.")
    print("1 : Ajouter un produit")
    print("2 : Modifier un produit")
    print("3 : Supprimer un produit")
    print("4 : Afficher les produits")
    print("5 : Quitter")

def menu():
    creation_fichier()
    while True:
        affichage_menu()
        choix = input("Quel est votre choix ? ")
        if choix == "1":
            ajout_produit()
        elif choix == "2":
            modifier()
        elif choix == "3":
            supprimer()
        elif choix == "4":
            affichage_produits()
        elif choix == "5":
            break
        elif choix != "1" or choix != "2" or choix != "3" or choix != "4" or choix != "5":
            print("Entrée invalide. Veuillez choisir une option valide.")
        else:
            print("Entrée invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    path_file = "produits.csv"
    menu()

