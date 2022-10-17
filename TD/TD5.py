from typing import List
from typing import TypeVar
from math import sqrt

T = TypeVar('T')
# Exercice 6.1

def repetition(x: T, k: int) -> List[T]:
    """Préconditions k >= 0
    Retounrne une liste répétant k fois l'élément x"""
    res: List[T] = []
    i: int
    for i in range(k):
        res.append(x)
    return res


def repetition_bloc(x: List[T], k: int) -> List[T]:
    """Préconditions k >= 0
    Retourne la concaténation de x k fois"""
    return x*k

# Exercice 6.2

def max_liste(l: List[float]) -> float:
    """Précondtions len(l) > 0
    Retourne la valeur maximal de la liste"""
    max: float = l[0]
    i: float
    for i in l:
        if i > max:
            max = i
    return max

def nb_occurrences(l: List[T], x: T) -> int:
    """Préconditions x est de même type que les éléments de l
    Retourne le nombre d'occurences de x dans l"""
    res: int = 0
    i: T
    for i in l:
        if i == x:
            res = res + 1
    return res

def nb_max(l: List[float]) -> int:
    """Préconditions len(l) > 0
    Retourne le nombre de maximum contenu dand l"""
    return nb_occurrences(l, max_liste(l))

# Exercice 6.7

def list_mult(l: List[int], k: int) -> List[int]:
    """Retourne la liste donnée multipliée par k"""
    res: List[int] = []
    i: int
    for i in l:
        res.append(i*k)
    return res

def list_div(l: List[int], k: int) -> List[int]:
    """Préconditions k != 0
    Retourne la liste divisée par k en supprimant tous les éléments non divisibles par k"""
    res: List[int] = []
    i: int
    for i in l:
        if i%k == 0:
            res.append(i//k)
    return res

# Exercice 6.6

def somme(l: List[float]) -> float:
    """Retourne la somme de l"""
    res: float = 0
    i: float
    for i in l:
        res = res + i
    return res

def moyenne(l: List[float]) -> float:
    """Précondition len(l) > 0
    Retourne la moyenne de l"""
    return somme(l)/len(l)

def carres(l: List[float]) -> List[float]:
    """Retourne une liste des carrées des élemets de l"""
    res: List[float] = []
    i: float
    for i in l:
        res.append(i**2)
    return res

def variance(l: List[float]) -> float:
    """Préconditions len(l) > 0
    Retourne la variance de la liste l"""
    return moyenne(carres(l)) - moyenne(l)**2

def ecart_type(l: List[float]) -> float:
    """Préconditions len(l) > 0
    Retourne la variance de la liste l"""
    return sqrt(variance(l))

# Exercice 4.4



