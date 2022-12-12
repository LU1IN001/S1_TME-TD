# Wilhem Blondel & Beeverly Gourdette

CaseT = str
PlateauT = List[List[CaseT]]

def plateaut_vide() -> PlateauT:
    """Retourne un plateau de TicTacToe vide"""
    return [[" " for _ in range (3)] for _ in range(3)]

pla1 : PlateauT = plateaut_vide()
assert plateaut_vide() == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
assert pla1[1][1] == " "
assert pla1[0][2] == " "

def videt(pla: PlateauT, i: int, j: int) -> bool:
    '''Préconditions: 0 <= i <= 2 et i  et 0 <= j <= 2
    Retourne si la case du plateau est vide'''
    return pla[i][j] == ' '

assert videt(pla1 , 1, 1) == True
assert videt(pla1 , 0, 2) == True

def jouex(pla: PlateauT, i: int, j: int)-> None:
    '''***Procédure***
    Préconditions: 0 <= i <= 2 et i  et 0 <= j <= 2
    Ajoute un X à la case souhaitée'''
    pla[i][j] = 'X'

def joueo(pla: PlateauT, i: int, j: int)-> None:
    '''***Procédure***
    Préconditions: 0 <= i <= 2 et i  et 0 <= j <= 2
    Ajoute un O à la case souhaitée'''
    pla[i][j] = 'O' 

assert videt(pla1 , 0, 2) == True
assert jouex(pla1 , 1, 1) == None
assert joueo(pla1 , 0, 2) == None
assert videt(pla1 , 0, 2) == False


def dessine_plateaut(pla:PlateauT)-> str:
    """Dessine le plateau de TicTacToe"""
    res: str = "/---\\\n"
    i: int
    j: int
    for i in range(len(pla)-1, -1, -1):
        res = res + "|"
        for j in range(len(pla)):            
            case: CaseT = pla[j][i]
            res = res + case
        res = res + "|\n"
    return res + "\---/"

assert dessine_plateaut(pla1) == '/---\\\n|O  |\n| X |\n|   |\n\\---/'

def gagnet(pla: PlateauT,s: str) -> bool:
    """Préconditions s == "X" or s == "O"
    Indique si la partie est gagné par s"""
    
