from typing import List
Matrice = List[List[int]]

def tourner_sous_matrice(m: Matrice, x: int, y: int, k: int) -> None:
    """***Procédure***
    Prcéondition: k est une puissance de 2, x/y/x+k/y+k sont contenu dans m
    Fait tourner à 90° par cadrans la sous matrice de coordonnées supérieures gauche x y et de taille k*k"""
    values: List[int] = [m[x][i] for i in range(y, k//2+y)] # Valeurs à déplacer au prochain tours de boucle
    temp: int               # temp: Variable temporaire de stockage à placer dans values après assignation
    cst: int = k//2         # cst: Constante qui oriente le sens des cycles
    colonne: int = y + k//2 # colonne: Colonne à évaluer. On commence à évaluer la première colonne de la matrice suivante
                            #          Ceci est cohérent avec notre initialisation des valeurs à remplacer au départ
    ligne: int = x
    i: int
    for i in range(1, k+1):
        if i%3 == 0:
            # Tous les cycles sont terminés, on passe à la ligne suivante
            ligne = ligne + 1
            values = [m[ligne][n] for n in range(y, k//2+y)] # Regénération des valeurs (qui vont être sautées)
        if i%2 == 0:
            # Le cycle part à gauche puis ira vers le haut
            cst = - k//2
        else:
            # Retour du cycle vers la droite, il ira ensuite vers le bas
            cst = k//2

        j: int
        for j in range(len(values)):
            # Gestion des valeurs sur la même ligne
            temp = m[ligne][colonne+j]
            m[ligne][colonne+j] = values[j]
            values[j] = temp
        ligne = ligne + cst # Passage à la ligne suivante (vers bas puis haut)
        o: int
        for o in range(len(values)):
            # Gestion des valeurs sur la même colonne
            temp = m[ligne][colonne+o]
            m[ligne][colonne+o] = values[o]
            values[o] = temp
        colonne = colonne - cst # Passage à la colonne suivante (vers la gauche puis droite)

m0: Matrice = [[0, 0, 0, 0],
               [0, 1, 2, 0],
               [0, 3, 4, 0],
               [0, 0, 0, 0]]

m1 : Matrice = [[ 1, 2, 3, 4, 0, 0, 0, 0],
                [ 5, 6, 7, 8, 0, 0, 0, 0],
                [ 9, 10, 11, 12, 0, 0, 0, 0],
                [13, 14, 15, 16, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 0]]

assert tourner_sous_matrice(m0, 1, 1, 2) == None
assert m0 == [[0, 0, 0, 0], [0, 3, 1, 0], [0, 4, 2, 0], [0, 0, 0, 0]]  
assert tourner_sous_matrice(m1, 0, 0, 4) == None
assert m1 == [[9, 10, 1, 2, 0, 0, 0, 0], [13, 14, 5, 6, 0, 0, 0, 0], [11, 12, 3, 4, 0, 0, 0, 0], [15, 16, 7, 8, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]


def tourner_matrice(m: Matrice, k: int) -> None:
    """***Procédure***
    Fait tourner la matrice m en fonction d'une sous matrice de taille k
    Tourner à 90° par quadrant"""
    nb_iter: int = (len(m)//k)**2 # Calcul le nombre d'itération
                                          # L'élévation au carré permet de prendre en compte l'intégralité de la matrice
    
    x: int = 0
    y: int = 0
    i: int
    for i in range(1, nb_iter+2):
        tourner_sous_matrice(m, x, y, k)
        if i%(len(m)//k) != 0:
            x = x + k
        else:
            x = 0
            y = y + k

m2 : Matrice = [[0,0,0,0],
                [0,1,2,0],
                [0,3,4,0],
                [0,0,0,0]]

m3 : Matrice = [[0,0,0,0],
                [0,1,2,0],
                [0,3,4,0],
                [0,0,0,0]]

m4 : Matrice = [[0,0,0,0],
                [0,1,2,0],
                [0,3,4,0],
                [0,0,0,0]]

assert tourner_matrice(m2, 2) == None
assert m2 == [[0, 0, 2, 0], [1, 0, 0, 0], [0, 0, 0, 4], [0, 3, 0, 0]]
assert tourner_matrice(m3, 1) == None
assert m3 == [[0, 0, 0, 0], [0, 1, 2, 0], [0, 3, 4, 0], [0, 0, 0, 0]]
assert tourner_matrice(m4, 4) == None
assert m4 == [[0, 3, 0, 0], [0, 0, 0, 1], [4, 0, 0, 0], [0, 0, 2, 0]]

def tourner(m: Matrice) -> None:
    i: int = 2
    while i <= len(m):
            print(i)
            tourner_matrice(m, i)
            i = i*2

m5: Matrice = [[1, 2],
               [3, 4]]

m6: Matrice = [[l for l in range(2 ** 3 * k, 2 ** 3 * (k + 1))]
                for k in range(2 ** 3)]

assert m6 == [[0, 1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30, 31], [32, 33, 34, 35, 36, 37, 38, 39], [40, 41, 42, 43, 44, 45, 46, 47], [48, 49, 50, 51, 52, 53, 54, 55], [56, 57, 58, 59, 60, 61, 62, 63]]

assert tourner(m5) == None
assert m5 == [[3, 1], [4, 2]]

assert tourner(m6) == None
print(m6)
assert m6 == [[56, 48, 40, 32, 24, 16, 8, 0], [57, 49, 41, 33, 25, 17, 9, 1], [58, 50, 42, 34, 26, 18, 10, 2], [59, 51, 43, 35, 27, 19, 11, 3], [60, 52, 44, 36, 28, 20, 12, 4], [61, 53, 45, 37, 29, 21, 13, 5], [62, 54, 46, 38, 30, 22, 14, 6], [63, 55, 47, 39, 31, 23, 15, 7]]