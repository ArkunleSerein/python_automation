import random
import tkinter as tk

# Fonction pour gérer la logique du jeu


def check_guess(event=None):  # On ajoute un paramètre event pour permettre l'appel par bind
    global nb_essai, nb_mystere, nb_joueur, ancien_ecart

    try:
        nb_joueur = int(entry.get())  # Obtenir la tentative du joueur
    except ValueError:
        result_label.config(text="Veuillez entrer un nombre valide.", fg="red")
        return

    nb_essai -= 1  # Incrémenter le nombre d'essais

    # Mettre à jour l'affichage du nombre d'essais
    attempts_label.config(text=f"Nombre d'essais : {nb_essai}")

    # Mettre à jour le label pour afficher le nombre choisi par le joueur
    chosen_label.config(text=f"Vous avez choisi : {nb_joueur}")

    if nb_joueur == nb_mystere:
        result_label.config(text=f"Félicitations ! Vous avez trouvé le nombre mystère ({
                            nb_mystere})", fg="green")
        disable_buttons()  # Désactiver les boutons une fois le jeu terminé
    elif nb_joueur < nb_mystere:
        result_label.config(
            text="Votre nombre est trop petit. Essayez encore !", fg="orange")
    else:
        result_label.config(
            text="Votre nombre est trop grand. Essayez encore !", fg="orange")

    # Calcul de la différence entre le nombre mystère et l'essai du joueur
    ecart = abs(nb_joueur - nb_mystere)

    # Comparaison avec l'écart précédent pour savoir si l'utilisateur se réchauffe ou se refroidit
    if ancien_ecart is not None:
        if ecart < ancien_ecart and nb_mystere - 5 <= nb_joueur <= nb_mystere + 5:
            result_label.config(text=result_label.cget(
                "text") + " Tu te réchauffes !", fg="green")
        elif ecart > ancien_ecart and nb_mystere - 5 <= nb_joueur <= nb_mystere + 5:
            result_label.config(text=result_label.cget(
                "text") + " Tu te refroidis !", fg="blue")

    # Mémoriser l'écart actuel pour le comparer au prochain essai
    ancien_ecart = ecart

    # Vérifier si l'utilisateur a perdu tous ses essais
    if nb_essai == 0:
        result_label.config(text=f"Vous avez perdu ! Le nombre mystère était {
                            nb_mystere}.", fg="red")
        disable_buttons()  # Désactiver les boutons une fois le jeu terminé

    # Réinitialiser l'input après chaque validation
    entry.delete(0, tk.END)

# Fonction pour réinitialiser le jeu


def reset_game():
    global nb_essai, nb_mystere, nb_joueur, ancien_ecart
    nb_essai = 10
    nb_mystere = random.randint(1, 100)
    nb_joueur = None
    ancien_ecart = None  # Réinitialiser l'écart précédent
    entry.delete(0, tk.END)  # Effacer la zone de saisie
    # Réinitialiser le nombre d'essais
    attempts_label.config(text=f"Nombre d'essais : {nb_essai}")
    # Réinitialiser le label du choix du joueur
    chosen_label.config(text="Vous n'avez pas encore choisi de nombre.")
    result_label.config(text="")  # Réinitialiser le résultat
    enable_buttons()  # Réactiver les boutons une fois le jeu réinitialisé

# Fonction pour désactiver les boutons de jeu


def disable_buttons():
    button.config(state="disabled")  # Désactiver le bouton de validation
    retry_button.config(state="normal")  # Activer le bouton de réessai

# Fonction pour activer les boutons de jeu


def enable_buttons():
    button.config(state="normal")  # Réactiver le bouton de validation
    # Désactiver le bouton de réessai au début
    retry_button.config(state="disabled")


# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu du Nombre Mystère")
root.geometry("500x500")  # Taille de la fenêtre

# Initialisation du nombre mystère et du compteur d'essais
nb_mystere = random.randint(1, 100)
nb_essai = 10
nb_joueur = None
ancien_ecart = None  # Initialiser la variable pour l'écart

# Création des widgets
label = tk.Label(
    root, text="Devinez le nombre mystère (entre 1 et 100) :", font=("Helvetica", 12))
label.pack(pady=20)

entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=10)

button = tk.Button(root, text="Valider", font=(
    "Helvetica", 14), command=check_guess)
button.pack(pady=10)

# Label pour afficher le nombre d'essais
attempts_label = tk.Label(root, text=f"Nombre d'essais : {
                          nb_essai}", font=("Helvetica", 10))
attempts_label.pack(pady=10)

# Nouveau label pour afficher le nombre choisi par le joueur
chosen_label = tk.Label(
    root, text="Vous n'avez pas encore choisi de nombre.", font=("Helvetica", 12))
chosen_label.pack(pady=10)

# Label pour afficher le résultat du jeu
result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="black")
result_label.pack(pady=10)

# Nouveau bouton "Réessayer"
retry_button = tk.Button(root, text="Réessayer", font=(
    "Helvetica", 14), command=reset_game, state="disabled")
retry_button.pack(pady=10)

# Lier la touche "Entrée" pour appeler la fonction check_guess
root.bind("<Return>", check_guess)

# Lancement de la boucle principale de l'interface
root.mainloop()
