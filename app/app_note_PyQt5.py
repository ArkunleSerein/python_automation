import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt


class SaisieNotesApp(QWidget):
    def __init__(self):
        super().__init__()

        # Titre de la fenêtre
        self.setWindowTitle('Saisie et gestion des notes')
        # Position et taille de la fenêtre
        self.setGeometry(100, 100, 400, 300)

        self.notes = []  # Liste pour stocker les notes
        self.init_ui()

    def init_ui(self):
        # Création des éléments graphiques
        self.layout = QVBoxLayout()

        # Zone de saisie de la note
        self.note_input = QLineEdit(self)
        self.note_input.setPlaceholderText(
            "Entrez une note (entrez une valeur négative pour arrêter)")
        self.layout.addWidget(self.note_input)

        # Bouton pour ajouter la note
        self.btn_saisie = QPushButton('Ajouter la note', self)
        self.btn_saisie.clicked.connect(
            self.ajouter_note)  # Connexion du bouton
        self.layout.addWidget(self.btn_saisie)

        # Zone pour afficher les résultats
        self.result_label = QLabel("Résultats affichés ici", self)
        self.layout.addWidget(self.result_label)

        # Boutons pour afficher les résultats
        self.btn_afficher_notes = QPushButton('Afficher les notes', self)
        self.btn_afficher_notes.clicked.connect(self.afficher_notes)
        self.layout.addWidget(self.btn_afficher_notes)

        self.btn_max = QPushButton('Afficher la note max', self)
        self.btn_max.clicked.connect(self.afficher_max)
        self.layout.addWidget(self.btn_max)

        self.btn_min = QPushButton('Afficher la note min', self)
        self.btn_min.clicked.connect(self.afficher_min)
        self.layout.addWidget(self.btn_min)

        self.btn_moyenne = QPushButton('Afficher la moyenne', self)
        self.btn_moyenne.clicked.connect(self.afficher_moyenne)
        self.layout.addWidget(self.btn_moyenne)

        self.btn_quitter = QPushButton('Quitter', self)
        self.btn_quitter.clicked.connect(self.close)
        self.layout.addWidget(self.btn_quitter)

        # Appliquer le layout à la fenêtre principale
        self.setLayout(self.layout)

        # Connecter l'événement de la touche Entrée
        self.note_input.returnPressed.connect(self.ajouter_note)

    def ajouter_note(self):
        try:
            # Convertir le texte de la saisie en entier
            note = int(self.note_input.text())
            if note < 0:
                self.result_label.setText(
                    "Saisie terminée. Vous pouvez afficher les résultats.")
                self.note_input.setEnabled(False)
                # Désactiver le bouton de saisie
                self.btn_saisie.setEnabled(False)
            else:
                self.notes.append(note)  # Ajouter la note à la liste
                # Afficher la note ajoutée
                self.result_label.setText(f"Note {note} ajoutée.")
                self.afficher_notes()  # Mettre à jour l'affichage des notes
            self.note_input.clear()  # Réinitialiser la zone de saisie
        except ValueError:
            self.result_label.setText("Veuillez entrer un nombre valide.")

    def afficher_notes(self):
        if self.notes:
            self.result_label.setText(f"Notes saisies: {self.notes}")
        else:
            self.result_label.setText("Aucune note saisie.")

    def afficher_max(self):
        if self.notes:
            self.result_label.setText(
                f"La note maximale est : {max(self.notes)}")
        else:
            self.result_label.setText("Aucune note saisie.")

    def afficher_min(self):
        if self.notes:
            self.result_label.setText(
                f"La note minimale est : {min(self.notes)}")
        else:
            self.result_label.setText("Aucune note saisie.")

    def afficher_moyenne(self):
        if self.notes:
            moyenne = sum(self.notes) / len(self.notes)
            self.result_label.setText(
                f"La moyenne des notes est : {moyenne:.2f}")
        else:
            self.result_label.setText("Aucune note saisie.")


# Fonction principale pour démarrer l'application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SaisieNotesApp()
    window.show()  # Afficher la fenêtre
    sys.exit(app.exec_())  # Exécuter l'application
