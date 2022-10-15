# Wilhem Blondel
from typing import List
Polyn = List[int]

ex1 : Polyn = [3, 0, 2]
ex2 : Polyn = [1, -1, 1, -1, 0]
ex3 : Polyn = [27]
ex4 : Polyn = []

def degre(polynome: Polyn) -> int:
    """Retourne le degré du polynôme"""
    i: int
    for i in range(len(polynome)-1, -1, -1):
        if(polynome[i] != 0):
            return i
    return 0

assert degre(ex1) == 2
assert degre(ex2) == 3
assert degre(ex3) == 0
assert degre(ex4) == 0
assert degre([0,0,0,0,0]) == 0


def somme(p1: Polyn, p2: Polyn) -> Polyn:
    """Retourne la somme des polynômes donnés"""
    pres: Polyn = []
    p1_len: int = len(p1)
    p2_len: int = len(p2)
    i: int
    for i in range(max(p1_len,p2_len)):
        if(i >= p2_len):
            pres.append(p1[i])
        elif(i >= p1_len):
            pres.append(p2[i])
        else:
            pres.append(p1[i] + p2[i])
    return pres

assert somme(ex1, ex1) == [6, 0, 4]
assert somme(ex1, ex4) == ex1
assert somme(ex1, ex2) == [4, -1, 3, -1, 0]

def normalise(p: Polyn) -> Polyn:
    """Retire tous les termes nulle d'un polynôme qui ne servent à rien"""
    i: int
    for i in range(len(p)-1, -1, -1):
        if(p[i] != 0):
            return p[:i+1]
    return []

assert normalise(ex1) == ex1
assert normalise(ex2) == [1, -1, 1, -1]
assert normalise([0, 0, 0, 0, 0]) == []
assert normalise([]) == []


def produit(p1: Polyn, p2: Polyn) -> Polyn:
    """Retourne le produit des polynômes p1 et p2"""
    i: int
    j: int
    k: int
    l: int
    m: int
    pres: Polyn = []
    d_1: int = degre(p1)
    d_2: int  = degre(p2)
    if(p1 == [] or p2 == []):
        # C'est un cas particulier inintéressant car on multiplie par 0
        # Afin d'éviter de vérifier des index qui n'existent pas
        # On return immédiatemment une liste vide
        return []
    for j in range(d_1 + d_2 + 1):
        # Initialisation de la liste à modifier
        # On modifie les index à l'envers, d'où l'intérêt de créer une
        # liste au préalable pour pouvoir évaluer les plus haut index
        pres.append(0)
    if(d_1 >= d_2):
        for i in range(d_1 + 1):
            for k in range(d_2 + 1):
                pres[d_1+d_2-k-i] = pres[d_1+d_2-k-i] + p1[d_1-i] * p2[d_2-k]
        return pres
    else:
        for l in range(d_2 + 1):
            for m in range(d_1 + 1):
                pres[d_1+d_2-l-m] = pres[d_1+d_2-l-m] + p1[d_1-m] * p2[d_2-l]
        return pres


assert normalise(produit(ex1, ex4)) == []
assert normalise(produit(ex1, ex1)) == [9, 0, 12, 0, 4]
assert normalise(produit(ex1, ex2)) == [3, -3, 5, -5, 2, -2]
assert normalise(produit(ex1, ex3)) == [27* 3, 0, 27* 2]
assert normalise(produit([1, 1], [1, 0, 1])) == [1, 1, 1, 1]

