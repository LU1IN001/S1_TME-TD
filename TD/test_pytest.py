import TD5 as a
import TD6 as b
from typing import List, Tuple

Etudiant = Tuple[str, str, int, List[int]]
BaseUPMC : List[Etudiant]
BaseUPMC = [('GARGA', 'Amel', 20231343, [12, 8, 11, 17, 9]),
('POLO', 'Marcello', 20342241, [9, 11, 19, 3]),
('AMANGEAI', 'Hildegard', 20244229, [15, 11, 7, 14, 12]),
('DENT', 'Arthur', 42424242, [8, 4, 9, 4, 12, 5]),
('ALEZE', 'Blaise', 30012024, [17, 15, 20, 14, 18, 16, 20]),
('D2', 'R2', 10100101, [10, 10, 10, 10, 10, 10])]

def test_repetition():
    assert a.repetition("thon", 4) == ['thon', 'thon', 'thon', 'thon']
    assert a.repetition(3, 8) == [3, 3, 3, 3, 3, 3, 3, 3]
    assert a.repetition(5, 0) == []
    assert a.repetition([1, 2, 3], 5) == [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]

def test_repition_bloc():
    assert a.repetition_bloc(["chat", "thon", "loup"], 3) == ['chat', 'thon', 'loup', 'chat', 'thon', 'loup', 'chat', 'thon', 'loup']
    assert a.repetition_bloc([1, 2, 3], 5) == [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
    assert a.repetition_bloc([1, 2, 3, 4, 5], 0) == []

def test_max_liste():
    assert a.max_liste([3, 7, 9, 5.4, 8.9, 9, 8.999, 5]) == 9

def test_nb_occurrence():
    assert a.nb_occurrences([3, 7, 9, 5.4, 8.9, 9, 8.999, 5], 9) == 2
    assert a.nb_occurrences(["chat", "ours", "chat", "chat", "loup"], "chat") == 3
    assert a.nb_occurrences(["chat", "ours", "chat", "chat", "loup"], "ou") == 0

def test_nb_max():
    assert a.nb_max([3, 7, 9, 5.4, 8.9, 9, 8.999, 5]) == 2
    assert a.nb_max([-2, -1, -5, -3, -1, -4, -1]) == 3

def test_list_mult():
    assert a.list_mult([3, 5, 9, 4], 2) == [6, 10, 18, 8]
    assert a.list_mult([], 2) == []

def test_list_div():
    assert a.list_div([2, 7, 9, 24, 6], 2) == [1, 12, 3]
    assert a.list_div([2, 7, 9, 24, 6], 3) == [3, 8, 2]
    assert a.list_div([2, 7, 9, 24, 6], 5) == []
    assert a.list_div([2, 7, 9, -24, 6], -3) == [-3, 8, -2]
    assert a.list_div([], 3) == []

def test_somme():
    assert a.somme([1, 2, 3, 4, 5]) == 15
    assert a.somme([1, 2.5, 3.2, 4, 5]) == 15.7
    assert a.somme([1, 2.5, 3.5, 4, 5]) == 16.0
    assert a.somme([]) == 0

def test_moyenne():
    assert a.moyenne([1, 2, 3, 4, 5]) == 3.0
    assert a.moyenne([1, 2.5, 3.5, 4, 5]) == 3.2
    assert a.moyenne([5]) == 5

def test_carres():
    assert a.carres([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
    assert a.carres([-5, -1, 2]) == [25, 1, 4]
    assert a.carres([]) == []
    assert a.carres([10, 0.5]) == [100, 0.25]

def test_variance():
    assert a.variance([10, 10, 10, 10]) == 0.0
    assert a.variance([20, 0, 20, 0]) == 100.0

def test_ecart_type():
    assert a.ecart_type([10, 10, 10, 10]) == 0.0
    assert a.ecart_type([20, 0, 20, 0]) == 10.0
    assert a.ecart_type([15, 15, 5, 5]) == 5.0
    assert abs(a.ecart_type([12, 11, 10, 12, 11]) - 0.7483314773547993) <= 10**-15

def test_partie_reelle():
    assert b.partie_reelle((2.0, 3.0)) == 2.0
    assert b.partie_reelle((0.0, 1.0)) == 0.0
    assert b.partie_reelle((4.0, 0.0)) == 4.0

def test_partie_imaginaire():
    assert b.partie_imaginaire((2.0, 3.0)) == 3.0
    assert b.partie_imaginaire((0.0, 1.0)) == 1.0
    assert b.partie_imaginaire((4.0, 0.0)) == 0.0

def test_addition_complexe():
    assert b.addition_complexe((1.0, 0.0), (0.0, 1.0)) == (1.0, 1.0)
    assert b.addition_complexe((2.0, 3.0), (0.0, 1.0)) == (2.0, 4.0)

def test_alignes():
    assert b.alignes((0,0), (1,1), (5,5)) == True
    assert b.alignes((0,0), (1,1), (1,2)) == False

def test_alignement():
    assert b.alignement([(0,0), (1,1), (5,5)]) == True
    assert b.alignement([(0,0), (1,1), (5,5), (1,0)]) == False

def test_repetition_comprehension():
    assert b.repetition_comprehension("thon", 4) == ['thon', 'thon', 'thon', 'thon']
    assert b.repetition_comprehension(3, 8) == [3, 3, 3, 3, 3, 3, 3, 3]
    assert b.repetition_comprehension(5, 0) == []
    assert b.repetition_comprehension([1, 2, 3], 5) == [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]

def test_liste_diviseurs():
    assert b.liste_diviseurs(18) == [1, 2, 3, 6, 9, 18]

def test_liste_diviseurs_impairs():
    assert b.liste_diviseurs_impairs(24) == [1, 3]
    assert b.liste_diviseurs_impairs(8) == [1]
    assert b.liste_diviseurs_impairs(15) == [1, 3, 5, 15]

def test_note_moyenne():
    assert b.note_moyenne([12, 8, 14, 6, 5, 15]) == 10.0
    assert b.note_moyenne([]) == 0.0

def test_moyenne_generale():
    assert abs(b.moyenne_generale(BaseUPMC) - 11.307142857142857) <= 10**-15
    assert b.moyenne_generale([]) == 0

def test_top():
    assert b.top_etudiant(BaseUPMC) == ('ALEZE', 'Blaise')

def test_recherche_moyenne():
    assert b.recherche_moyenne(20244229, BaseUPMC) == 11.8
    assert b.recherche_moyenne(20342241, BaseUPMC) == 10.5
    assert b.recherche_moyenne(2024129111, BaseUPMC) == None