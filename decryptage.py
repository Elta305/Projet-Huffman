def decodage_char(tab, char):
    """ tab, tab -> tab
        Retourne un tableau avec le caractère char décodé mais sans le nombre d'itération.
    """
    
    for i in range(len(tab)):
        tmp = tab[i][1]
        if char == tmp:
            return tab[i][0]
    return None

def decodage(tab):
    """ tab, tab -> tab
        Retourne un tableau avec toutes les valeurs décodées.
    """
    
    tab_decodage = []
    for i in range(len(tab)):
        tab_decodage.append(decodage_char(tab, tab[i][1]))
    return tab_decodage
