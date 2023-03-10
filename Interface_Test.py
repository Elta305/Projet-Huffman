import tkinter as tk
from Structure import Sommet, ArbreB
from Cryptage import Huffman


class Interface():

    def __init__(self):
        # Creation instance arbre
        self.arbre = ArbreB()

        # Creation fenetre
        self.root = tk.Tk()
        self.root.title("Arbre binaire")
        self.root.geometry("1920x1080")
        self.fenetre_width = 1920
        self.fenetre_height = 1080

        self.canvas_width = 1920
        self.canvas_height = 1080
        self.canevas = tk.Canvas(
            self.root, width=self.canvas_width, height=self.canvas_height, scrollregion=f"0 0 {self.canvas_width} {self.canvas_height}")

        # scrollbar horizontal
        self.hbar = tk.Scrollbar(self.root, orient=tk.HORIZONTAL)
        self.hbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.hbar.config(command=self.canevas.xview)
        self.canevas.config(xscrollcommand=self.hbar.set)

        self.canevas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.arbre_huffman()

    def arbre_huffman(self):

        # changer text
        text = Huffman("text.txt")
        liste_sommet = Huffman.liste_sommet(text.occurence())

        while len(liste_sommet) > 1:

            # A1 et A2
            arbre1, arbre2, liste_sommet = Huffman.sommets_minimum(
                liste_sommet)

            # Nouvel arbre A fusionné
            self.arbre = ArbreB.fusion(self, arbre1, arbre2)

            # Ajout du nouvel arbre dans la liste
            liste_sommet.append(self.arbre)

        self.afficher_arbre()  # Affichage de l'arbre

        table_encodage = text.creation_table_encodage(
            self.arbre)  # Creation de la table d'encodage (clé)
        print("hauteur: ", self.arbre.trouver_hauteur(self.arbre.racine))
        print("taille: ", self.arbre.trouver_taille(self.arbre))
        print("texte encodé: ", text.encodage_text(table_encodage))

    def afficher_arbre(self):
        """
        Affiche le contenu de l'arbre binaire sur le canevas.

        La méthode commence par effacer le contenu actuel du canevas, puis elle appelle la méthode
        _afficher_arbre pour afficher chaque noeud de l'arbre.
        """
        hauteur = self.arbre.trouver_hauteur(self.arbre.racine)
        self.canevas.delete("all")
        self._afficher_arbre(
            self.arbre.racine, self.canvas_width/2, 50, self.canvas_width/2, (self.canvas_height - 100)/hauteur, code="")

    def _afficher_arbre(self, sommet, x, y, dx, dy, code):
        """
        Affiche un sous-arbre binaire sur le canevas à partir d'un sommet donné.

        La méthode commence par dessiner un cercle blanc pour représenter le noeud, et écrit son étiquette si elle est définie.
        Ensuite, elle dessine une ligne entre le noeud courant et ses fils gauche et droit (si existants),
        et appelle récursivement cette méthode sur les fils pour les afficher à leur tour.

        Args:
            sommet (Noeud): Le noeud courant de l'arbre à afficher.
            x (int): La position x du cercle représentant le noeud sur le canevas.
            y (int): La position y du cercle représentant le noeud sur le canevas.
            dx (float): La séparation entre les noeuds lors de l'affichage.
            dy (float): La séparation entre les noeuds lors de l'affichage.
            code (str) : ""
        """
        rayon = 25

        if sommet is not None:
            self.canevas.create_oval(
                x-rayon, y-rayon, x+rayon, y+rayon, fill="white")
            if sommet.feuille() is False:
                self.canevas.create_text(x, y, text=sommet.valeur)
            else:
                self.canevas.create_text(
                    x, y, text=f"'{sommet.etiquette}' : {code}")
                sommet.code_binaire = code
                code = ""

            if sommet.gauche is not None:
                x_left = x - dx / 2
                y_left = y + dy
                self.canevas.create_line(
                    x, y, x_left, y_left)
                self.canevas.create_text(
                    ((x + x_left)/2) - 10, (y + y_left)/2, text="0")

                code_gauche = code + "0"

                self._afficher_arbre(sommet.gauche.racine,
                                     x_left, y_left, dx / 2, dy, code_gauche)

            if sommet.droite is not None:
                x_right = x + dx / 2
                y_right = y + dy
                self.canevas.create_line(
                    x, y, x_right, y_right)
                self.canevas.create_text(
                    ((x + x_right)/2) + 10, (y + y_right)/2, text="1")

                code_droit = code + "1"

                self._afficher_arbre(sommet.droite.racine,
                                     x_right, y_right, dx / 2, dy, code_droit)

    def run(self):
        self.root.mainloop()


interface = Interface()
interface.run()
