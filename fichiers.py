import decryptage as d
import cryptage as c

class Fichier:
    def __init__(self, f, c, t):
        self.fichier = f
        self.cle = c
        self.texte_encode = t
    
    # @property
    # def fichier(self):
    #     return self.fichier
    
    # @property
    # def cle(self):
    #     return self.cle
    
    # @property
    # def texte_encode(self):
    #     return self.texte_encode
    
    def set_fichier(self, fichier):
        self.fichier = fichier

    def set_cle(self, cle):
        self.cle = cle

    def set_texte_encode(self, texte_encode):
        self.texte_encode = texte_encode

    def table_encodage(self):
        """
        Attribue à self.cle un tableau avec tous les éléments d'un fichier texte codés selon l'encodage de Huffman.
        """
        
        texte = self.fichier
        t = c.Huffman(texte)
        tab = t.occurence()
        abr = t.creation_arbre(tab)
        self.cle = t.creation_table_encodage(abr)

    def compression_texte(self):
        """ -> str
        Encode le texte présent dans le fichier en utilisant la table d'encodage fournie.
        Returns:
            Le texte encodé en binaire.
        """
        
        encodage = ""
        for lettre in self.fichier:
            encodage += self.cle.get(lettre)
        return encodage

    def enregistrement_encodage(self):
        """ -> str
        Enregistre le fichier texte encodé."""
        
        texte = open("fichier_encode.txt", "w")
        a = self.compression_texte()
        texte.write(a)
        texte.close()
        return a

    def enregistrement_cle(self):
        """ -> str
        Enregistre la clé de l'encodage de Huffman."""
        
        texte = open("cle_encodage.txt", "w", encoding='utf8')
        dic = str(self.cle)
        texte.write(dic)
        texte.close()
        return dic

    def decodage_texte(self):
        """ -> str
        Renvoie un texte décodé."""
        
        tmp = ""
        decodage = ""
        self.cle = eval(self.cle)
        for code in self.texte_encode:
            tmp += code
            a = d.decodage_char(self.cle, tmp)
            if a is not None:
                decodage += a
                tmp = ""
        return decodage

    def enregistrement_decodage(self):
        """ -> str
        Renvoie et enregistre le fichier texte décodé.
        """
        
        texte = open("fichier_decode.txt", "w", encoding='utf8')
        a = self.decodage_texte()
        texte.write(a)
        texte.close()
        return a
