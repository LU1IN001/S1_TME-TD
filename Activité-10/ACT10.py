# Wilhem Blondel & Beeverly Gourdette
import random
import sys
sys.path.append('C:/Users/wilhe/OneDrive/Documents/Bureau/Sorbonne Workspace/MrPython/mrpython/studentlib/gfx')
import image

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

def case_vides(pla: PlateauT) -> List[Tuple[int, int]]:
    """Renvoie les coordonnées des cases vides du plateau"""
    return [(i, j) for i in range(3) for j in range(3) if videt(pla, i, j)]

assert case_vides([["X", " ", "O"], ["O", "X", " "], ["X", " ", " "]]) == [(0,1), (1,2), (2,1), (2,2)]
assert case_vides([["O", "X", "O"], ["X", "O", "X"], ["O", "X", "O"]]) == []

def pick_random_num(mn: int, mx: int) -> int:
    """Préconditoons mn <= mx
    Retourne un nombre compris entre le mn et mx inclus de manière aléatoire"""
    return round((mx-mn)*random.random())+mn

assert 4 <= pick_random_num(4, 8) <= 8
assert 0 <= pick_random_num(0, 2) <= 2
assert 50 <= pick_random_num(50, 89) <= 89

def tourt(pla: PlateauT, i: int, j: int) -> None:
    """***Procédure***
    Préconditions,  et j respecte la taille du plateau pla
    Fait joue l'ordinateur sur le plateau pla en supposant que le joueur à joué en i,j"""
    if not videt(pla, i, j):
        print(dessine_plateaut(pla) + "\nImpossible de jouer ici")
        return None
    jouex(pla, i, j)
    if gagnet(pla, "X"):
        print(dessine_plateaut(pla), "\n*** GAGNE ***")
        return None
    elif pleint(pla):
        print(dessine_plateaut(pla), '\n*** EGALITE ***')
        return None
    vides: List[Tuple[int, int]] = case_vides(pla)
    x, y = vides[pick_random_num(0, len(vides)-1)]
    joueo(pla, x, y)
    if gagnet(pla, "X"):
        print(dessine_plateaut(pla), '\n*** GAGNE ***')
        return None
    elif pleint(pla):
        print(dessine_plateaut(pla), '\n*** EGALITE ***')
        return None
    else:
        print(dessine_plateaut(pla), "\n L'ordinateur a joué en (", x, ",", y ,")")

plat_essai: PlateauT = plateaut_vide()

def dessinex(x: float, y: float, t: float) -> Image:
    """Dessine une croix au coordonnée x, y le centre de la croix dans un carré de côté t"""
    # param 1 -> inférieur gauche vers supérieur droit
    # param 2 -> inférieur droit vers supérieur gauche
    return overlay(draw_line(x-t/2, y-t/2, x+t/2, y+t/2), draw_line(x+t/2, y-t/2, x-t/2, y+t/2))

def dessineo(x: float, y: float, r: float) -> Image:
    """Dessine un cercle au cordonnée x,y le centre dans un carré de côté r"""
    return draw_ellipse(x-r/2, y+r/2, x+r/2, y-r/2)

#show_image(dessinex(0, 0, 0.5)
#show_image(dessineo(0, 0, 0.5))

def dessine_pla_vide(size: float, division: int) -> Image:
    """Préconditions 0 <= size <= 2.0 and division > 0
    Va dessiner le quadrillage du plateau au centre de la fenêtre
    Le quadriage sera divisé en un nombre de division donné
    La taille du carré du quadrillge est défini par size

    Pour une taille de 1.5 et une division de 3 nous avons les valeurs suivantes
    La position réelle représente le centre de la case

    pla[x][y] | Position réelle
    0,0       | -0.5, -0.5
    0,1       | -0.5, 0
    0,2       | -0.5, 0.5
    1,0       | 0, -0.5
    1,1       | 0, 0
    1,2       | 0, 0.5
    2,0       | 0.5, -0.5
    2,1       | 0.5, 0
    2,2       | 0.5, 0.5
    
    """

    res: Image = draw_line(10, 10, 10, 10) # Initialistation en dehors du cadre
    i: int
    for i in range(division+1):
        margin: float = (2-size)/2
        nxt: float = i*size/division #Ajoute l'espacement en plus à chaque génération
        init: float = -1+margin # Position du point initial
        final: float = 1-margin # Position du point final
        # Génération de la verticale (Depuis la plus à gauche)
        res = overlay(res, draw_line(init+nxt, init, init+nxt, final))
        # Génération de l'horizontale (Depuis la plus en bas)
        res = overlay(res, draw_line(init, init+nxt, final, init+nxt))
    return res

#show_image(dessine_pla_vide(1, 3))
#show_image(dessine_pla_vide(0.5, 2))
#show_image(dessine_pla_vide(1.5, 15))
#show_image(dessine_pla_vide(1.85,8))

def dessine_pla(pla: PlateauT, size: float, margin: float) -> Image:
    """
    Préconditions 0 <= size <= 2 and 0 <= margin < size/3
    Affiche le plateau pla dans l'interface graphique ayant une taille size de côté
    Le plateau sera affiché au centre de la fenêtre graphique
    margin est la marge souhaitée d'un élément contenu dans une case (son espacement par rapport au bord de la case"""
    res: Image = dessine_pla_vide(size, len(pla))
    esp: float = size/3 # Taille des sous carré du quadrillage
    t: float = (esp-margin) # Taille des éléments dans la case
    i: int
    j: int
    for i in range(len(pla)-1, -1, -1):
        for j in range(len(pla)):
            if pla[i][j] == "X":
                res = overlay(res, dessinex(esp+esp*(-i), -esp+esp*j, t))
            elif pla[i][j] == "O":
                res = overlay(res, dessineo(esp+esp*(-i), -esp+esp*j, t))

    return res

show_image(dessine_pla([["X", " ", "O"], ["O", "X", " "], ["X", " ", " "]], 1.85, 0.15))
#show_image(dessine_pla([["O", "X", "O"], ["X", "O", "X"], ["O", "X", "O"]], 1.5, 0.35))
#show_image(dessine_pla([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], 1, 0.02))
#show_image(dessine_pla([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], 0.5, 0.1))
#show_image(dessine_pla([["X", " ", "O"], ["X", "O", " "], ["X", " ", " "]], 2, 0.25))
#show_image(dessine_pla([["X", " ", "O"], ["O", "X", " "], ["X", " ", " "]], 1.95, 0.7))
#show_image(dessine_pla([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]], 1.85, 0.35))
