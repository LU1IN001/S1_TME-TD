# Wilhem Blondel

def ouvre_fichier(nom: str) -> List[str]:
    """renvoie la liste des lignes du fichier texte ./nom.txt"""
    with open("C:/Users/wilhe/Desktop/Sorbonne Workspace/PPTI-Retrieved/Activité-9/"+nom+".txt", "r", encoding= "utf-8") as f:
        return f.readlines()

ponctuation : Set[str] = {" ", ",", ";", "'", "(", ")", ".", "!", "?", ":"}
exemple1: List[str] = ouvre_fichier("beaute")

def decompose_ligne(li: str, sep: Set[str]) -> List[str]:
    """Préconditions li contient un retour chariot 
    Décompose la ligne en une liste à partir des séparateurs indiqué et retire le retour chariot"""
    mot: str = ""
    res: List[str] = []
    c: str
    for c in li[:-2]:
        if c not in sep:
            mot = mot + c
        elif len(mot) > 0:
            res.append(mot)
            mot = ""
    
    if len(mot) > 0:
        res.append(mot)
            
    return res


assert decompose_ligne(exemple1[0], ponctuation) == ['Je', 'suis', 'belle', 'ô', 'mortels', 'comme', 'un', 'rêve', 'de', 'pierre']
assert decompose_ligne(exemple1[4], ponctuation) == []
assert decompose_ligne(exemple1[8], ponctuation) == ['Et', 'jamais', 'je', 'ne', 'pleure', 'et', 'jamais', 'je', 'ne', 'ris']

def minusculise(s: str) -> str:
    """Met en minsucule toutes les lettres majuscules"""
    k: int =  ord('a') - ord('A')
    res: str = ""
    c: str
    for c in s:
        if ord('A') <= ord(c) <= ord('Z'):
            res = res + chr(ord(c) + k)
        else:
            res = res + c
    return res


assert minusculise("bonjour") == "bonjour"
assert minusculise("BONJOUR") == "bonjour"
assert minusculise("Bonjour") == "bonjour"

def mots(lis: List[str], sep: Set[str]) -> List[str]:
    """Renvoie la liste de phrase en minuscule séparée par la ponctuation"""
    return [minusculise(e) for line in lis for e in decompose_ligne(line, sep)]

assert mots(exemple1, ponctuation)[:15] == ['je', 'suis', 'belle', 'ô', 'mortels', 'comme', 'un', 'rêve', 'de', 'pierre', 'et', 'mon', 'sein', 'où', 'chacun']

def dictionnaire_occ_mots(ms: List[str]) -> Dict[str, int]:
    """Renvoie un dictionnaire qui associe à chaque mots du texte son nombre d'occurrences"""
    res: Dict[str, int] = dict()
    m: str
    for m in ms:
        if m not in res:
            res[m] = 0
        res[m] = res[m] + 1
    return res

dico1 : Dict[str, int] = dictionnaire_occ_mots(mots(exemple1, ponctuation))

assert dico1["je"] == 5
assert dico1["belle"] == 1
assert dico1["jamais"] == 2

def hapax(dic: Dict[str, int]) -> Set[str]:
    """Renvoie les mots apparaissant seulement une fois de tout le texte"""
    return {k for k, v in dic.items() if v == 1}


assert len(hapax(dico1)) == 67
assert ("sphinx" in hapax(dico1)) == True
assert ("jamais" in hapax(dico1)) == False


def plus_frequent(dic: Dict[str, int]) -> str:
    """Renvoie le mot le plus fréquent d'un texte à partir du dictionnaire de fréquence"""
    v_max: int = -1
    m: str = ""
    for k, v in dic.items():
        if v_max < v:
            v_max = v
            m = k
    return m

assert plus_frequent(dico1) == "je"

# Suggestion 2

def dictionnaire_freq_mots(ms: List[str]) -> Dict[str, float]:
    """Associe à un moment sa fréqunce d'apparition dans le texte"""
    return {k: (v/len(ms)) for k, v in dictionnaire_occ_mots(ms).items()}

dico2 : Dict[str, float] = dictionnaire_freq_mots(mots(exemple1 , ponctuation))

assert abs(dico2["je"] - 0.04065040650406504) <= 10**-15
assert abs(dico2["belle"] - 0.008130081300813009) <= 10**-15

def distance_freq(d1: Dict[str, float], d2: Dict[str, float]) -> float:
    """Retourne la distance entre les dictionnaires de fréquence d1 et d2"""
    score: float = 100
    for m2, f2 in d2.items():
        if m2 in d1:
            score = score + 100*abs(d1[m2]-f2)
        else:
            score = score + 100*f2
    return score

# Suggestion 3

def jointure_dict_freq(d1: Dict[str, float], d2: Dict[str, float], l1: int, l2: int) -> Dict[str, float]:
    """Joint les deux dictionnaires de fréquence entre eux
    avec l1 la longueur du texte de d1 et d2 la longueur du texte de d2"""
    res: Dict[str, float] = dict()
    for (m1, f1), (m2, f2) in zip(d1.items(), d2.items()):
        if m1 in d2 and m1 not in res:
            res[m1] = (f1*l1 - d2[m1]*l2)/(l1+l2)
        elif m1 not in d2:
            res[m1] = (f1*l1)/(l1+l2)
        elif m2 not in d1:
            res[m2] = (f2*l2)/(l1+l2)
    return res

