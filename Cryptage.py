from fichiers import ouverture_fichier
from Structure import Sommet, ArbreB


class Huffman():
    def __init__(self, file):
        self.file = file

    def occurence(self):
        text = ouverture_fichier(self.file).read()
        dict_char = {}
        for char in text:
            if char == " ":
                char = "SPC"
            if char == "\n":
                char = "LINE"
            if char in dict_char:
                dict_char[char] += 1
            else:
                dict_char[char] = 1
        return dict_char

    def liste_sommet(dict_char):
        return [ArbreB(racine=Sommet(value, etiquette=key)) for key, value in dict_char.items()]

    def sommets_minimum(liste_sommet):
        # Remplacer par heapq ? optimisation possible

        # Recupere dont les racines portent les plus petites etiquettes.

        arbre1 = min(liste_sommet, key=lambda x: x.racine.valeur)
        liste_sommet.remove(arbre1)
        arbre2 = min(liste_sommet, key=lambda x: x.racine.valeur)
        liste_sommet.remove(arbre2)

        return arbre1, arbre2, liste_sommet

    def creation_table_encodage(self, arbre):
        liste_sommet = arbre.parcours_prefixe(arbre.racine)
        liste_feuille = [
            sommet for sommet in liste_sommet if isinstance(sommet, tuple)]
        table_encodage = {k: v for k, v in liste_feuille}
        return table_encodage

    def encodage_text(self, table_encodage):
        text = ouverture_fichier(self.file).read()
        res = ""
        for char in text:
            if char == " ":
                char = "SPC"
            if char == "\n":
                char = "LINE"
            res += table_encodage[char]
        return res
