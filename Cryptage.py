from fichiers import ouverture_fichier
from structure import Sommet, ArbreB


class Huffman():
    """
    Classe pour la compression de fichiers texte à l'aide de l'algorithme
    de Huffman.

    Attributes:
        file (str): Le nom du fichier à compresser.
    """

    def __init__(self, file):
        """
        Initialise une instance de la classe Huffman.

        Args:
            file: le nom du fichier à compresser.
        """
        self.file = file

    def occurence(self):
        """
        Calcule le nombre d'occurrences de chaque caractère dans le texte
        du fichier donné.

        Returns:
            Un dictionnaire contenant le nombre d'occurrences de chaque
            caractère dans le texte du fichier.

            Les clés sont les caractères et les valeurs sont les nombres
            d'occurrences correspondants.
        """
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

    def liste_sommet(self, dict_char):
        """
        Construit une liste de sommets, où chaque sommet contient un
        caractère comme etiquette et son nombre d'occurrences en tant
        que valeur.

        Args:
            dict_char: un dictionnaire contenant le nombre d'occurrences
            de chaque caractère dans le texte.

            Les clés sont les caractères et les valeurs sont les nombres
            d'occurrences correspondants.

        Returns:
            Une liste de sommets, où chaque sommet contient un caractère
            et son nombre d'occurrences.
        """
        return [ArbreB(racine=Sommet(value, etiquette=key))
                for key, value in dict_char.items()]

    def sommets_minimum(self, liste_sommet):
        """
        Trouve les deux sommets ayant les plus petites valeurs dans une
        liste de sommets.

        Args:
            liste_sommet: une liste de sommets.

        Returns:
            les deux plus petits sommets et
            la liste de sommets avec les deux sommets supprimés.
        """
        # Remplacer par heapq ? optimisation possible

        # Recupere dont les racines portent les plus petites etiquettes.

        arbre1 = min(liste_sommet, key=lambda x: x.racine.valeur)
        liste_sommet.remove(arbre1)
        arbre2 = min(liste_sommet, key=lambda x: x.racine.valeur)
        liste_sommet.remove(arbre2)

        return arbre1, arbre2, liste_sommet

    def creation_table_encodage(self, arbre):
        """
        Crée une table d'encodage pour les caractères présents
        dans l'arbre donné.

        Args:
            arbre: l'arbre binaire de Huffman contenant
            les caractères à encoder.

        Returns:
            Un dictionnaire où les clés sont les caractères
            présents dans l'arbre et les valeurs sont les codes binaire
            selon l'encodage de Huffman.
        """
        liste_sommet = arbre.parcours_prefixe(arbre.racine)
        liste_feuille = [
            sommet for sommet in liste_sommet if isinstance(sommet, tuple)]
        table_encodage = dict(liste_feuille)
        return table_encodage

    def encodage_text(self, table_encodage):
        """
        Encode le texte présent dans le fichier en utilisant
        la table d'encodage fournie.

        Args:
            table_encodage: Un dictionnaire où les clés sont les caractères
            présents dans l'arbre et les valeurs sont les codes binaire
            selon l'encodage de Huffman.

        Returns:
            Le texte encodé en binaire.
        """
        text = ouverture_fichier(self.file).read()
        res = ""
        for char in text:
            if char == " ":
                char = "SPC"
            if char == "\n":
                char = "LINE"
            res += table_encodage[char]
        return res
