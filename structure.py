class Sommet:

    def __init__(self, valeur, etiquette=None):
        self.valeur = valeur
        self.etiquette = etiquette
        self.gauche = None
        self.droite = None
        self.code_binaire = ""

    def feuille(self):
        """
        Vérifie si le sommet est une feuille de l'arbre.

        Returns:
            True si le sommet est une feuille, False sinon.
        """
        return self.gauche is None and self.droite is None


class ArbreB:

    def __init__(self, racine=None):
        self.racine = racine

    def __lt__(self, other):
        """
        Compare les valeurs des racines de deux arbres binaires pour pouvoir les trier selon leurs valeurs.

        Args:
            self: instance de la classe ArbreB.
            other: autre instance de la classe ArbreB à comparer.

        Returns:
            True si la valeur de la racine de l'arbre est inférieure à celle de l'autre arbre, False sinon.
        """
        return self.racine.valeur < other.racine.valeur

    def __add__(self, other):
        """
        Calcule la somme des valeurs des racines de deux arbres binaires.

        Args:
            self: instance de la classe ArbreB.
            other: autre instance de la classe ArbreB à ajouter.

        Returns:
            La somme des valeurs des racines de l'arbre et de l'autre arbre.
        """
        return self.racine.valeur + other.racine.valeur

    def inserer(self, valeur):
        """
        Insère un nouveau sommet contenant la valeur spécifiée dans l'arbre.
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
            sommet (Sommet): le sommet de l'arbre à partir duquel commencer l'insertion récursive.
        """
        if valeur < sommet.valeur:
            if sommet.gauche is None:
                sommet.gauche = ArbreB(racine=Sommet(valeur))
            else:
                self.inserer_recursif(valeur, sommet.gauche.racine)
        else:
            if sommet.droite is None:
                sommet.droite = ArbreB(racine=Sommet(valeur))
            else:
                self.inserer_recursif(valeur, sommet.droite.racine)

    # def supprimer(self, valeur):
    #     """
    #     Supprime le sommet contenant la valeur spécifiée de l'arbre.

    #     Args:
    #         valeur (int): la valeur à supprimer de l'arbre.
    #     """
    #     # nouvel_arbre = ArbreB()
    #     # nouvel_arbre = self.supprimer_recursif(valeur, self)
    #     # return self.supprimer_recursif(valeur, self)
    #     self.supprimer_recursif(valeur, self)

    # def supprimer_recursif(self, valeur, sommet):
    #     """
    #     Fonction auxiliaire (def supprimer) pour supprimer un sommet contenant la valeur spécifiée de l'arbre de manière récursive.

    #     Args:
    #         valeur (int): la valeur à supprimer de l'arbre.
    #         sommet (Sommet): le sommet à partir duquel commencer la recherche pour la suppression.

    #     Returns:
    #         Le nouveau sommet, après la suppression de la valeur spécifiée.
    #     """

    #     if sommet is None:
    #         return sommet

    #     if valeur < sommet.racine.valeur:
    #         sommet.gauche = self.supprimer_recursif(
    #             valeur, sommet.racine.gauche)

    #     elif valeur > sommet.racine.valeur:
    #         sommet.droite = self.supprimer_recursif(
    #             valeur, sommet.droite.racine)

    #     else:

    #         # Si le sous-arbre gauche n'existe pas alors, on supprime le sommet actuel en le remplaçant par son sous-arbre droit.
    #         if sommet.racine.gauche is None:
    #             self.racine = sommet.racine.droite.racine

    #         # Si le sous-arbre droit n'existe pas alors, on supprime le sommet actuel en le remplaçant par son sous-arbre gauche.
    #         elif sommet.racine.droite is None:
    #             self.racine = sommet.racine.gauche.racine

    #         # Si le sommet à supprimer a deux fils, on le remplace par le plus petit sommet du sous-arbre droit.
    #         else:
    #             temp = self.trouver_min(sommet.racine.droite)
    #             sommet.valeur = temp.racine.valeur
    #             sommet.droite = self.supprimer_recursif(
    #                 temp.racine.valeur, sommet.racine.droite)

    # def trouver_min(self, sommet):
    #     """
    #     Trouve le plus petit sommet dans le sous-arbre droit.

    #     Args:
    #         sommet: Le sommet à partir duquel commencer la recherche.

    #     Returns:
    #         Le plus petit sommet.
    #     """
    #     while sommet.racine.gauche is not None:
    #         sommet = sommet.gauche
    #     return sommet

    def supprimer(self, valeur):
        """
        Supprime un sommet contenant la valeur spécifiée de l'arbre.

        Args:
            valeur (int): la valeur à supprimer de l'arbre.
        """
        if self.racine is None:
            return

        self.racine = self.supprimer_recursif(valeur, self.racine)

    def supprimer_recursif(self, valeur, sommet):
        """
        Fonction auxiliaire (def supprimer) pour supprimer un sommet de l'arbre de manière récursive.

        Args:
            valeur (int): la valeur à supprimer de l'arbre.
            sommet (Sommet): le sommet de l'arbre à partir duquel commencer la suppression récursive.

        Returns:
            Le nouveau sommet qui remplace le sommet supprimé (ou le même sommet si aucune suppression n'a eu lieu).
        """
        if sommet is None:
            return None

        if valeur < sommet.valeur:
            sommet.gauche = self.supprimer_recursif(
                valeur, sommet.gauche.racine)
        elif valeur > sommet.valeur:
            sommet.droite = self.supprimer_recursif(
                valeur, sommet.droite.racine)
        else:
            if sommet.gauche is None:
                return sommet.droite
            elif sommet.droite is None:
                return sommet.gauche
            else:
                # Trouver le plus grand sommet dans le sous-arbre gauche
                # (ou le plus petit dans le sous-arbre droit)
                plus_grand = sommet.gauche.racine
                while plus_grand.droite is not None:
                    plus_grand = plus_grand.droite.racine

                # Supprimer le plus grand sommet et le remplacer par le sommet à supprimer
                sommet.valeur = plus_grand.valeur
                sommet.gauche.racine = self.supprimer_recursif(
                    plus_grand.valeur, sommet.gauche.racine)

        return sommet

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
        """
        Calcule la hauteur de l'arbre en partant d'un sommet donné.

        Args:
            self: instance de la classe ArbreB.
            sommet: sommet de l'arbre pour lequel on veut calculer la hauteur.

        Returns:
            La hauteur de l'arbre en partant du sommet donné.
        """
        if sommet.feuille() is True:
            return 0

        return 1 + max(self.trouver_hauteur(sommet.gauche.racine), self.trouver_hauteur(sommet.droite.racine))

    def trouver_taille(self, arbre):
        """
        Retourne la taille de l'arbre binaire.

        Args:
            arbre: l'arbre binaire dont on veut calculer la taille.

        Returns:
            La taille de l'arbre binaire.

        """
        if arbre is None:
            return 0
        return 1 + self.trouver_taille(arbre.racine.gauche) + self.trouver_taille(arbre.racine.droite)

    def parcours_prefixe(self, sommet):
        """
        Réalise un parcours prefix de l'arbre en partant d'un sommet donné.

        Args:
            self: instance de la classe ArbreB.
            sommet: sommet de l'arbre à partir duquel on veut réaliser le parcours.

        Returns:
            Une liste contenant les valeurs des sommets rencontrés lors du parcours préfixe.
        """

        valeurs = []

        valeurs.append((sommet.valeur))

        if sommet.gauche is not None:
            valeurs.extend(self.parcours_prefixe(sommet.gauche.racine))
        if sommet.droite is not None:
            valeurs.extend(self.parcours_prefixe(sommet.droite.racine))

        return valeurs

    def parcours_arbre(self, sommet):
        """
        Réalise un parcours de l'arbre en partant d'un sommet donné.

        Args:
            self: instance de la classe ArbreB.
            sommet: sommet de l'arbre à partir duquel on veut réaliser le parcours.

        Returns:
            Une liste contenant les valeurs des sommets rencontrés lors du parcours préfixe.
            Si un sommet est une feuille, sa valeur est un tuple contenant son étiquette et son code binaire.
            Sinon, sa valeur.
        """

        valeurs = []
        if sommet.feuille() is True:
            valeurs.append((sommet.etiquette, sommet.code_binaire))
        else:
            valeurs.append((sommet.valeur))

        if sommet.gauche is not None:
            valeurs.extend(self.parcours_arbre(sommet.gauche.racine))
        if sommet.droite is not None:
            valeurs.extend(self.parcours_arbre(sommet.droite.racine))

        return valeurs

