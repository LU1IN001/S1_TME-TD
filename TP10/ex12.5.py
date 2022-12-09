from typing import List

def partitionner(l: List[int]) -> int:
    """Préconditions: les éléments de la liste 
    sont des entiers positif strictement inférieur à len(l)

    ***Procédure***
    
    Retourne la liste l partitionner en fonction de son
    pivot, élément d'indice 0"""
    gauche: int = 0 # Décalage par rapport à l'index du pivot
    droite: int = 0 # Décalage par rapport à l'index 0
    temp: int = 0
    pivot: int = l[0]
    for _ in range(len(l)-1):
        if l[0] >= pivot:
            # On déplace l'élément à gauche du pivot
            temp = l[pivot+gauche]
            l[pivot+gauche] = l[0]
            l[0] = temp # On va réévaluer l'élément 0 qui était à la place de l'élément précédent
            gauche = gauche+1
        else:
            temp = l[droite]
            l[droite] = l[0]
            l[0] = temp
            droite=droite+1

    return l[0]


l1: List[int] = [2, 1, 4, 0, 3]
partitionner(l1)

def partitionner_sl(l: List[int], i: int, j: int) -> int:
    """Préconditions: 0 <= i < j <= len(l)
    ***Procédure***
    Effectue la fonction partitionner sur une sous liste
    de l"""
    # On a dû tout réécrire pour éviter la copie de liste
    
    gauche: int = 0 # Décalage par rapport à l'index du pivot
    droite: int = 0 # Décalage par rapport à l'index 0
    temp: int = 0
    pivot: int = l[i]+i
    value: int = l[i]
    for _ in range(j-i-1):
        if l[i] >= value:
            # On déplace l'élément à gauche du pivot
            temp = l[pivot+gauche]
            l[pivot+gauche] = l[i]
            l[i] = temp # On va réévaluer l'élément 0 qui était à la place de l'élément précédent
            gauche = gauche+1
        else:
            temp = l[droite]
            l[droite] = l[i]
            l[i] = temp
            droite=droite+1

    return pivot

l2 : List[int] = [8, 5, 2, 1, 3, 0, 4, 6, 7]
partitionner_sl(l2, 2, 7)
print(l2)

l3 : List[int] = [2, 1, 3, 0, 4]
partitionner_sl(l3, 0, 5)
print(l3)


"""def trier_rapide_sl(l: List[int], i: int, j: int) -> None:
    ***Procédure***
    Précondition : 0 <= i <= j < len(l)
    Trie la sous-liste de l allant de i (inclus) à j (exclu)
    
    ip : int # indice du pivot
    if i != j:
        ip = partitionner_sl(l, i, j)
        trier_rapide_sl(l, i, ip)
        trier_rapide_sl(l, ip + 1, j)

# ????
# Comment savoir si le pivot est un indice ????
def trier_rapide(l: List[int]) -> None:
    trier_rapide_sl(l, 0, len(l))


l1 : List[int]= [3, 1, 0, 4, 2, 5]
trier_rapide(l1)
print(l1)"""