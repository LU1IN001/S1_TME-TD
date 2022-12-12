# ----- Exercice 2.2 -----
# Question 1
def mention(note: float) -> str:
    """
    Precondition: note <= 20 && note >= 0
    retourne la mention associée à la note
    """
    if note < 10:
        return 'Eliminé'
    elif note < 12:
        return 'Passable'
    elif note < 14:
        return 'AB'
    elif note < 16:
        return 'B'
    else:
        return 'TB'


assert mention(0) == 'Eliminé'
assert mention(8) == 'Eliminé'
assert mention(10) == 'Passable'
assert mention(12.5) == 'AB'
assert mention(15) == 'B'
assert mention(20) == 'TB'


# Question 2

def mention2(note: float) -> str:
    """
    Precondition: note <= 20 && note >= 0
    retourne la mention associée à la note
    """
    if note < 12:
        if note < 10:
            return 'Eliminé'
        else:
            return 'Passable'
    elif note < 14:
        return 'AB'
    elif note < 16:
        return 'B'
    else:
        return 'TB'


assert mention2(0) == 'Eliminé'
assert mention2(8) == 'Eliminé'
assert mention2(10) == 'Passable'
assert mention2(12.5) == 'AB'
assert mention2(15) == 'B'
assert mention2(20) == 'TB'


# ------ Exercice 2.3 ------
# Question 1

def f(n1: float, n2: float, n3: float) -> str:
    """Précondition : n1 != n2 and n2 != n3 and n3 != n1
    retourne un cas parmi 6 selon les valeurs de n1, n2 et n3.
    """
    if n1 < n2 and n2 < n3:
        return 'cas 1'
    elif n1 < n3 and n3 < n2:
        return 'cas 2'
    elif n2 < n1 and n1 < n3:
        return 'cas 3'
    elif n2 < n3 and n3 < n1:
        return 'cas 4'
    elif n3 < n1 and n1 < n2:
        return 'cas 5'
    else:
        return 'cas 6'


assert f(1, 2, 3) == 'cas 1'
assert f(1.3, 3.2, 2.6) == 'cas 2'
assert f(2, 1, 3) == 'cas 3'
assert f(3, 1, 2) == 'cas 4'
assert f(2, 3, 1) == 'cas 5'
assert f(3, 2, 1) == 'cas 6'


# Question 2

def f2(n1: float, n2: float, n3: float) -> str:
    """Précondition : n1 != n2 and n2 != n3 and n3 != n1
    retourne un cas parmi 6 selon les valeurs de n1, n2 et n3.
    """
    if n1 < n2 < n3:
        return 'cas 1'
    elif n1 < n3 < n2:
        return 'cas 2'
    elif n2 < n1 < n3:
        return 'cas 3'
    elif n2 < n3 < n1:
        return 'cas 4'
    elif n3 < n1 < n2:
        return 'cas 5'
    else:
        return 'cas 6'


assert f2(1, 2, 3) == 'cas 1'
assert f2(1, 3, 2) == 'cas 2'
assert f2(2, 1, 3) == 'cas 3'
assert f2(3, 1, 2) == 'cas 4'
assert f2(2, 3, 1) == 'cas 5'
assert f2(3, 2, 1) == 'cas 6'


# ----- Exercice 2.4 -----

# Question 1

def egal_eps(x1: float, x2: float, epsilon: float) -> bool:
    """
    Précondition: epsilon > 0
    retourne si x1 == x2 à epsilon près
    """
    return abs(x1 - x2) <= epsilon


assert egal_eps(0.1, 0.15, 0.1) == True
assert egal_eps(0.1, 0.12, 0.01) == False
assert egal_eps(0.1, 0.101, 0.01) == True
assert egal_eps(0.1, 0.102, 0.02) == True
assert egal_eps(0.1, 0.102, 0.001) == False
assert egal_eps(0.1, 0.10001, 0.001) == True


# Question 2

def fiabilite(v1: float, v2: float, v3: float, epsilon: float) -> float:
    """
    Précondition: epsilon > 0
    retourne la fiabilité de v1 = v2 = v3
    """
    coef: int = 0
    if abs(v1 - v2) <= epsilon:
        coef += 1
    if abs(v2 - v3) <= epsilon:
        coef += 1
    if abs(v3 - v1) <= epsilon:
        coef += 1
    return coef / 3


assert fiabilite(0.5, 0.501, 0.52, 0.2) == 1.0
assert fiabilite(0.5, 0.501, 0.52, 0.01) == 1 / 3


# ----- Exercice 2.6 -----

def ou(p: bool, q: bool) -> bool:
    if p:
        return True
    else:
        return q


def et(p: bool, q: bool) -> bool:
    if p:
        return q
    else:
        return False


# ----- Exercice 3.3 -----

def divise(n: int, p: int) -> bool:
    """
    Précondition n > 0 et p >= 0
    retourne si n et p se divise entre eux
    """
    return p % n == 0


def est_premier(n: int) -> bool:
    """
    Précondition n > 0
    retourne si n et p se divise entre eux
    """
    if n == 0 or n == 1:
        return False
    i: int = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


assert est_premier(0) == False
assert est_premier(1) == False
assert est_premier(2) == True
assert est_premier(17) == True
assert est_premier(357) == False
