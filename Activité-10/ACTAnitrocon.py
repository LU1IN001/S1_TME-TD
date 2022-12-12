#Question 1
from typing import List
CaseT = str 
PlateauT = List[List[CaseT]]

def plateau_vide()->PlateauT:
    """Renvoie un plateau de jeu vide pour le tic-tac-toe"""
    return [[" " for _ in range(3)]for _ in range(3)]
    
    
pla1 : PlateauT = plateau_vide()
assert pla1 [1][1] == " "
assert pla1 [0][2] == " "

#Question 2

def videt (p:PlateauT, i:int, j:int)->bool:
    """Précondition : 0 <= i <= 2 and 0 <= j <= 2
    Décide si la case de cordonnées (i,j) du plateau est vide"""

    return p[i][j]== " "

assert videt (pla1 , 1, 1) == True
assert videt (pla1 , 0, 2) == True

#Question 3

def jouex (pla:PlateauT, i:int, j:int)->None:
    """***Procédure***"""
    pla[i][j]= 'X'


def joueo (pla:PlateauT, i:int, j:int)->None:
    """***Procédure***"""
    pla[i][j]= 'O'

assert videt (pla1 , 0, 2) == True
assert jouex (pla1 , 1, 1) == None
assert joueo (pla1 , 0, 2) == None
assert videt (pla1 , 0, 2) == False

#Question 4
def dessine_plateaut(pla:PlateauT)->str:
    """ """

    i:int
    j:int
    res:str=''

    for i in range (len(pla)-1, -1, -1):
        for j in range (len(pla)):
            res=res+pla[j][i]
        res = res + "\n"
    return res

def gagnet(pla : PlateauT, s : str) -> bool:

    '''Préconditions : s == "X" ou s == "O"
    Retourne si s a gagné'''
    
    i : int
    for i in range(3):
        if (pla[i][0] == s and pla[i][1] == s and pla[i][2] == s) or (pla[0][i] == s and pla[1][i] == s and pla[2][i] == s):
            return True
        
    return (pla[0][0] == s and pla[1][1] == s and pla[2][2] == s) or (pla[0][2] == s and pla[1][1] == s and pla[2][0] == s)

#Jeu de tests

assert gagnet([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], "X")
assert not gagnet([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], "O")
assert gagnet([["X", " ", "O"], ["X", "O", " "], ["X", " ", " "]], "X")
assert not gagnet([["X", " ", "O"], ["O", "X", " "], ["X", " ", " "]], "X")
assert gagnet([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]], "O")


def pleint(pla : PlateauT) -> bool:
    '''Vérifie si le pateau est plein'''    
    i : int
    j : int
    for i in range(3):
        for j in range(3):
            if videt(pla, i, j):
                return False
            
    return True

# Jeu de tests

assert not pleint([["X", " ", "O"], ["O", "X", " "], ["X", " ", " "]])
assert pleint([["O", "X", "O"], ["X", "O", "X"], ["O", "X", "O"]])
                 
