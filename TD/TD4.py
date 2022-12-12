from typing import Optional
# Exercice 5.1

# Question 1

def somme_carre(n: int) -> int:
    """Préconditions n >= 0"""
    res: int = 0
    i: int
    for i in range(n+1):
        res = res + i**2
    return res


# Question 2

def f(n: int, m: int) -> int:
    """Préconditions n >= 0 and m < n
    Retourne le produit des cubes de m à n"""
    p: int = 1
    k: int = 3
    while k < n:
        p = p * k * k * k
        k = k + 1
    return p

"""
| Boucle | k | p         |
| Entrée | 4 | 1         |
| Tour 1 | 5 | 64        |
| Tour 2 | 6 | 8000      |
| Tour 3 | 7 | 1728000   |
| Sortie | 8 | 592764000 |
"""

# Exercice 5.2

def nb_chiffre(a):
    """Compte le nombre de chiffre dans le str"""
    b: int = 0
    c: str
    for c in a:
        if c >= '0' and c <= '9':
            b = b + 1
    return b

# Question 2

"""
| Boucle | b | c   |
| Entrée | 0 | ?   |
| Tour 1 | 0 | 'u' |
| Tour 2 | 0 | 'n' | 
| Tour 3 | 0 | ':' | 
| Sortie | 1 | '1' | 

"""

# Exercice 5.9

def moins_lettre(c: str, a: str) -> Optional[str]:
    """Précondition: len(a) == 1"""
    res: str = ""
    has_occured: bool = False
    char: str
    for char in c:
        if (char != a or has_occured):
            res = res + char
        else:
            has_occured = True
    if has_occured:
        return res
    else:
        return None

def anagramme(m1: str, m2: str) -> bool:
    """Indique si m1 et m2 sont anagrammes"""
    if(len(m1) != len(m2)):
         return False
    char: str
    m3: Optional[str] = m1
    for char in m2:
            m3 = moins_lettre(m3, char)
            if(m3==None):
                return False
    if(m3==""):
        return True
    else:
        return False

    
