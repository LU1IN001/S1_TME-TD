from typing import Callable, Tuple, List, TypeVar
T = TypeVar('T')

def fibo(n: int) -> int:
    """Précondtions n >= 1"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fibofast(n: int, a: int, b: int) -> int:
    """Précondtions n >= 0 and a >= 0 and b >= 0"""
    if n == 0:
        return a
    else:
        return fibofast(n-1, b, a + b)

def fibit(n: int) -> int:
    a: int = 0
    b: int = 1
    prev: int = b
    i: int = 0
    while i < n:
        prev = b
        b = a + b
        a = prev
        i = i + 1
    return a


def divination(oracle: Callable[[int], str], a: int, b: int) -> int:
    """Précondition : l'oracle retourne la chaîne 'plus petit',
    'plus grand'ou 'égal'
    Précondition : b > a >= 0
    Retourne le nombre d'étapes permettant de deviner le nombre caché,
    selon les réponses données par l'oracle.
    Ce nombre est compris entre les bornes a et b (incluses)
    """
    i: int
    for i in range(a, b):
        if (oracle(i) == 'égal'):
            return i + 1 - a
    # On ne sort jamais de la boucle
    return b

def oracle42(k: int) -> str:
    """Indique si k est 'plus petit', 'plus grand' ou 'égal'"""
    if k == 42:
        return 'égal'
    elif k < 42:
        return 'plus petit'
    else:
        return 'plus grand'

def divination_rec(oracle: Callable[[int], str], a: int, b: int, n: int) -> int:
    m: int = (a + b)//2
    if oracle(m) == 'égal':
        return n + 1
    elif oracle(m) == 'plus grand':
        return divination_rec(oracle, a, m - 1, n + 1)
    else:
        return divination_rec(oracle, m + 1, b, n + 1)
