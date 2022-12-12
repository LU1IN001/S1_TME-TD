
from typing import List, Dict

def valeur_decomposition(decomp: Dict[int, int]) -> int:
    """Retourne la valeur du dictionnaire de domposition de facteurs"""
    res: int = 1
    e: int
    for e in decomp:
        res = res*e**decomp[e]
    return res

assert valeur_decomposition({2:1, 3:1, 5:1}) == 30
assert valeur_decomposition({2:3, 7:1}) == 56
assert valeur_decomposition({2:10}) == 1024

def decomposition(l: List[int]) -> Dict[int, int]:
    """Retourne le dicitionnaire qui décompose le produit de facteurs"""
    res: Dict[int, int] = dict()
    e: int
    for e in l:
        if not e in res:
            res[e] = 0
        res[e] = res[e]+1
    return res

assert decomposition([2, 3, 5]) == {2: 1, 3: 1, 5: 1}
assert decomposition([2, 2, 2, 7]) == {2: 3, 7: 1}
assert decomposition([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == {2: 10}

def liste_nombres_premiers(n: int) -> List[int]:
    """Préconditions n >= 2
    Retourne la liste des nombres premiers jusqu'à n"""
    return [i for i in range(2, n+1)]

print(liste_nombres_premiers(10))
assert liste_nombres_premiers(10) == [2, 3, 5, 7]
assert liste_nombres_premiers(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
assert liste_nombres_premiers(2) == [2]


def liste_facteurs_premiers(n: int) -> List[int]:
    """Préconditions n >= 2
    Renvoie la liste correspondant à la décomposition en facteur premier de n"""
    nb_premiers: List[int] = liste_nombres_premiers(n)
    res: List[int] = []
    n_copy: int = n
    i: int
    for i in nb_premiers:
        while n_copy%i == 0 and n_copy != 1:
            res.append(i)
            n_copy = n_copy//i
    return res
        
assert liste_facteurs_premiers(30) == [2, 3, 5]
assert liste_facteurs_premiers(56) == [2, 2, 2, 7]
assert liste_facteurs_premiers(1024) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
assert liste_facteurs_premiers(13) == [13]

def decomposition_facteurs_premiers(n: int) -> Dict[int, int]:
    """Préconditions n >= 2
    Retourne le dictionanaire correspondant à la décomposition en produit de facteur de premiers de n"""
    return decomposition(liste_facteurs_premiers(n))

assert decomposition_facteurs_premiers(1024) == {2: 10}
assert decomposition_facteurs_premiers(30) == {2: 1, 3: 1, 5: 1}
assert decomposition_facteurs_premiers(56) == {2: 3, 7: 1}
assert decomposition_facteurs_premiers(13) == {13: 1}
