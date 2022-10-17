import TD5 as a

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
