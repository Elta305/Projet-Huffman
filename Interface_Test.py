import tkinter as tk
from cryptage import Huffman
from structure import ArbreB


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

        # Creation fenetre
        self.root = tk.Tk()
        self.root.title("Arbre binaire")
        self.root.geometry("1920x1080")
        self.canvas_width = 1920
        self.canvas_height = 1080
        self.canevas = tk.Canvas(
            self.root, width=self.canvas_width, height=self.canvas_height,
            scrollregion=f"0 0 {self.canvas_width} {self.canvas_height}")

        # scrollbar horizontal
        self.hbar = tk.Scrollbar(self.root, orient=tk.HORIZONTAL)
        self.hbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.hbar.config(command=self.canevas.xview)
        self.canevas.config(xscrollcommand=self.hbar.set)

        self.canevas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.arbre_huffman()

    def arbre_huffman(self):
        """
        Construit l'arbre de Huffman pour le texte donné en utilisant
        l'algorithme de Huffman.
        Cette fonction affiche l'arbre, la hauteur de l'arbre, la taille de
        l'arbre, la table d'encodage (clé)
        """

        # donner a l'utilisateur de choisir le text, avec interface graphique
        # (à faire)
        text = Huffman("text.txt")
        liste_sommet = text.liste_sommet(text.occurence())

        while len(liste_sommet) > 1:

            # A1 et A2
            arbre1, arbre2, liste_sommet = text.sommets_minimum(
                liste_sommet)

            # Nouvel arbre A fusionné
            self.arbre = ArbreB.fusion(self, arbre1, arbre2)

            # Ajout du nouvel arbre dans la liste
            liste_sommet.append(self.arbre)

        self.afficher_arbre()  # Affichage de l'arbre

        table_encodage = text.creation_table_encodage(
            self.arbre)  # Creation de la table d'encodage (clé)
        print("hauteur:", self.arbre.trouver_hauteur(self.arbre.racine))
        print("taille:", self.arbre.trouver_taille(self.arbre))
        print("table_encodage:", table_encodage)
        print("texte encodé:", text.encodage_text(table_encodage))

    def afficher_arbre(self):
        """
        Affiche le contenu de l'arbre binaire sur le canevas.

        La méthode commence par effacer le contenu actuel du canevas,
        puis elle appelle la méthode
        _afficher_arbre pour afficher chaque noeud de l'arbre.
        """
        hauteur = self.arbre.trouver_hauteur(self.arbre.racine)
        self.canevas.delete("all")

        coords = (self.canvas_width/2, 50, self.canvas_width/2,
                  (self.canvas_height - 100)/hauteur)

        self._afficher_arbre(
            self.arbre.racine, coords, code="")

    def _afficher_arbre(self, sommet, coords, code):
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

        if sommet is not None:
            self.canevas.create_oval(
                x_pos-rayon, y_pos-rayon, x_pos+rayon, y_pos+rayon,
                fill="white")
            if sommet.feuille() is False:
                self.canevas.create_text(x_pos, y_pos, text=sommet.valeur)
            else:
                self.canevas.create_text(
                    x_pos, y_pos, text=f"'{sommet.etiquette}' : {code}")
                sommet.code_binaire = code
                code = ""

            if sommet.gauche is not None:
                x_left = x_pos - x_sep / 2
                y_left = y_pos + y_sep
                self.canevas.create_line(
                    x_pos, y_pos, x_left, y_left)
                self.canevas.create_text(
                    ((x_pos + x_left)/2) - 10, (y_pos + y_left)/2, text="0")

                code_gauche = code + "0"

                coords = (x_left, y_left, x_sep / 2, y_sep)
                self._afficher_arbre(sommet.gauche.racine, coords, code_gauche)

            if sommet.droite is not None:
                x_right = x_pos + x_sep / 2
                y_right = y_pos + y_sep
                self.canevas.create_line(
                    x_pos, y_pos, x_right, y_right)
                self.canevas.create_text(
                    ((x_pos + x_right)/2) + 10, (y_pos + y_right)/2, text="1")

                code_droit = code + "1"

                coords = (x_right, y_right, x_sep / 2, y_sep)

                self._afficher_arbre(sommet.droite.racine,
                                     coords, code_droit)

    def run(self):
        """
        Lance la boucle principale de l'interface graphique
        """
        self.root.mainloop()


interface = Interface()
interface.run()
