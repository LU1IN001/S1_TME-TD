def fzip(lst1 : List[T], lst2 : List[U]) -> List[Tuple[T, U]]:
    """Retourne la liste des couples formés par les éléments de lst1
    (premier élément du couple) et les éléments de lst2 (second élément).
    """
    i: int
    res: List[Tuple[T, U]] = []
    for i in range(min(len(lst1), len(lst2))):
        res.append((lst1[i], lst2[i]))
    return res

assert fzip([1, 3, 5], [2, 4, 6]) == [(1, 2), (3, 4), (5, 6)]
assert fzip(["un", "deux", "trois"], [1, 2, 3, 4]) == [('un', 1), ('deux', 2), ('trois', 3)]

def funzip(lst : List[Tuple[T, U]]) -> Tuple[List[T], List[U]]:
    """Retourne un couple formé de la
    - la liste des premiers éléments de la liste lst,
    - la liste des seconds éléments de cette même liste
    """
    lst1: List[T] = []
    lst2: List[U] = []
    for e1, e2 in lst:
        lst1.append(e1)
        lst2.append(e2)
    return (lst1, lst2)


assert funzip([(1, 2), (3, 4), (5, 6)]) == ([1, 3, 5], [2, 4, 6])
assert funzip([("un", 1), ("deux", 2), ("trois", 3)]) == (['un', 'deux', 'trois'], [1, 2, 3])

def plus(a : int, b : int) -> int:
    """Retourne a + b"""
    return a + b

assert plus(4, 5) == 9
assert plus(7, 9) == 16
assert plus(3, 2) == 5

def inf(a : int, b : int) -> bool:
    """Indique si a < b"""
    return a < b

assert inf(5, 6) == True
assert inf(4, 4) == False
assert inf(3, 1) == False

def fzip_with(f: Callable[[T, U], V], lst1: List[T], lst2: List[U]) -> List[V]:
    """Précondtions: Les éléments que prennent en paraméètres f doivent être les mêmes que les listes données
    Retourne la liste d'éléments retounés par f par rapport aux éléments de lst1 et lst2"""
    i: int
    res: List[V] = []
    for i in range(min(len(lst1), len(lst2))):
        res.append(f(lst1[i], lst2[i]))
    return res

assert fzip_with(plus, [1, 2, 3], [9, 8, 7]) == [10, 10, 10]
assert fzip_with(inf, [1, 2, 3], [3, 2, 1, 4]) == [True, False, False]
