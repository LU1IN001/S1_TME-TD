from typing import Tuple, List, TypeVar, Optional

T = TypeVar('T')
Complexe = Tuple[float, float]

def partie_reelle(c: Complexe) -> float:
    Re, _ = c
    return Re

def partie_imaginaire(c: Complexe) -> float:
    _, Im = c
    return Im

def addition_complexe(c1: Complexe, c2: Complexe) -> Complexe:
    return partie_reelle(c1) + partie_reelle(c2), partie_imaginaire(c1) + partie_imaginaire(c2)

# Exercice 7.5

Point = Tuple[int, int]

def vecteur(p1: Point, p2: Point) -> Point:
    x1, y1 = p1
    x2, y2 = p2
    return (x1-x2, y1-y2)


def alignes(p1: Point, p2: Point, p3: Point) -> bool:
    x1, y1 = vecteur(p1, p2)
    x2, y2 = vecteur(p2, p3)
    return y1*x2 == y2*x1

def alignement(points: List[Point]) -> bool:
    for i in range(2, len(points)):
        if not alignes(points[i-2], points[i-1], points[i]):
            return False
    return True

def repetition_comprehension(e: T, i: int) -> List[T]:
    return [e for _ in range(i)]

def liste_diviseurs(n: int) -> List[int]:
    return [i for i in range(1, n+1) if n%i==0]

def liste_diviseurs_impairs(n: int) -> List[int]:
    return [i for i in range(1, n+1) if n%i == 0 and i%2 != 0]

# Exercice 7.6

Etudiant = Tuple[str, str, int, List[int]]
BaseUPMC : List[Etudiant]
BaseUPMC = [('GARGA', 'Amel', 20231343, [12, 8, 11, 17, 9]),
('POLO', 'Marcello', 20342241, [9, 11, 19, 3]),
('AMANGEAI', 'Hildegard', 20244229, [15, 11, 7, 14, 12]),
('DENT', 'Arthur', 42424242, [8, 4, 9, 4, 12, 5]),
('ALEZE', 'Blaise', 30012024, [17, 15, 20, 14, 18, 16, 20]),
('D2', 'R2', 10100101, [10, 10, 10, 10, 10, 10])]

def note_moyenne(notes: List[int]) -> float:
    if(len(notes) == 0): return 0
    return sum(notes)/len(notes)

def moyenne_generale(l: List[Etudiant]) -> float:
    if(len(l) == 0): return 0
    res = 0
    for _, _, _, notes in l:
        res += note_moyenne(notes)
    return res/len(l)

def top_etudiant(bd: List[Etudiant]) -> Tuple[str, str]:
    nom, prenom, _, notes0 = bd[0]
    identite: Tuple[str, str] = (nom, prenom)
    note_moyenne_max = note_moyenne(notes0)
    for nom, prenom, _, notes in bd:
        if note_moyenne_max < note_moyenne(notes):
            identite = (nom, prenom)
    return identite

def recherche_moyenne(etu: int, bd: List[Etudiant]) -> Optional[float]:
    for _, _, id, notes in bd:
        if(id == etu):
            return note_moyenne(notes)
    return None
