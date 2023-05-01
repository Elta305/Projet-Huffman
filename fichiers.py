import encodage as e

class Fichier:
    def __init__(self, fn, f, c, t):
        self._filename = fn
        self._fichier = f
        self._cle = c
        self._texte_encode = t
    
    @property
    def filename(self):
        return self._filename
    @filename.setter
    def filename(self, fn):
        self._filename = fn

    @property
    def fichier(self):
        return self._fichier
    @fichier.setter
    def fichier(self, f):
        self._fichier = f
    
    @property
    def cle(self):
        return self._cle
    @cle.setter
    def cle(self, c):
        self._cle = c
    
    @property
    def texte_encode(self):
        return self._texte_encode
    @texte_encode.setter
    def texte_encode(self, te):
        self._texte_encode = te

    def creation_arbre(self):
        """ -> abr
        Renvoie un arbre de Huffman à partir du texte présent dans le fichier.
        """
        texte = self.fichier
        t = e.Huffman(texte)
        dico = t.occurence()
        abr = t.creation_arbre(dico)
        return abr, t
    
    def table_encodage(self):
        """
        Attribue à self.cle un tableau avec tous les éléments d'un fichier texte codés selon l'encodage de Huffman.
        """
        
        abr = self.creation_arbre()
        abr, t = abr[0], abr[1]
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
        Enregistre le fichier texte encodé.
        """
        
        texte = open(f"{self.filename}_encode.txt", "w")
        a = self.compression_texte()
        texte.write(a)
        texte.close()
        return a

    def enregistrement_cle(self):
        """ -> str
        Enregistre la clé de l'encodage de Huffman.
        """
        
        texte = open(f"{self.filename}_cle.key", "w", encoding='utf8')
        dic = str(self.cle)
        texte.write(dic)
        texte.close()
        return self.cle

    def decodage_texte(self):
        """ -> str
        Renvoie un texte décodé.
        """
        
        tmp = ""
        decodage = ""
        for code in self.texte_encode:
            tmp += code
            a = e.decodage_char(self.cle, tmp)
            if a is not None:
                decodage += a
                tmp = ""
        return decodage

    def enregistrement_decodage(self):
        """ -> str
        Renvoie et enregistre le fichier texte décodé.
        """
        
        if "_encode" in self.filename:
            tmp = self.filename.split("_")
            self.filename = tmp[0]
        texte = open(f"{self.filename}_decode.txt", "w", encoding='utf8')
        a = self.decodage_texte()
        texte.write(a)
        texte.close()
        return a
