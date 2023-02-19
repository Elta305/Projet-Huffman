class Sommet:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None


class ArbreB:
    def __init__(self, racine=None):
        self.racine = racine

    def inserer(self, valeur):
        if self.racine is None:
            self.racine = Sommet(valeur)
        else:
            self.inserer_recursif(valeur, self.racine)

    def inserer_recursif(self, valeur, sommet):
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
        self.racine = self.supprimer_recursif(valeur, self.racine)

    def supprimer_recursif(self, valeur, sommet):
        if sommet is None:
            return sommet
        if valeur < sommet.valeur:
            sommet.gauche = self.supprimer_recursif(valeur, sommet.gauche)
        elif valeur > sommet.valeur:
            sommet.droite = self.supprimer_recursif(valeur, sommet.droite)
        else:
            if sommet.gauche is None:
                temp = sommet.droite
                sommet = None
                return temp
            elif sommet.droite is None:
                temp = sommet.gauche
                sommet = None
                return temp
            temp = self._trouver_min(sommet.droite)
            sommet.valeur = temp.valeur
            sommet.droite = self.supprimer_recursif(temp.valeur, sommet.droite)
        return sommet

    def _trouver_min(self, sommet):
        noeud = sommet
        while noeud.gauche is not None:
            noeud = noeud.gauche
        return noeud
