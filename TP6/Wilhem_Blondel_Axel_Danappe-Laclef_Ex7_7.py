def intersection_2_listes(l1: List[int], l2: List[int]) -> List[int]:
    """Précondition: les listes sont ordonnées dans l'ordre croissant
    Retourne l'intersection entre deux listes"""

    larger_list: List[int] = l1
    smaller_list: List[int] = l2
    if(len(l2) > len(l1)):
       larger_list = l2
       smaller_list = l1
       
    i: int = 0 # i est le pointeur de la plus petite liste
    j: int = 0 # j est le pointeur de la plus grande liste
    tested_value: int
    res: List[int] = []

    while i < len(smaller_list) and j < len(larger_list):
        
        tested_value = smaller_list[i]
        if larger_list[j] == smaller_list[i]:
            # Valeur trouvée, incrémentation des pointeurs
            res.append(larger_list[j])
            i = i + 1
            j = j + 1
        elif(larger_list[j] < smaller_list[i]):
            # Valeur toujours non trouvée. Décalage du pointeur j
            j = j + 1
        else:
            # Les valeurs de la grande liste sont plus grandes que celle de la petite
            # On décale i
            i = i + 1
            
    return res
        
            
            
assert intersection_2_listes([0,1,2], [3,4,5]) == []
assert intersection_2_listes([1,2,3],[1,2,3]) == [1, 2, 3]
assert intersection_2_listes([1,1],[1,1]) == [1, 1]
assert intersection_2_listes([1,1],[1,2]) == [1]
assert intersection_2_listes([],[1,2,3]) == []
assert intersection_2_listes([1,2,2,3,4],[2,3,4,4,5,6]) == [2, 3, 4]


def intersection(l: List[List[int]]) -> List[int]:
    """Précondition: les listes sont ordonnées dans l'ordre croissant
    Retourne l'intersection entre plusieurs listes"""
    res: List[int] = l[0]
    i: int
    for i in range(1, len(l)):
        res = intersection_2_listes(res, l[i])
    return res
    
assert intersection([[1, 2, 3, 4, 4, 5], [2, 5, 7], [0, 2, 2, 4, 4, 5, 9]]) == [2, 5]
assert intersection([[1, 2, 3, 4, 4, 5], [2, 4, 4, 5, 7], [0, 2, 2, 4, 4, 5, 9]]) == [2, 4, 4, 5]
