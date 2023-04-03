import decryptage as d

class Fichier:
    def __init__(self):
        self.fichier = None
        self.cle = None
        self.texte_encode = None
    
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
        self.fichier = open(fichier, "r", encoding = 'utf8').read()

    def set_cle(self, cle):
        self.cle = open(cle, "r", encoding = 'utf8').read()

    def set_texte_encode(self, texte_encode):
        self.texte_encode = open(texte_encode, "r", encoding = 'utf8').read()

    # def ouverture_fichier(self, fichier):
    #     """ str -> file
    #     Ouvre un fichier texte.
    #     """
        
    #     fichier = open(fichier, "r", encoding = 'utf8')
    #     return fichier

    def table_encodage(self):
        """ str -> tab
        Renvoie un tableau avec tous les éléments d'un fichier texte codés selon l'encodage de Huffman.
        """
        
        texte = self.fichier
        # A implémenter, voir avec Kaan
        # tab = nuk(texte)
        # abr = creation_arbre(tab)
        # tab = encodage(tab, abr)
        # return tab

    def compression_char(self):
        """ str -> tab
        Renvoie un tableau des caractères d'un texte codés selon l'encodage de Huffman.
        """

        texte = self.fichier
        tab = self.table_encodage()
        tab2 = []
        for lettre in texte:
            for i in range(len(tab)):
                if lettre == tab[i][0]:
                    tab2 += tab[i][1]
        return tab2

    def compression_texte(self):
        """ -> str
        Renvoie un string des caractères d'un texte codés selon l'encodage de Huffman."""
        
        tab = self.compression_char()
        encodage = str()
        for k in range(len(tab)):
            encodage += str(tab[k])
        return encodage

    def enregistrement_encodage(self):
        """Enregistre le fichier texte encodé."""
        
        texte = open("fichier_encode.txt", "w")
        a = self.compression_texte()
        texte.write(a)
        texte.close()
        return a

    def enregistrement_cle(self):
        """Enregistre la clé de l'encodage de Huffman."""
        
        texte = open("cle_encodage.txt", "w", encoding='utf8')
        tab = str(self.table_encodage())
        texte.write(tab)
        texte.close()
        return tab

    def decodage_texte(self):
        """ str, tab -> tab
        Renvoie un tableau avec tous les éléments d'un fichier texte décodés.
        """

        tmp = []
        tab2 = []
        for code in self.texte_encode:
            tmp.append(int(code))
            a = d.decodage_char(self.cle, tmp)
            if a is not None:
                tab2.append(a)
                tmp = []
        return tab2

    def decompression_texte(self):
        """ -> str
        Renvoie un texte décodé."""
        
        tab = self.decodage_texte()
        decodage = str()
        for k in range(len(tab)):
            decodage += str(tab[k])
        return decodage

    def enregistrement_decodage(self):
        """Enregistre le fichier texte décodé."""
        
        texte = open("fichier_decode.txt", "w", encoding='utf8')
        a = self.decompression_texte()
        texte.write(a)
        texte.close()
