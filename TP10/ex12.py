from typing import List
Matrice = List[List[int]]

def tourner_sous_matrice(m: Matrice, x: int, y: int, k: int) -> None:
    values: List[int] = [m[x][i] for i in range(y, k//2+y)] # Valeurs à déplacer au prochain tours de boucle
    temp: int # Variable temporaire de stockage
    cst: int = k//2
    colonne: int = y + k//2
    ligne: int = x
    i: int
    for i in range(1, k+1):
        if i%3 == 0 and i!=0:
            # Tous les cycles sont terminés, on passe à la ligne suivante
            ligne = ligne + 1
            values = [m[ligne][n] for n in range(y, k//2+y)]
        if i%2 == 0:
            # Le cycle part à gauche
            cst = - k//2
        elif i%2 != 0:
            # Retour du cycle vers la droite
            cst = k//2

        j: int
        for j in range(len(values)):
            # Gestion des valeurs sur la même ligne
            temp: int = m[ligne][colonne+j]
            m[ligne][colonne+j] = values[j]
            values[j] = temp
        ligne = ligne + cst
        for j in range(len(values)):
            # Gestion des valeurs sur la même colonne
            temp: int = m[ligne][colonne+j]
            m[ligne][colonne+j] = values[j]
            values[j] = temp
        colonne = colonne - cst

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