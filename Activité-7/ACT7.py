
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
    if not chemin_possible(la, c, ch):
        return False

    # Vérification de la position finale de c
    # Le chemin est valide, donc on peut utiliser deplace_chemin
    x_fin, y_fin = deplace_chemin(c, ch)
    _, _, _, _, state_fin = la[x_fin][y_fin]
    if state_fin != "SORTIE":
        return False

    # Si on a jamais return, alors le cehmin est solution
    return True

assert est_solution(laby1 , (0, 1), ["S", "E", "N"])
assert est_solution(laby1 , (0, 1), ["S", "E", "O", "E", "N"])
assert not est_solution(laby1 , (0, 0), ["E", "N"])
assert not est_solution(laby1 , (0, 1), ["S", "E"])
assert not est_solution(laby1 , (0, 1), ["E"])
    


        
