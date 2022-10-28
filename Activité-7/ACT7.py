# Wilhem Blondel
import random

Coord = Tuple[int, int]
Dir = str

ori: Coord = (0, 0)
p1: Coord = (3, 3)
p2: Coord = (0, 2)

def deplace(c: Coord, d: Dir) -> Coord:
    """Deplace le point de coordonnée donné dans la direction souhaitée"""
    x, y = c
    if d == "N":
        return (x, y+1)
    elif d == "S":
        return (x, y-1)
    elif d == "E":
        return (x+1, y)
    elif d == "O":
        return (x-1, y)

assert deplace(ori , "N") == (0, 1)
assert deplace(p1 , "E") == (4, 3)
assert deplace(deplace(p2 , "N"), "S") == p2

def deplace_chemin(c: Coord, d: List[Dir]) -> Coord:
    """Deplace un point sur le chemin donné en utilisant la récursivité"""
    if len(d) == 0:
        return c
    else:
        return deplace_chemin(deplace(c, d[0]), d[1:])

assert deplace_chemin(ori, ["N", "N"]) == p2
assert deplace_chemin(ori, ["N", "E", "S", "O"]) == ori
assert deplace_chemin(ori , []) == ori

Case = Tuple[bool,bool,bool,bool,str]
Laby = List[List[Case]]

laby1 : Laby = [[(True, True, False, False, ""), (False, False, True, False, "ENTREE")],
                [(True, False, False, True, ""),(False, False, True, False, "SORTIE")]]

def deplace_possible(la: Laby, c: Coord, d: Dir) -> bool:
    """Préconditions, c sont des cordonnées de la
    Indique s'il est possible de se déplacer dans la direction choisit"""
    x, y = c
    n, e, s, o, _ = la[x][y]
    if d == "N":
        return n
    elif d == "S":
        return s
    elif d == "E":
        return e
    elif d == "O":
        return o


assert deplace_possible(laby1 , (0, 1), "S")
assert not deplace_possible(laby1 , (0, 1), "N")
assert not deplace_possible(laby1 , (0, 1), "E")

def chemin_possible(la: Laby, c: Coord, ch: List[Dir]) -> bool:
    """Préconditions, c est dans la
    Indique si le chemin indiqué est possible ou non"""
    if len(ch) == 0:
        return True
    elif not deplace_possible(la, c, ch[0]):
        return False
    else:
        return chemin_possible(la, deplace(c, ch[0]), ch[1:])

assert chemin_possible(laby1 , (0, 1), ["S", "E", "N"])
assert chemin_possible(laby1 , (0, 1), ["S", "N", "S", "E", "N"])
assert not chemin_possible(laby1 , (0, 1), ["S", "O"])
assert not chemin_possible(laby1 , (0, 1), ["S", "E", "N", "O"])
        

def est_solution(la: Laby, c: Coord, ch: List[Dir]) -> bool:
    """Préconditions, c est dans le labyrinthe
    Indique si le chemin ch, est solution du labyrinthe"""
    # Vérification si c est une entrée
    x, y = c
    _, _, _, _, state = la[x][y]
    if state != "ENTREE":
        return False

    # Vérification du chemin possible
    elif not chemin_possible(la, c, ch):
        return False

    # Vérification de la position finale de c
    # Le chemin est valide, donc on peut utiliser deplace_chemin
    x_fin, y_fin = deplace_chemin(c, ch)
    _, _, _, _, state_fin = la[x_fin][y_fin]
    if state_fin != "SORTIE":
        return False

    # Si on a jamais return, alors le chemin est solution
    else:
        return True

assert est_solution(laby1 , (0, 1), ["S", "E", "N"])
assert est_solution(laby1 , (0, 1), ["S", "E", "O", "E", "N"])
assert not est_solution(laby1 , (0, 0), ["E", "N"])
assert not est_solution(laby1 , (0, 1), ["S", "E"])
assert not est_solution(laby1 , (0, 1), ["E"])

# Suggestion 2