def dict_auteur(li: List[str], sep: Set[str]) -> Dict[str, float]:
    """
    Renvoie un dictionnaire de fréquence de mot fusionnée
    avec tous les fichiers textes renseignés dans li"""
    res: Dict[str, float] = dict()
    l1: int = 0
    l2: int = 0
    ready: bool = False
    for fich in li:
        mots_l: List[str] = mots(ouvre_fichier(fich), sep)
        d: Dict[str, float] = dictionnaire_freq_mots(mots_l)
        if not ready:
            res = d
            l1 = len(mots_l)
            ready = True
        else:
            l2 = len(mots_l)
            res = jointure_dict_freq(res, d, l1, l2)
            l1 = l1+l2
    return res

baudelaire : Dict[str, float] = dict_auteur(["beaute", "spleen", "albatros"], ponctuation)

def auteur(candidats: List[Tuple[str, Dict[str, float]]], titre: str, sep: Set[str]) -> str:
    """Renvoie l'auteur le plus probable ayant écrit le fichier indiqué par titre
    La liste candidats se construits comme suit: (auteur, fréquence)"""
    d_cible: Dict[str, float] = dictionnaire_freq_mots(mots(ouvre_fichier(titre), sep))
    res_auteur: str = ""
    best: float = 0 # Les scores commencent à 100 points
    for auteur, d in candidats:
        score: float = distance_freq(d, d_cible)
        if best < score:
            best = score
            res_auteur = auteur
    return res_auteur # Ne sera jamais vide sauf si len(candidats) == 0

# Suggestion 4

lettres_francais: Dict[str, float] = {
    "e": 0.1210,
    "a": 0.0711,
    "i": 0.0659,
    "s": 0.0651,
    "n": 0.0639,
    "r": 0.0607,
    "t": 0.0592,
    "o": 0.0502,
    "l": 0.0496,
    "u": 0.0449,
    "d": 0.0367,
    "c": 0.0318,
    "m": 0.0262,
    "p": 0.0249,
    "g": 0.0123,
    "b": 0.0114,
    "v": 0.0111,
    "h": 0.0111,
    "q": 0.0065,
    "y": 0.0046,
    "x": 0.0038,
    "j": 0.0034,
    "k": 0.0029,
    "w": 0.0017,
    "z": 0.0015
}

def decalage_ligne(li: str, dec: int) -> str:
    """Préconditions dec > 0 and dec < 26
    Decale les lettres de la lignes li"""
    res: str = ""
    c: str
    for c in li:
        if ord('a') <= ord(c) <= ord('z'):
            position_alphabet: int = ord(c) - ord('a')
            res = res + chr(ord('a') + (position_alphabet + dec)%26)
        elif ord('A') <= ord(c) <= ord('Z'):
            position_alphabet: int = ord(c) - ord('A')
            res = res + chr(ord('A') + (position_alphabet + dec)%26)
        else:
            res = res + c
    return res

    
assert decalage_ligne(" bonjour lu1in011 ", 3) == " erqmrxu ox1lq011 "
assert decalage_ligne(" bonjour lu1in011 ", 0) == " bonjour lu1in011 "


def dictionnaire_freq_lettre(ms: List[str]) -> Dict[str, float]:
    """Préconditions len(ms) > 0, ms est une liste de mot en minuscule
    Renvoie la fréquence d'apparitions des lettres contenue dans un texte"""
    nb_lettre_total: int = 0
    dres: Dict[str, float] = dict()
    cste: int =  ord('a') - ord('A')
    m: str
    for m in ms:
        # On ne va pas utiliser nos anciennes méthodes
        # Car la complexité de celle-ci est nécéssairement quadratique
        # Afin de pouvoir récupérer les lettres de la liste de str
        nb_lettre_total = nb_lettre_total + len(m)
        c_to_test: str = ""
        c: str
        for c in m:
            if ord('A') < ord(c) < ord('Z'):
                c_to_test = chr(ord(c) + cste)
            elif ord('a') < ord(c) < ord('z'):
                c_to_test = c
            if c_to_test != "":
                if c_to_test not in dres:
                    dres[c_to_test] = 0
                dres[c_to_test] = dres[c_to_test] + 1
    
    k: str
    for k in dres:
        dres[k] = dres[k]/nb_lettre_total
    
    return dres




def decode_cesar_auto(nom: str, sep: Set[str], compare_with: Dict[str, float]) -> int:
    """Décode automatiquement le fichier donné chiffré en code césar
    La fonction renvoie la valeur de la clé utilisé pour le déchiffrage"""
    fich: List[str]  = ouvre_fichier(nom)
    max_score: float = 0
    better_dec: int = 0
    decale1: List[str] = [decalage_ligne(minusculise(li), 0) for li in fich]
    d1: Dict[str, float] = dict()
    i: int
    for i in range(1, 27): # Nombre de lettre dans l'alphabet
        decale1: List[str] = [decalage_ligne(minusculise(li), i) for li in fich]
        d1: Dict[str, float] =  dictionnaire_freq_lettre(mots(decale1, sep))
        score1: float = distance_freq(d1, compare_with)
        if max_score < score1:
            max_score = score1
            better_dec = i
    print(d1)
    with open("C:/Users/wilhe/Desktop/Sorbonne Workspace/PPTI-Retrieved/Activité-9/"+nom+"-decrypte.txt", "w", encoding= "utf-8") as f:
        for lines in fich:
            
            f.write(decalage_ligne(lines[:-2], better_dec) +"\n") # On retire le chariot à la fin puis on el rajoute après decryptage

    return better_dec



