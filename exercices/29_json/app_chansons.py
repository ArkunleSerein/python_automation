import os
import json


def affichage_menu():
    print("\n\n\n========== MENU PRINCIPAL ==========")
    print("1 : Ajouter une chanson")
    print("2 : Modifier une chanson")
    print("3 : Supprimer une chanson")
    print("4 : Afficher les chansons")
    print("5 : Quitter")


def charger_chansons():
    try:
        with open(path_file, "r", encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def sauvegarder_chansons(chansons):
    with open(path_file, "w", encoding="UTF-8") as file:
        json.dump(chansons, file, ensure_ascii=False, indent=4)


def ajout_chanson():
    print("========== AJOUTER UNE CHANSON ==========.")
    chansons = charger_chansons()
    nouvelle_chanson = {
        "Titre": input("Titre de la chanson : "),
        "Artiste": input("Artiste de la chanson : "),
        "Catégorie": input("Catégorie de la chanson : "),
        "Score": input("Score de la chanson (sur 5) : ")
    }
    chansons.append(nouvelle_chanson)
    sauvegarder_chansons(chansons)
    print("La chanson a bien été ajoutée.")


def modifier_chanson():
    print("========== MODIFIER UNE CHANSON ==========.")
    chansons = charger_chansons()
    for index, chanson in enumerate(chansons):
        print(f"{index + 1} : {chanson.get("Titre")} - {chanson.get("Artiste")}")
    choix = int(input("Quel est votre choix ? ")) - 1
    if 0 <= choix < len(chansons):
        chanson = chansons[choix]
        chanson["Titre"] = input("Titre de la chanson : ")
        chanson["Artiste"] = input("Artiste de la chanson : ")
        chanson["Catégorie"] = input("Catégorie de la chanson : ")
        chanson["Score"] = input("Score de la chanson (sur 5) : ")
        sauvegarder_chansons(chansons)
        print("La chanson a bien été modifiée.")
    else:
        print("Entrée invalide. Veuillez choisir une option valide.")


def supprimer_chanson():
    print("========== SUPPRIMER UNE CHANSON ==========.")
    chansons = charger_chansons()
    for index, chanson in enumerate(chansons):
        print(f"{index + 1} : {chanson.get("Titre")} - {chanson.get("Artiste")}")
    choix = int(input("Quel est votre choix ? ")) - 1
    if 0 <= choix < len(chansons):
        chansons.pop(choix)
        sauvegarder_chansons(chansons)
        print("La chanson a bien été supprimée.")
    else:
        print("Entrée invalide. Veuillez choisir une option valide.")


def affichage_chansons():
    print("========== AFFICHAGE DES CHANSONS ==========.")
    chansons = charger_chansons()
    for index, chanson in enumerate(chansons):
        print(f"{index + 1} : {chanson.get("Titre")} - {chanson.get("Artiste")}")
        print(f"Catégorie : {chanson.get("Catégorie")}")
        print(f"Score : {chanson.get("Score")}")
        print("------------------")


def main():
    while True:
        affichage_menu()
        choix = input(
            "====================================\nQuel est votre choix ? ""\n")
        if choix == "1":
            ajout_chanson()
        elif choix == "2":
            modifier_chanson()
        elif choix == "3":
            supprimer_chanson()
        elif choix == "4":
            affichage_chansons()
        elif choix == "5":
            break
        else:
            print("Entrée invalide. Veuillez choisir une option valide.")


if __name__ == "__main__":
    os.makedirs("datas", exist_ok=True)
    path_file = os.path.join("datas", "music.json")
    main()
