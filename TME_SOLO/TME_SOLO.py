# Wilhem BLONDEL (21212622)

# Question 1.1

def nbSup(l: List[int], n: int) -> List[int]:
    """Retourne les éléments de la liste l supérieurs ou égaux à la valeur n"""
    res: List[int] = []
    i: int
    for i in l:
        if i >= n:
            res.append(i)
    return res

assert nbSup([1, 2, 3, 4, 6, 7], 6) == [6, 7]
assert nbSup([1, 2, 3, 4, 6, 7], 1) == [1, 2, 3, 4, 6, 7]
assert nbSup([1, 2, 3, 4, 6, 7], 8) == []
assert nbSup([], 12) == []


# Question 1.2
def nbSup_comp(l: List[int], n: int) -> List[int]:
    """Retourne les éléments de la liste l supérieurs ou égaux à la valeur n"""
    return [i for i in l if i >= n]

assert nbSup_comp([1, 2, 3, 4, 6, 7], 6) == [6, 7]
assert nbSup_comp([1, 2, 3, 4, 6, 7], 1) == [1, 2, 3, 4, 6, 7]
assert nbSup_comp([1, 2, 3, 4, 6, 7], 8) == []
assert nbSup_comp([], 12) == []

# Question 1.3
def sommeCumulee(l: List[int]) -> List[int]:
    """Retourne la liste des sommes cumulées de l"""
    if len(l) == 0:
        return []
    
    res: List[int] = [l[0]]
    i: int
    for i in l[1:]:
        res.append(res[-1] + i)
    return res

assert sommeCumulee([1,2,0,3]) == [1,3,3,6]
assert sommeCumulee([]) == []
assert sommeCumulee([10,0,1,5,6]) == [10, 10, 11, 16, 22]

# Question 1.4

def verifierPassword(pswd: str) -> bool:
    """Indique si le mot de passe donnée respecte les conditions"""
    if len(pswd) < 6:
        return False
    maj: bool = False
    minu: bool = False
    chiffre: bool = False
    cara: bool = False
    special: Set[str] = { "@", "?", ".", "!" }
    c: str
    for c in pswd:
        if ord('a') <= ord(c) <= ord('z'):
            minu = True
        elif ord('A') <= ord(c) <= ord('Z'):
            maj = True
        elif ord('1') <= ord(c) <= ord('9'):
            chiffre = True
        elif c in special:
            cara = True
    return minu and maj and chiffre and cara

assert verifierPassword("Toto?1")
assert not verifierPassword("toto!1")
assert verifierPassword("Test123@")
assert not verifierPassword("Ta1!")


# Exercice 2

Match = Tuple[str, str, int, int]

# Question 2.1

def ajouterMatch(challenger1: str, challenger2: str, score1: int, score2: int, bd: List[Match]) -> List[Match]:
    """Préconditions score1 >= 0 and score2 >= 0
    Retourne la nouvelle base de donnée des match avec le match renseigné"""
    return [(challenger1, challenger2, score1, score2)] + bd

assert ajouterMatch("France","Australie", 2, 0, [("Qatar","Equateur",0,2)]) == [("France","Australie",2,0), ("Qatar","Equateur",0,2)]
assert ajouterMatch("Angleterre", "Iran", 2, 1, [("France","Australie",2,0), ("Qatar","Equateur",0,2)]) == [("Angleterre","Iran",2,1), ("France","Australie",2,0), ("Qatar","Equateur",0,2)]
assert ajouterMatch("Tunisie","Danemark",0,0, [("USA","Pays de Galles",0,0)]) == [("Tunisie","Danemark",0,0), ("USA","Pays de Galles",0,0)]


# Question 2.2

def maximumDifference(bd: List[Match]) -> Optional[Match]:
    """Retourne le match ayant une différence de score maximum dans la liste"""
    max_diff: float = 0 # la fonction abs renvoie un flottant selon MrPython
    store_m: Optional[Match] = None
    m: Match
    for m in bd:
        _, _, score1, score2 = m
        if abs(score1 - score2) > max_diff:
            max_diff = abs(score1 - score2)
            store_m = m
    return store_m


assert maximumDifference([("France","Australie",2,0), ("Angleterre","Iran",2,1), ("Qatar","Equateur",0,2)]) == ("France","Australie",2,0)
assert maximumDifference([("Tunisie","Danemark",0,0), ("USA","Pays de Galles",0,0)]) == None

assert maximumDifference([]) == None
    
