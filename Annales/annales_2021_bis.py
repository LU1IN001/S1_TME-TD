from typing import *
Dep = Dict[str, Set[str]]

LicenseInfo: Dep = {"BDD": {"Alice", "Bob", "Carole"}, 
                    "Lambda": {"Alice", "Bob", "Carole", "David", "Elise"}, 
                    "POO": {"Bob", "Elise"},
                    "IA": set(),
                    "Compil": {"Alice", "Bob", "David"}}

LicenseBio: Dep = {"Microbio": {"Fadia", "David"}, 
                    "Genetique": {"Fadia", "David"}, 
                    "Animale": {"Fadia"}}

LicenseMath: Dep = {"Topologie": {"Elise", "Gwenael"}, 
                    "AlgLin": {"Elise", "Gwenael"}}

Faculte2Science: List[Dep] = [LicenseBio, LicenseInfo, LicenseMath]

def effectifs_UE(d: Dep, ue: str) -> int:
    if ue in d:
        return len(d[ue])
    else:
        return 0

def etudiants(d: Dep) -> Set[str]:
    res: Set[str] = set()
    v: Set[str]
    for _, v in d.items():
        res = res | v
    return res

def inscriptions_etu(d: Dep, etu:str) -> Set[str]:
    return {k for k,v in d.items() if etu in v}

def inscriptions_tous(d: Dep) -> Dict[str, Set[str]]:
    return {etu: inscriptions_etu(d, etu) for etu in etudiants(d)}

def doubles_licenses(dl: List[Dep]) -> Set[str]:
    res: Set[str] = set()
    seen: Set[str] = set()
    d: Dep
    for d in dl:
        e: str
        for e in etudiants(d):
            if e in seen:
                res.add(e)
            seen.add(e)
    return res

# Exercice 3

def sep_eq_possible(li: List[int]) -> bool:
    s1: int = 0
    s2: int  = 0
    i: int = 0
    while i < len(li):
        if s1 <= s2:
            s1 = s1 + li[i]
        else:
            s2 = s2 + li[i]
        i= i + 1
    return s1 == s2


def sep_eq(li: List[int]) -> Optional[Tuple[List[int], List[int]]]:
    l1 : List[int] = []
    s1: int = 0
    l2: List[int] = []
    s2: int = 0
    i: int = 0
    while i < len(li):
        if s1 <= s2:
            l1.append(li[i])
            s1 = s1 + li[i]
        else:
            l2.append(li[i])
            s2 = s2 + li[i]
    if s1 == s2:
        return (l1, l2)
    
# Exercice 4

Pixel = Tuple[int, int, int]

def moyenne(li: List[int]) -> int:
    """Préconditions len(li) > 0"""
    s: int = 0
    e: int
    for e in li:
        s = s + e
    return int(s/len(li))

def est_noir(p: Pixel) -> bool:
    r, g, b = p
    return r == 0 and g == 0 and b == 0

def listes_par_couleur(li: List[Pixel]) -> Tuple[List[int], List[int], List[int]]:
    l1: List[int] = []
    l2: List[int] = []
    l3: List[int] = []
    e: Pixel
    for e in li:
        r, g, b = e
        l1.append(r)
        l2.append(g)
        l3.append(b)
    return (l1, l2, l3)

def pixel_moyen(lp: List[Pixel]) -> Pixel:
    """Préconditions len(lp) > 0"""
    r, g, b = listes_par_couleur(lp)
    return (moyenne(r), moyenne(g), moyenne(b))

Im = List[List[Pixel]]

def compression(im: Im) -> Im:
    """Préconditions len(im)%2 == 0 and len(im[0])%2 == 0"""
    res: Im = [[]]
    index: int = 0
    i: int
    j: int
    for i in range(0, len(im), 2):
        if i >= 2:
            res.append([])
            index = index + 1
        for j in range(0, len(im), 2):
            res[index].append(pixel_moyen([im[i][j], im[i][j+1], im[i+1][j], im[i+1][j+1]]))
    return res