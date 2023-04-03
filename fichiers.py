import decryptage as d
from cryptage import Huffman


def ouverture_fichier(fichier):
    """ str -> file
    Ouvre un fichier texte.
    """

    fichier = open(fichier, "r", encoding='utf8')
    return fichier


def table_encodage(fichier):
    """ str -> tab
    Renvoie un tableau avec tous les éléments d'un fichier texte codés selon l'encodage de Huffman.
    """

    texte = ouverture_fichier(fichier)
    texte = texte.read()

    t = Huffman(texte)
    tab = t.occurence()

    abr = t.creation_arbre(tab)
    tab = t.creation_table_encodage(abr)

    return tab


def compression_char(fichier):
    """ str -> tab
    Renvoie un tableau des caractères d'un texte codés selon l'encodage de Huffman.
    """

    tab = table_encodage()
    tab2 = []
    texte = ouverture_fichier(fichier)
    texte = texte.read()
    for lettre in texte:
        for i in range(len(tab)):
            if lettre == tab[i][0]:
                tab2 += tab[i][1]
    return tab2


def compression_texte():
    """ -> str
    Renvoie un string des caractères d'un texte codés selon l'encodage de Huffman."""

    tab = compression_char()
    encodage = str()
    for k in range(len(tab)):
        encodage += str(tab[k])
    return encodage


def enregistrement_encodage():
    """Enregistre le fichier texte encodé."""

    texte = open("fichier_encode.txt", "w")
    a = compression_texte()
    texte.write(a)
    texte.close()
    texte = open("cle_encodage.txt", "w", encoding='utf8')
    tab = str(table_encodage())
    texte.write(tab)
    texte.close()


def decodage_texte(fichier_a_decoder, cle):
    """ str, tab -> tab
    Renvoie un tableau avec tous les éléments d'un fichier texte décodés.
    """

    def set_texte_encode(self, texte_encode):
        self.texte_encode = open(texte_encode, "r", encoding='utf8').read()


def decompression_texte():
    """ -> str
    Renvoie un texte décodé."""

    tab = decodage_texte()
    decodage = str()
    for k in range(len(tab)):
        decodage += str(tab[k])
    return decodage


def enregistrement_decodage():
    """Enregistre le fichier texte décodé."""

    texte = open("fichier_decode.txt", "w", encoding='utf8')
    a = decompression_texte()
    texte.write(a)
    texte.close()
