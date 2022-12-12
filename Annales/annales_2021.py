from typing import *
T = TypeVar('T')
# Exercice 1

#1.1
def nb_occ(mot: str, c: str) -> int:
    """Préconditions len(c) == 1"""
    return len([e for e in mot if e == c])


#1.2
def est_voyelle(c: str) -> bool:
    """Préconditions len(c) == 1"""
    return c in {'a', 'e', 'i', 'o', 'u', 'y'}

#1.3
def nb_voyelle(mot: str) -> int:
    return len([c for c in mot if est_voyelle(c)])

#1.4
def rm_voyelle(mot: str) -> str:
    res: str = ""
    c: str
    for c in mot:
        if not est_voyelle(c):
            res = res + c
    return res

#1.5
def consonne_ou_voyelle(mot: str) -> str:
    res: str = ""
    c: str
    for c in mot:
        if est_voyelle(c):
            res = res + "v"
        else:
            res = res + "c"
    return res

# Exercice 2

#2.1
Composition = Dict[str, float]
def quantite_dans(c: Composition, nut:str) -> float:
    if nut in c:
        return c[nut]
    else:
        return 0.0

#2.2
def energie(c: Composition) -> float:
    return quantite_dans(c, "glucides")*4 + quantite_dans(c, "protides")*4 + quantite_dans(c, "lipides")*9

#2.3
def quantite_eau(c: Composition) -> float:
    s: float = 0
    k: str
    for k in c:
        s = s + c[k]
    return 100.0-s

BaseAliments = Dict[str, Composition]

#2.4
def plus_gras_que(bd: BaseAliments, q: float) -> List[str]:
    """Préconditions q > 0"""
    return [k for k,v in bd.items() if quantite_dans(v, "lipides") >= q]

#2.5
def composition_recette(bd: BaseAliments, rec: List[Tuple[str, float]]) -> Composition:
    res: Dict[str, float] = dict()
    for k,p in rec:
        c: Composition = bd[k]
        nut: str
        for nut in c:
            if nut not in res:
                res[nut] = 0
            res[nut] = res[nut] + c[nut]*(p/100)
    return res

#Exercice 4
#4.1
def triplet_date(d: str) -> Tuple[int, int, int]:
    return (int(d[:2]), int(d[3:5]), int(d[6:]))

#4.2
def avant_ou_egale(d1: str, d2: str) -> bool:
    j1, m1, y1 = triplet_date(d1)
    j2, m2, y2 = triplet_date(d2)
    return y1 < y2 or (y1 == y2 and m1 < m2) and (y1 == y2 and m1==m2 and j1<=j2)

#4.3
Sorties = List[Tuple[str, str, str]]
def sorties_categorie(bd: Sorties, cat: str) -> Sorties:
    return [(d,t,c) for d,t,c in bd if cat==c]

#4.4
def sorties_ajout(db: Sorties, sort: Tuple[str, str, str]) -> Sorties:
    dsort, _, _ = sort
    added: bool = False 
    res: Sorties = []
    for d,t,c in db:
        if avant_ou_egale(d, dsort) and not added: 
            res.append(sort)
            added = True
        res.append((d,t,c))
    return res

#4.5
def deux_sorties_rassemblees(s1: Sorties, s2: Sorties) -> Sorties:
    lres: Sorties = []
    e: Tuple[str, str, str]
    for e in s1:
        lres = sorties_ajout(s2, e)
    return lres

# Alternative (plus optimisée)
def deux_sorties_rassemeblees2(s1: Sorties, s2: Sorties) -> Sorties:
    i: int = 0
    j: int = 0
    lres: Sorties = []
    while i < len(s1) and j < len(s2):
        d1, _, _ = s1[i]
        d2, _, _ = s2[j]
        if avant_ou_egale(d1, d2):
            lres.append(s1[i])
            i=i+1
        else:
            lres.append(s2[j])
            j=j+1
    if i < len(s1):
        lres = lres + s1[i:]
    else:
        lres = lres + s2[j:]
    return lres # + s1[i:] + s2[j:]
