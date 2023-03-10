class Sommet:

    def __init__(self, valeur, etiquette=None):
        self.valeur = valeur
        self.etiquette = etiquette
        self.gauche = None
        self.droite = None
        self.code_binaire = ""

    def feuille(self):
        return self.gauche is None and self.droite is None


class ArbreB:

    def __init__(self, racine=None):
        self.racine = racine

    def __lt__(self, other):
        return self.racine.valeur < other.racine.valeur

    def __add__(self, other):
        return self.racine.valeur + other.racine.valeur

    def inserer(self, valeur):
        """
        Insère un nouveau noeud contenant la valeur spécifiée dans l'arbre.
        Si l'arbre est vide, la valeur deviens la racine de l'arbre.

        Args:
            valeur (int): la valeur à insérer dans l'arbre.
        """
        if self.racine is None:
            self.racine = Sommet(valeur)
        else:
            self.inserer_recursif(valeur, self.racine)

    def inserer_recursif(self, valeur, sommet):
        """
        Fonction auxiliaire (def inserer) pour insérer une valeur dans l'arbre de manière récursive.

        Args:
            valeur (int): la valeur à insérer dans l'arbre.
            sommet (Sommet): le noeud de l'arbre à partir duquel commencer l'insertion récursive.
        """
        if valeur < sommet.valeur:
            if sommet.gauche is None:
                sommet.gauche = Sommet(valeur)
            else:
                self.inserer_recursif(valeur, sommet.gauche)
        else:
            if sommet.droite is None:
                sommet.droite = Sommet(valeur)
            else:
                self.inserer_recursif(valeur, sommet.droite)

    def supprimer(self, valeur):
        """
        Supprime le noeud contenant la valeur spécifiée de l'arbre.

        Args:
            valeur (int): la valeur à supprimer de l'arbre.
        """
        self.racine = self.supprimer_recursif(valeur, self.racine)

    def supprimer_recursif(self, valeur, sommet):
        """
        Fonction auxiliaire (def supprimer) pour supprimer un noeud contenant la valeur spécifiée de l'arbre de manière récursive.

        Args:
            valeur (int): la valeur à supprimer de l'arbre.
            sommet (Sommet): le noeud à partir duquel commencer la recherche pour la suppression.

        Returns:
            Le nouveau noeud, après la suppression de la valeur spécifiée.
        """

        if sommet is None:
            return sommet

        if valeur < sommet.valeur:
            sommet.gauche = self.supprimer_recursif(valeur, sommet.gauche)

        elif valeur > sommet.valeur:
            sommet.droite = self.supprimer_recursif(valeur, sommet.droite)

        else:

            # Si le sous-arbre gauche n'existe pas alors, on supprime le sommet actuel en le remplaçant par son sous-arbre droit.
            if sommet.gauche is None:
                temp = sommet.droite
                sommet = None
                return temp

            # Si le sous-arbre droit n'existe pas alors, on supprime le sommet actuel en le remplaçant par son sous-arbre gauche.
            elif sommet.droite is None:
                temp = sommet.gauche
                sommet = None
                return temp

            # Si le sommet à supprimer a deux fils, on le remplace par le plus petit noeud du sous-arbre droit.
            temp = self.trouver_min(sommet.droite)
            sommet.valeur = temp.valeur
            sommet.droite = self.supprimer_recursif(temp.valeur, sommet.droite)

        return sommet

    def trouver_min(self, sommet):
        """
        Trouve le plus petit noeud dans le sous-arbre droit.

        Args:
            sommet: Le noeud à partir duquel commencer la recherche.

        Returns:
            Le plus petit noeud.
        """
        noeud = sommet
        while noeud.gauche is not None:
            noeud = noeud.gauche
        return noeud

    def fusion(self, arbre1, arbre2):
        """
        Crée un nouvel arbre binaire en fusionnant les deux arbres binaires donnés.

        Args:
            arbre1 (ArbreB): Le premier arbre binaire à fusionner.
            arbre2 (ArbreB): Le deuxième arbre binaire à fusionner.

        Returns:
            ArbreB: Le nouvel arbre binaire résultant de la fusion.
        """
        nouvel_arbre = ArbreB()

        nouvel_arbre.racine = Sommet(
            arbre1.racine.valeur + arbre2.racine.valeur)
        nouvel_arbre.racine.gauche = arbre1
        nouvel_arbre.racine.droite = arbre2

        return nouvel_arbre

    def trouver_hauteur(self, sommet):
        if sommet.feuille() is True:
            return 0
        else:
            return 1 + max(self.trouver_hauteur(sommet.gauche.racine), self.trouver_hauteur(sommet.droite.racine))

    def parcours_prefixe(self, sommet):

        valeurs = []
        if sommet.feuille() is True:
            valeurs.append((sommet.etiquette, sommet.code_binaire))
        else:
            valeurs.append((sommet.valeur))

        if sommet.gauche is not None:
            valeurs.extend(self.parcours_prefixe(sommet.gauche.racine))
        if sommet.droite is not None:
            valeurs.extend(self.parcours_prefixe(sommet.droite.racine))

        return valeurs

    def trouver_taille(self, arbre):
        if arbre is None:
            return 0
        else:
            return 1 + self.trouver_taille(arbre.racine.gauche) + self.trouver_taille(arbre.racine.droite)
