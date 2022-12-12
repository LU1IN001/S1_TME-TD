def est_voyelle(c : str) -> bool:
    """Précondition : len(c) == 1
    Retourne True si et seulement si c est une voyelle
    miniscule ou majuscule.
    """
    return (c == 'a') or (c == 'A') \
    or (c == 'e') or (c == 'E') \
    or (c == 'i') or (c == 'I') \
    or (c == 'o') or (c == 'O') \
    or (c == 'u') or (c == 'U') \
    or (c == 'y') or (c == 'Y')

# Jeu de tests
assert est_voyelle('a') == True
assert est_voyelle('E') == True
assert est_voyelle('b') == False
assert est_voyelle('y') == True
assert est_voyelle('z') == False


def nb_voyelles(s: str) -> int:
    """Retourne le nombre de voyelle contenu dans la chaîne s"""
    res: int = 0
    e: str
    for e in s:
        if est_voyelle(e):
            res = res + 1
    return res

assert nb_voyelles('la maman du petit enfant le console') == 12
assert nb_voyelles('mr brrxcx') == 0
assert nb_voyelles('ai al o ents') == 5
assert nb_voyelles('la maman du bébé le réconforte') == 8

def est_voyelle_accent(c: str) -> bool:
    """Préconditions: len(c) == 1
    Renvoie True si le caractère c est une voyelle. Ajoute le test pour les accents"""
    return est_voyelle(c) or c == "é" or c == "è" or c == "î" \
        or c == "à" or c=="ô" or c == "â" or c == "ö" or c == "Ô" \
        or c == "Â" or c == "Ö"

# Jeu de tests
assert est_voyelle_accent('a') == True
assert est_voyelle_accent('E') == True
assert est_voyelle_accent('ô') == True
assert est_voyelle_accent('é') == True
assert est_voyelle_accent('z') == False

def nb_voyelles_accents(s: str) -> int:
    """Retourne le nombre de voyelle contenu dans la chaîne"""
    res: int = 0
    e: str
    for e in s:
        if est_voyelle_accent(e):
            res = res + 1
    return res

assert nb_voyelles_accents('la maman du bébé le réconforte') == 11

def sans_voyelle(s: str) -> str:
    """Renvoie la chaîne de caractère sans les voyelles"""
    res: str = ""
    e: str 
    for e in s:
        if not est_voyelle(e):
            res = res + e
    return res

assert sans_voyelle('aeiouy') == ''
assert sans_voyelle('la balle au bond rebondit') == 'l bll  bnd rbndt'
assert sans_voyelle('mr brrxcx') == 'mr brrxcx'


def mot_mystere(s: str) -> str:
    res: str = ""
    e: str
    for e in s:
        if est_voyelle(e):
            res = res + "_"
        else:
            res = res + e
    return res

assert mot_mystere('aeiouy') == '______'
assert mot_mystere('la balle au bond rebondit bien') == 'l_ b_ll_ __ b_nd r_b_nd_t b__n'
assert mot_mystere('mr brrxcx') == 'mr brrxcx'

