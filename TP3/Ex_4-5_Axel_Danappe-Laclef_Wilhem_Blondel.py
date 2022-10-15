# Question 1
def nb_couples_intervalle(n: int, p: int) -> int:
    """Préconditions: n <= p
    Retourne le nombre de couple d'entiers distincts dans l'intervalle [n,p]
    """
    i: int = n
    j: int = n
    nb_couple: int = 0
    while i <= p:
        while j <= p:
            if(j != i and j >= i):
                nb_couple = nb_couple + 1
            j = j + 1
        i = i + 1
        j = n
    return nb_couple

assert nb_couples_intervalle(0, 0) == 0
assert nb_couples_intervalle(2, 4) == 3
assert nb_couples_intervalle(-1, 3) == 10

# Question 2
def nb_couples_divise(n: int, p: int) -> int:
    """Préconditions: n <= p
    Retourne le nombre de couple d'entiers distincts qui se divise dans l'intervalle [n,p]
    """
    i: int = n
    j: int = n
    nb_couple: int = 0
    while i <= p:
        while j <= p:
            if(i < j and i != 0 and j % i == 0):
                nb_couple = nb_couple + 1
            j = j + 1
        i = i + 1
        j = n
    return nb_couple

assert nb_couples_divise(4, 6) == 0
assert nb_couples_divise(2, 6) == 3
assert nb_couples_divise(-1, 1) == 2
assert nb_couples_divise(1, 10) == 17

# Question 3
def nb_couples_divise_trace(n: int, p: int) -> int:
    """Préconditions: n <= p
    Retourne le nombre de couple d'entiers distincts qui se divise dans l'intervalle [n,p]
    """
    i: int = n
    j: int = n
    nb_couple: int = 0
    while i <= p:
        while j <= p:
            if(i < j and i != 0 and j != 0 ):
                print("couple(",i,",",j,")")
                if(j % i == 0):
                    nb_couple = nb_couple + 1
                    print("------------")
                    print(i, "divise", j, "!")
                    print("------------")
            j = j + 1
        i = i + 1
        j = n
    return nb_couple

# Question 4
def existe_couples_divise(n: int, p: int) -> bool:
    """Préconditions: n <= p
    Renvoie True s'il exitse un couple d'entiers distincts dans l'intervalle [n, p] qui se divise
    """
    i: int = n
    j: int = n
    nb_couple: int = 0
    existe: bool = False
    while i <= p and not existe:
        while j <= p and not existe:
            if(i < j and i != 0 and j % i == 0):
                existe = True
            j = j + 1
        i = i + 1
        j = n
    return existe

assert existe_couples_divise(0, 0) == False
assert existe_couples_divise(2, 6) == True
assert existe_couples_divise(-1, 1) == True
assert existe_couples_divise(1, 10) == True
assert existe_couples_divise(21, 34) == False

# Question 5
def existe_couples_divise_variante(n: int, p: int) -> bool:
    """Préconditions: n <= p
    Renvoie True s'il exitse un couple d'entiers distincts dans l'intervalle [n, p] qui se divise
    """
    i: int = n
    j: int = n
    nb_couple: int = 0
    while i <= p:
        while j <= p:
            if(i < j and i != 0 and j % i == 0):
                return True
            j = j + 1
        i = i + 1
        j = n
    return False

assert existe_couples_divise_variante(0, 0) == False
assert existe_couples_divise_variante(2, 6) == True
assert existe_couples_divise_variante(-1, 1) == True
assert existe_couples_divise_variante(1, 10) == True
assert existe_couples_divise_variante(21, 34) == False
