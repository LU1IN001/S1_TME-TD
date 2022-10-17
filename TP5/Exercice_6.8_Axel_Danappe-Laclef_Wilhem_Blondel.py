from typing import List
from typing import TypeVar

T = TypeVar('T')
#Question 1
def entrelacement(l1 : List[T], l2 : List[T]) -> List[T]:
    """Précondition : len(l1) == len(l2)
    Retourne la liste obtenue en intercalant"""
    res : List[T] = []
    i : int
    for i in range(len(l1)):
        res.append(l1[i])
        res.append(l2[i])
    return res
        
assert entrelacement([1, 2, 3] , [4, 5, 6]) == [1, 4, 2, 5, 3, 6]
assert entrelacement([2, 4, 6] , [8, 10, 12]) == [2, 8, 4, 10, 6, 12]

#Question 2
def entrelacement_general(l1 : List[T], l2 : List[T]) -> List[T]:
    """Retourne la liste obtenue en intercalant les éléments de l1 et ceux de l2"""
    res : List[T] = []
    l1_is_larger: bool = len(l1) >= len(l2)
    if(l1_is_larger):
        res = res + entrelacement(l1[:len(l2)], l2)
        res = res + l1[len(l2):]
    else:
        res = res + entrelacement(l1, l2[:len(l1)])
        res = res + l2[len(l1):]      
    return res

assert entrelacement_general([1,2,3,4,5],[6,7,8]) == [1, 6, 2, 7, 3, 8, 4, 5]
assert entrelacement_general([1,2,3],[4,5,6,7,8]) == [1, 4, 2, 5, 3, 6, 7, 8]
assert entrelacement_general([1,2,3],[4,5,6]) == [1, 4, 2, 5, 3, 6]
