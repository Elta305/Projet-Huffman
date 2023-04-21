import tkinter as tk
import random
from structure import ArbreB, Sommet


class Interface():
    """
    Classe qui permet de créer une interface graphique pour visualiser l'arbre
    binaire de Huffman généré à partir d'un texte donné.
    """

    def __init__(self):
        """
        Crée une nouvelle instance de la classe Interface.

        La méthode initialise les attributs de la classe,

        crée une nouvelle fenêtre avec une zone de dessin en utilisant
        le module Tkinter,

        définit les dimensions de la fenêtre et de la zone de dessin,

        ajoute une barre de défilement horizontal à la fenêtre,

        et enfin appelle la méthode `arbre_huffman` pour créer l'arbre binaire.
        """
        # Creation instance arbre
        self.arbre = ArbreB()

        self.compteur_etape = 0

        # Creation fenetre
        self.root = tk.Tk()
        self.root.title("Arbre binaire")
        self.root.geometry("1920x1080")
        self.canvas_width = 1920
        self.canvas_height = 1080
        self.canevas = tk.Canvas(
            self.root, width=self.canvas_width, height=self.canvas_height,
            scrollregion=f"0 0 {self.canvas_width} {self.canvas_height}")

        # Bouton

        self.next = tk.Button(
            self.root, text="Prochaine etape", command=self.prochaine_etape)
        self.boutton = tk.Button(
            self.root, text="Lancer le test", command=self.arbre_binaire)

        self.next.pack(side=tk.BOTTOM, fill=tk.X)
        self.boutton.pack(side=tk.BOTTOM, fill=tk.X)

        # # scrollbar horizontal
        # self.hbar = tk.Scrollbar(self.root, orient=tk.HORIZONTAL)
        # self.hbar.pack(side=tk.BOTTOM, fill=tk.X)
        # self.hbar.config(command=self.canevas.xview)
        # self.canevas.config(xscrollcommand=self.hbar.set)

        self.canevas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def arbre_binaire(self):
        """
        Construit l'arbre de Huffman pour le texte donné en utilisant
        l'algorithme de Huffman.
        Cette fonction affiche l'arbre, la hauteur de l'arbre, la taille de
        l'arbre, la table d'encodage (clé)
        """
        self.arbre.inserer(10)
        self.arbre.inserer(5)
        self.arbre.inserer(15)
        self.arbre.inserer(3)
        self.arbre.inserer(7)
        self.arbre.inserer(25)
        self.arbre.inserer(6)
        self.arbre.inserer(16)
        self.arbre.inserer(30)
        self.arbre.inserer(27)
        self.arbre.inserer(33)

        self.afficher_arbre()

        self.compteur_etape += 1

    def prochaine_etape(self):
        """
        """

        if self.compteur_etape == 1:

            self.arbre.supprimer_noeud(3)

            self.afficher_arbre()

            self.compteur_etape += 1

        elif self.compteur_etape == 2:
            self.arbre.inserer(3)

            self.afficher_arbre()

            self.compteur_etape += 1

        elif self.compteur_etape == 3:

            self.arbre.supprimer_noeud(7)

            self.afficher_arbre()

            self.compteur_etape += 1

        elif self.compteur_etape == 4:

            self.arbre.inserer(7)

            self.compteur_etape += 1

            self.afficher_arbre()

        elif self.compteur_etape == 5:
            self.arbre.supprimer_noeud(25)

            self.compteur_etape += 1

            self.afficher_arbre()
        elif self.compteur_etape == 6:
            arbre2 = ArbreB()

            arbre2.inserer(26)
            arbre2.inserer(31)
            arbre2.inserer(28)
            arbre2.inserer(34)
            arbre2.inserer(13)
            arbre2.inserer(12)

            self.arbre.fusion_abr(arbre2)

            self.compteur_etape += 1

            self.afficher_arbre()

        elif self.compteur_etape == 7:
            self.arbre.decomposition()

            self.afficher_arbre()

    def afficher_arbre(self):
        """
        Affiche le contenu de l'arbre binaire sur le canevas.

        La méthode commence par effacer le contenu actuel du canevas,
        puis elle appelle la méthode
        _afficher_arbre pour afficher chaque noeud de l'arbre.
        """
        self.canevas.delete("all")

        coords = (self.canvas_width/2, 50, self.canvas_width/2,
                  (self.canvas_height - 100)/6)

        self._afficher_arbre(
            self.arbre.racine, coords)

    def _afficher_arbre(self, sommet, coords):
        """
        Affiche un sous-arbre binaire sur le canevas à partir
        d'un sommet donné.

        La méthode commence par dessiner un cercle blanc pour représenter
        le noeud, et affiche son étiquette si elle est définie.
        Ensuite, elle dessine une ligne entre le noeud courant
        et ses fils gauche et droit (si existants),
        et appelle récursivement cette méthode sur les fils
        pour les afficher à leur tour.

        Args:
            sommet (Noeud): Le noeud courant de l'arbre à afficher.

            x_pos (int): La position x du cercle représentant
            le noeud sur le canevas.

            y_pos (int): La position y du cercle représentant
            le noeud sur le canevas.

            x_sep (float): La séparation entre les noeuds lors
            de l'affichage.

            y_sep (float): La séparation entre les noeuds lors
            de l'affichage.

            code (str) : code binaire du sommet actuel selon
            l'encodage de Huffman
        """
        rayon = 25
        x_pos, y_pos, x_sep, y_sep = coords

        self.root.update()

        if sommet is not None:
            self.canevas.create_oval(
                x_pos-rayon, y_pos-rayon, x_pos+rayon, y_pos+rayon,
                fill="white")

            self.canevas.create_text(x_pos, y_pos, text=sommet.valeur)

            if sommet.gauche is not None:
                x_left = x_pos - x_sep / 2
                y_left = y_pos + y_sep
                self.canevas.create_line(
                    x_pos, y_pos, x_left, y_left)

                coords = (x_left, y_left, x_sep / 2, y_sep)
                self._afficher_arbre(
                    sommet.gauche.racine, coords)

            if sommet.droite is not None:
                x_right = x_pos + x_sep / 2
                y_right = y_pos + y_sep
                self.canevas.create_line(
                    x_pos, y_pos, x_right, y_right)

                coords = (x_right, y_right, x_sep / 2, y_sep)
                self._afficher_arbre(
                    sommet.droite.racine, coords)

    def run(self):
        """
        Lance la boucle principale de l'interface graphique
        """
        self.root.mainloop()


interface = Interface()
interface.run()
