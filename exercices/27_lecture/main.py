import os

def creation_fichier():
    with open(path_file, 'w', encoding="UTF-8") as f:
        pass

def affichage_menu_texte_secret():
    print("""
    1. voir le secret
    2. Modifier le secret
    3. Sauvegarder et quitter le programme 
    """)

def voir_le_secret():
    with open(path_file, "r") as file:
        print(file.read())

def modifier_le_secret():
    with open(path_file, "w") as file:
        secret = input("Quel est le secret ? ")
        file.write(secret)

def main():
    if not os.path.exists(path_file):
        creation_fichier()
    while True:
        affichage_menu_texte_secret()
        choix = input("Quel est votre choix ? ")
        if choix == "1":
            voir_le_secret()
        elif choix == "2":
            modifier_le_secret()
        elif choix == "3":
            break
        elif choix != "1" or choix != "2" or choix != "3":
            print("Entrée invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    path_file = "secret.txt"
    main()
