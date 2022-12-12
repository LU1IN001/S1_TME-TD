from typing import *
T = TypeVar('T')
# Exercice 10.1

# 1
# Renvoie une liste de Tuple contenant la clé du dictionnaire et sa valeur
# Même chose que la 1
# Renvoie les valeurs du dictionnaire Dico dans une liste
# Même chose que la 3
# Renvoie uniquement les éléments qui, arrondis à l'entier supérieur, sont inféreiur à 5

# 2
# Renvoie { ' ', 'c', 'a', 'b' }
# Renvoie { 'c', 'a', 'b' }
# -
# -
# -
# Renvoie { 'cuicuis', 'miaous' }
# -
# Renvoie { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }

# 3
# -
# Renvoie le dictionnaire avec les clés et les valeurs inversés, seul la dernière valeur de tout sera retenue
# -
# -
# -
# { 4:31, 6:17, 7:31, 8:42 }
# { 9:31, 9:17, 9:31, 9:42 }

# Exercice 10.2

LivresBD = Dict[str,Tuple[str,int]]
bd: LivresBD = {'Les misérables':('Victor Hugo', 5),
'Le dernier des Mohicans':('James F. Cooper', 0),
'Un animal doué de raison': ('Robert Merle', 6),
'Le grand Meaulnes':('Alain Fournier', 1),
'Notre-dame de Paris':('Victor Hugo', 4),
'Les comtemplations':('Victor Hugo', 0) }


def auteurs(bd: LivresBD) -> Set[str]:
    return { a for a, _ in bd.values() }


def titres_empruntables(bd: LivresBD) -> Set[str]:
    return { b for (b, (_, l)) in bd.items() if l != 0 }

def titres_auteurs(livres: LivresBD, auteur: str) -> Set[str]:
    return { b for (b, (a, _)) in bd.items() if a == auteur}


# Exercice 10.4

def melements_list(l: List[T]) -> Set[T]:
    return { e for e in l }

def melements_dict(d: Dict[T, int]) -> Set[T]:
    return { c for c in d}

def mdict_de_mlist(l: List[T]) -> Dict[T, int]:
    dico: Dict[T, int] = dict()
    e: T
    for e in l:
        if e not in dico:
            dico[e] = 0
        dico[e]= dico[e] + 1
    return dico

def minter_dict(m1: Dict[T, int], m2: Dict[T, int]) -> Dict[T, int]:
    return {k:min(v, m2[k]) for k, v in m1.items() if k in m2}

    



