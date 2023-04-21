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

    def supprimer_noeud(self, valeur):
        """Supprime le noeud ayant la valeur spécifiée de l'arbre."""
        if self.racine is None:
            return

        # Cherche le noeud à supprimer et son parent
        parent = None
        courant = self.racine
        while courant is not None and courant.valeur != valeur:
            parent = courant
            if valeur < courant.valeur:
                courant = courant.gauche.racine
            else:
                courant = courant.droite.racine

        # Si le noeud n'a pas été trouvé, on sort de la fonction
        if courant is None:
            return

        # Cas 1: le noeud est une feuille
        if courant.feuille():
            if courant == self.racine:
                self.racine = None
            elif parent.gauche.racine == courant:
                parent.gauche = None
            else:
                parent.droite.racine = None

        # Cas 2: le noeud a un seul enfant
        elif courant.gauche is None:
            if courant == self.racine:
                self.racine = courant.droite
            elif parent.gauche == courant:
                parent.gauche = courant.droite
            else:
                parent.droite = courant.droite
        elif courant.droite is None:
            if courant == self.racine:
                self.racine = courant.gauche
            elif parent.gauche == courant:
                parent.gauche = courant.gauche
            else:
                parent.droite = courant.gauche

        # Cas 3: le noeud a deux enfants
        else:
            # Trouve le plus petit noeud dans le sous-arbre droit
            successeur = courant.droite
            successeur_parent = courant
            while successeur.racine.gauche is not None:
                successeur_parent = successeur
                successeur = successeur.racine.gauche

            # Échange les valeurs entre le noeud à supprimer et son successeur
            courant.valeur, successeur.racine.valeur = successeur.racine.valeur, courant.valeur

            # Supprime le successeur (qui est maintenant une feuille ou a un enfant droit)
            if successeur_parent.racine.gauche.racine == successeur.racine:
                successeur_parent.racine.gauche = successeur.racine.droite
            else:
                successeur_parent.droite = successeur.droite

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

    def fusion_abr(self, arbre2):
        """
        Fusionne l'arbre courant avec l'arbre passé en argument. Les noeuds de l'arbre 2 sont insérés dans l'arbre courant.
        """
        noeuds_a_inserer = arbre2.parcours_prefixe(arbre2.racine)
        for noeud in noeuds_a_inserer:
            self.inserer(noeud)

    def decomposition(self):
        """
        Découpe l'arbre courant en deux arbres, en enlevant le sous-arbre gauche ou le sous-arbre droit de la racine.
        """
        nouvelle_arbre = ArbreB()
        if self.racine is None:
            return

        if self.racine.feuille():
            return

        if self.racine.droite is not None:
            nouvelle_arbre.racine = self.racine.droite.racine
            self.racine.droite = None

        elif self.racine.gauche is not None:
            nouvelle_arbre.racine = self.racine.gauche.racine
            self.racine.gauche = None
