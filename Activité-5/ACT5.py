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

# Suggestion 2

def multiplication_polynome(p1: Polyn, coef: int) -> Polyn:
    """Retourne le polynôme multiplié par l'entier donné"""
    pres: Polyn = p1[:]
    i: int
    for i in range(len(pres)):
        pres[i] = pres[i]*coef
    return pres

assert normalise(multiplication_polynome(ex1, 2)) == [6, 0, 4]
assert normalise(multiplication_polynome(ex4, 10)) == []
assert normalise(multiplication_polynome(ex3, -1)) == [-27]


def puissance_polyn(p1: Polyn, power: int) -> Polyn:
    """Préconditions: power >= 0
    Retourne le polynôme élevé à la puissance donnée"""
    if(power == 0):
        return [1]
    pres: Polyn = p1[:]
    i: int
    for i in range(1, power):
        pres = normalise(produit(pres, p1))
    return pres

assert normalise(puissance_polyn(ex1, 2)) == normalise(produit(ex1, ex1))
assert normalise(puissance_polyn(ex4, 0)) == [1]
assert normalise(puissance_polyn(ex4, 6)) == []
assert normalise(puissance_polyn(ex3, 5)) == [27**5]

def derivee(p1: Polyn) -> Polyn:
    """Retourne la dérivation du polynôme"""
    pres: Polyn = []
    x_power = 1
    i: int
    for i in p1[1:]:
        pres.append(x_power*i)
        x_power = x_power + 1
    return pres

assert normalise(derivee(ex1)) == [0, 4]
assert normalise(derivee(ex4)) == []
assert normalise(derivee(ex2)) == [-1, 2, -3]

def primitive(p1: Polyn, k: int = 0) -> Polyn:
    """Préconditions, les coefficients doivent se diviser avec les puissances supérieures
    Retourne la primitive du polynôme donné avec une constante au choix k
    Par défaut k = 0"""
    pres: Polyn = [k]
    x_power = 1
    i: int
    for i in p1:
        pres.append(i//x_power)
        x_power = x_power + 1
    return pres

assert normalise(primitive(derivee(ex1), 3)) == normalise(ex1)
assert normalise(primitive(derivee(ex2), 1)) == normalise(ex2)
assert normalise(primitive(derivee(ex3), 27)) == normalise(ex3)
assert normalise(primitive(derivee(ex4), 12)) ==  [12]

def remplace_x(p1: Polyn, x: float) -> float:
    """Retourne le résultat du polynôme de x"""
    i: int
    res: float = 0.0
    for i in range(len(p1)):
        res = res + p1[i]*x**i
    return res

assert remplace_x(ex1, 1) == 5.0
assert remplace_x(ex2, 1) == 0.0
assert remplace_x(ex3, 0) == 27.0
assert remplace_x(ex3, 500) == 27.0
assert remplace_x(ex4, 80000) == 0.0


def integration(p1: Polyn, a: float, b: float) -> float:
    """Retoune l'intégration de p1 de a à b"""
    primitive_p: Polyn = primitive(p1)
    return remplace_x(primitive_p, b) - remplace_x(primitive_p, a)


