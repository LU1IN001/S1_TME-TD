# Question 1
def reste(a: int, b:int) -> int:
    """
    Préconditions: a >= 0 et b > 0
    retourne le reste de la division euclidienne de a par b
    """
    reste: int = a
    while(reste - b >= 0):
        reste = reste - b
    return reste

assert reste(11,4) == 3
assert reste(21,7) == 0
assert reste(0,3) == 0

# Question 2

def est_divisible(a: int, b: int) -> bool:
    """
    Préconditions: a >= 0 et b > 0
    indique si a est divisible par b
    """
    return reste(a, b) == 0

assert est_divisible(0,3) == True
assert est_divisible(11,4) == False
assert est_divisible(21,7) == True

def ppcm(a: int, b: int) -> int:
    """
    Préconditions: a >= 0 et b > 0
    retourne le plus petit commun multiple entre a et b
    """
    i: int = b
    while not(est_divisible(i, a) and (est_divisible(i, b))):
        i = i+1
    return i

assert ppcm(2,3) == 6
assert ppcm(6,8) == 24
assert ppcm(12,15) == 60