def random_int(n: int) -> int:
    """Préconditions n >= 0
    Renvoie un entier aléatoire entre 0 et le nombre donné exclus"""
    return int(n * random.random())

assert 0 <= random_int(4) < 4
assert 0 <= random_int(65) < 65
assert 0 <= random_int(32) < 32

def random_path(c: Case) -> Dir:
    """Préconditions case a une sortie
    Renvoie une direction aléatoire possible à prendre dans la case c"""
    n, e, s, o, _ = c
    dir_possible: List[Dir] = []
    
    if n:
        dir_possible.append("N")
    if e:
        dir_possible.append("E")
    if s:
        dir_possible.append("S")
    if o:
        dir_possible.append("O")

    return dir_possible[random_int(len(dir_possible))]


def coord_depart(la: Laby, c: Coord) -> Coord:
    """Préconditions, la contient une entrée, c est dans le labyrinthe
    Trouve les coordonnées de départ de la"""

    # On veut faire une récursivité inverse ici
    # Puisque l'entrée se trouvera plus souvent en début de liste
    x, y = c
    
    _, _, _, _, state = la[x][y]
    
    if state == "ENTREE":
        return c
    else:
        return coord_depart(la, (x, y+1))

assert coord_depart(laby1, (0, 0)) == (0, 1)


def marche_aleatoire(la: Laby, chemin: List[Dir], c_prev: Optional[Coord]) -> Optional[List[Dir]]:
    """Renvoie une chemin aléatoire solution du labyrinthe"""

    # On préfère ici stocker les éléments des coordonnée pour ne pas vaoir utiliser les fonctions récursives de déplacement
    # Qui prendrait trop de place sur la pile
    
    res_next: List[Dir] = chemin[:]

    c: Coord

    if(c_prev == None):
        c = coord_depart(la, (0, 0)) # Ceci prend beaucoup de place dans la pile pour de grand labyrinthe
                                     # Le mieux est de fournir les coordonnées d'entrer du labyrinthe avant l'exécution première
    else:
        c = c_prev # La valeur n'est jamais None
    
    x, y = c
    if len(chemin) > 950:
        # Surcharge de la pile maîtrisé
        return None
    
    _, _, _, _, state = la[x][y]
    
    if state == "SORTIE":
        return chemin

    else:
        dir_alea: Dir = random_path(la[x][y])
        res_next.append(dir_alea)
        return marche_aleatoire(la, res_next, deplace(c, dir_alea))

# Suggestion 3

def marche_droite(la: Laby, chemin: List[Dir], c_prev: Optional[Coord]) -> Optional[List[Dir]]:
    """Renvoie une chemin aléatoire solution du labyrinthe"""

    # On préfère ici stocker les éléments des coordonnée pour ne pas vaoir utiliser les fonctions récursives de déplacement
    # Qui prendrait trop de place sur la pile
    
    res_next: List[Dir] = chemin[:]

    c: Coord

    if(c_prev == None):
        c = coord_depart(la, (0, 0)) # Ceci prend beaucoup de place dans la pile pour de grand labyrinthe
                                     # Le mieux est de fournir les coordonnées d'entrer du labyrinthe avant l'exécution première
    else:
        c = c_prev # La valeur n'est jamais None
    
    x, y = c
    if len(chemin) > 950:
        # Surcharge de la pile maîtrisé
        return None
    
    _, _, _, _, state = la[x][y]
    
    if state == "SORTIE":
        return chemin

    else:
        if deplace_possible(la, c, "E"):
            res_next.append("E")
            return marche_droite(la, res_next, deplace(c, "E"))
        elif deplace_possible(la, c, "N"):
            res_next.append("N")
            return marche_droite(la, res_next, deplace(c, "N"))
        elif deplace_possible(la, c, "O"):
            res_next.append("O")
            return marche_droite(la, res_next, deplace(c, "O"))
        else:
            res_next.append("S")
            return marche_droite(la, res_next, deplace(c, "S"))

assert marche_droite(laby1, [], None) == ['S', 'E', 'N']
