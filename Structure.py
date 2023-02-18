class Sommet:
    def __init__(self, val, fg=None, fd=None):
        self.val = val
        self.fg = fg
        self.fd = fd


class ArbreB:
    def __init__(self, racine=None):
        self.racine = racine

    def inserer_recursif(self, val, sommet):
        if val < sommet.val:
            if sommet.fg is None:
                sommet.fg = Sommet(val)
            else:
                inserer_recursif(val, sommet.fg)
        else:
            if sommet.fd is None:
                sommet.fd = Sommet(val)
            else:
                self.inserer_recursif(val, sommet.fd)

    def inserer(self, val):
        """
        """
        if self.racine is None:
            self.racine = Sommet(val)
        else:
            self.inserer_recursif(val, self.racine)
