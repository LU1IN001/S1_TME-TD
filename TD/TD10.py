from typing import *
T= TypeVar('T')
# Exercice 12.1

def censurer(l: List[str], s: Set[str]) -> None:
    """***Procédure***
    Censure les éléments de la liste l contenu dans s"""
    i: int
    for i in range(len(l)):
        if l[i] in s:
            l[i] = "***CENSURE***"

def decaler(l: List[T], dec: int) -> None:
    """***Procédure***
    décale la liste l d'un pas de dec"""
    i: int
    if dec >= 0:
        for i in range(1, len(l)-dec%len(l)):
            tmp: T = l[-i]
            l[-i] = l[-i-dec%len(l)]
            l[-i-dec%len(l)] = tmp
    else:
        for i in range(len(l)-dec%len(l) + 2):
            tmp: T = l[i]
            l[i] = l[i-dec%len(l)]
            l[i-dec%len(l)] = tmp


def decaler2(l: List[T], dec: int) -> None:
    """***Procédure***
    décale la liste l d'un pas de dec"""
    i: int
    tmp: T
    for _ in range(dec%len(l)):
        tmp = l[-1]
        for i in range(len(l)-1):
            l[-i-1]=l[-i-2]
        l[0] = tmp

l1 : List[int] = [1, 2, 3, 4, 5, 6]
decaler(l1, 5)
print(l1)
