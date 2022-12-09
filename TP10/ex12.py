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
            temp: int = m[ligne][colonne+j]
            m[ligne][colonne+j] = values[j]
            values[j] = temp
        ligne = ligne + cst # Passage à la ligne suivante (vers bas puis haut)
        for j in range(len(values)):
            # Gestion des valeurs sur la même colonne
            temp: int = m[ligne][colonne+j]
            m[ligne][colonne+j] = values[j]
            values[j] = temp
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

tourner_sous_matrice(m1, 0, 0, 4)
tourner_sous_matrice(m0, 1, 1, 2)

print(m1)
print(m0)