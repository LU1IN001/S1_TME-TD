from typing import List, Tuple, Set, Optional, Dict, Callable, TypeVar
T = TypeVar('T')

# Exercice 9.1

def diff_sym(e1: Set[T], e2: Set[T]) -> Set[T]:
    res: Set[T] = set()
    e: T
    for e in e1:
        if not (e in e2):
            res.add(e)
    for e in e2:
        if not (e in e1):
            res.add(e)
    return res

def diff_sym_operand(e1: Set[T], e2: Set[T]) -> Set[T]:
    return (e1 - e2) | (e2 - e1)

# Exercice 9.2

def repetes(l: List[T]) -> Set[T]:
    res: Set[T] = set()
    i: int
    for i in range(1, len(l)):
        e: T = l[i-1]
        if e in l[i:]:
            res.add(e)
    return res


# Exercice 9.4

def est_lettre(c : str) -> bool:
    """Précondition : len(c) == 1 (caractère)
    Retourne True si le caractère c est une lettre, ou False sinon.
    """
    return ((c >= 'a') and (c <= 'z')) \
    or ((c >= 'A') and (c <= 'Z')) \
    or (c in {'é', 'è', 'à', 'ù', 'œ'})

# Jeu de tests
assert est_lettre('a') == True
assert est_lettre('Z') == True
assert est_lettre(',') == False
assert est_lettre('1') == False

def frequences_lettres(text: str) -> Dict[str, int]:
    dic: Dict[str, int] = dict()
    e: str
    for e in text:
        if est_lettre(e):
            if e in dic:
                dic[e] = dic[e] + 1
            else:
                dic[e] = 1
            # Ou
            # if not e in dic:
            #   dic[e] = 0
            # dic[e] = dic[e] + 1
    return dic

def lettre_freq_max(d: Dict[str, int]) -> str:
    """Préconditions: len(d) > 0"""
    max_value: int = 0
    max_key: str = ''
    k: str
    v: int
    for k, v in d.items():
        if max_value < v:
            max_value = v
            max_key = k
    return max_key

def lettres_freq_inf(d: Dict[str, int], f: int) -> Set[str]:
    """Préconditions f >= 0"""
    res: Set[str] = set()
    k: str
    v: int
    for k, v in d.items():
        if v <= f:
            res.add(k)
    return res

# CC1 Exercice 2

def inverse_char(c: str) -> str:
    if c == '0':
        return '1'
    else:
        return '0'

def nb_un(s: str) -> int:
    res: int = 0
    e: str
    for e in s:
        if e == '1':
            res = res + 1
    return res

def invc_avant_dernier_un(s: str) -> str:
    if len(s) <= 1:
        return s
    if s[-1] == '1':
        return s[:-2] + inverse_char(s[-2]) + '1'
    else: 
        return s

        

