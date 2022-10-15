def fermat(n: int) -> int:
    """
    Préconditions n>=0
    retourne le terme n de la suite de fermat
    """
    return (2**(2**n))+1


assert fermat(0) == 3
assert fermat(1) == 5
assert fermat(2) == 17
assert fermat(5) == 4294967297

# On peut utiliser l'expression fermat(5) % 641 != 0 pour voir si F5 divisible par 641
