import random
import tkinter as tk

# Fonction pour gérer la logique du jeu


def check_guess(event=None):
    global nb_essai, nb_mystere, nb_joueur, score, game_over

    # Si le jeu est déjà terminé (joueur a gagné ou perdu), on ignore l'entrée
    if game_over:
        return

    try:
        nb_joueur = int(entry.get())  # Obtenir la tentative du joueur
    except ValueError:
        result_label.config(text="Veuillez entrer un nombre valide.", fg="red")
        return

    nb_essai -= 1  # Décrémenter le nombre d'essais

    # Mettre à jour l'affichage du nombre d'essais
    attempts_label.config(text=f"Nombre d'essais : {nb_essai}")

    # Mettre à jour le label pour afficher le nombre choisi par le joueur
    chosen_label.config(text=f"Vous avez choisi : {nb_joueur}")

    # Vérifier si le joueur a trouvé le nombre mystère
    if nb_joueur == nb_mystere:
        score += 1  # Ajouter un point au score
        # Mettre à jour l'affichage du score
        score_label.config(text=f"Score : {score}")
        result_label.config(text=f"Félicitations ! Vous avez trouvé le nombre mystère ({
                            nb_mystere})", fg="green")
        disable_buttons()  # Désactiver les boutons une fois le jeu terminé
        game_over = True  # Marquer la fin du jeu
        return

    # Si le joueur n'a pas trouvé le nombre, afficher si c'est trop grand ou trop petit
    if nb_joueur < nb_mystere:
        result_label.config(
            text="Votre nombre est trop petit. Essayez encore !", fg="orange")
    else:
        result_label.config(
            text="Votre nombre est trop grand. Essayez encore !", fg="orange")

    # Si les essais sont épuisés
    if nb_essai == 0:
        result_label.config(text=f"Vous avez perdu ! Le nombre mystère était {
                            nb_mystere}.", fg="red")
        disable_buttons()  # Désactiver les boutons une fois le jeu terminé
        game_over = True  # Marquer la fin du jeu

    # Réinitialiser l'input après chaque validation
    entry.delete(0, tk.END)

# Fonction pour réinitialiser le jeu
def reset_game():
    global nb_essai, nb_mystere, nb_joueur, ancien_ecart, game_over
    nb_essai = 10
    nb_mystere = random.randint(1, 100)
    nb_joueur = None
    ancien_ecart = None  # Réinitialiser l'écart précédent
    game_over = False  # Réinitialiser l'état de fin de jeu
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
score = 0  # Initialisation du score
game_over = False  # Variable pour savoir si le jeu est terminé

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

# Nouveau label pour afficher le score
score_label = tk.Label(root, text=f"Score : {score}", font=("Helvetica", 12))
score_label.pack(pady=20)

# Lier la touche "Entrée" pour appeler la fonction check_guess
root.bind("<Return>", check_guess)

# Lancement de la boucle principale de l'interface
root.mainloop()
