
from tkinter import *
from random import randint


class SnakeGame:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.largeur = fenetre.winfo_screenwidth()
        self.hauteur = fenetre.winfo_screenheight()
        self.largeur_plateau = self.largeur / 2
        self.hauteur_plateau = self.hauteur / 1.2
        self.nombre_de_cases = 75
        self.largeur_case = self.largeur_plateau / self.nombre_de_cases
        self.hauteur_case = self.hauteur_plateau / self.nombre_de_cases

        # Canvas pour le plateau de jeu
        self.plateau = Canvas(
            fenetre, width=self.largeur_plateau, height=self.hauteur_plateau, bg="black")
        self.plateau.pack(side="bottom")

        # Canvas pour le score
        self.barre = Text(fenetre, width=int(self.largeur / 2),
                          height=int(self.hauteur_plateau / 10), bg="#fff")
        self.barre.pack(side="top")
        self.barre.insert(END, "score: 0\n")

        self.reinitialiser_jeu()

        # Gestion des touches
        fenetre.bind("<Left>", self.left_key)
        fenetre.bind("<Right>", self.right_key)
        fenetre.bind("<Up>", self.up_key)
        fenetre.bind("<Down>", self.down_key)

        # Boucle principale du jeu
        self.fenetre.after(0, self.tache)

    def reinitialiser_jeu(self):
        self.snake = [self.case_aleatoire()]
        self.fruit = self.fruit_aleatoire()
        self.mouvement = (0, 0)
        self.score = 0
        self.perdu = 0

    def case_aleatoire(self):
        return randint(0, self.nombre_de_cases - 1), randint(0, self.nombre_de_cases - 1)

    def remplir_case(self, x, y, couleur="yellow"):
        x1 = x * self.largeur_case
        y1 = y * self.hauteur_case
        x2 = x1 + self.largeur_case
        y2 = y1 + self.hauteur_case
        self.plateau.create_oval(x1, y1, x2, y2, fill=couleur)

    def dessine_serpent(self):
        for case in self.snake:
            self.remplir_case(case[0], case[1])

    def dessine_fruit(self):
        x, y = self.fruit
        x1 = x * self.largeur_case
        y1 = y * self.hauteur_case
        x2 = x1 + self.largeur_case
        y2 = y1 + self.hauteur_case
        self.plateau.create_oval(x1, y1, x2, y2, fill="light green")

    def etre_dans_snake(self, case):
        return 1 if case in self.snake else 0

    def fruit_aleatoire(self):
        fruit = self.case_aleatoire()
        while self.etre_dans_snake(fruit):
            fruit = self.case_aleatoire()
        return fruit

    def serpent_mort(self, nouvelle_tete):
        nouvelle_tete_x, nouvelle_tete_y = nouvelle_tete
        if (self.etre_dans_snake(nouvelle_tete) and self.mouvement != (0, 0)) or nouvelle_tete_x < 0 or nouvelle_tete_y < 0 or nouvelle_tete_x >= self.nombre_de_cases or nouvelle_tete_y >= self.nombre_de_cases:
            self.perdu = 1

    def mise_a_jour_score(self):
        self.score += 1
        self.barre.delete(0.0, 3.0)
        self.barre.insert(END, f"score: {self.score}\n")

    def mise_a_jour_snake(self):
        ancienne_tete_x, ancienne_tete_y = self.snake[0]
        mouvement_x, mouvement_y = self.mouvement
        nouvelle_tete = (ancienne_tete_x + mouvement_x,
                         ancienne_tete_y + mouvement_y)
        self.serpent_mort(nouvelle_tete)
        self.snake.insert(0, nouvelle_tete)

        if nouvelle_tete == self.fruit:
            self.fruit = self.fruit_aleatoire()
            self.mise_a_jour_score()
        else:
            self.snake.pop()

    def left_key(self, event):
        self.mouvement = (-1, 0)

    def right_key(self, event):
        self.mouvement = (1, 0)

    def up_key(self, event):
        self.mouvement = (0, -1)

    def down_key(self, event):
        self.mouvement = (0, 1)

    def tache(self):
        if self.perdu:
            self.barre.delete(0.0, 3.0)
            self.barre.insert(END, f"Perdu avec un score de {self.score}")
            self.reinitialiser_jeu()
        else:
            self.mise_a_jour_snake()
            self.plateau.delete("all")
            self.dessine_fruit()
            self.dessine_serpent()
            self.fenetre.after(70, self.tache)


# Création de la fenêtre principale
fenetre = Tk()
fenetre.title('Snake')
hauteur = fenetre.winfo_screenheight()
largeur = fenetre.winfo_screenwidth()
fenetre.geometry(f"{int(largeur / 2)}x{int(hauteur / 1.1)}+0+0")

# Lancement du jeu
game = SnakeGame(fenetre)

fenetre.mainloop()
