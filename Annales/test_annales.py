from annales_2021_bis import *

def test_q_2_1():
    assert effectifs_UE(LicenseInfo, "Lambda") == 5
    assert effectifs_UE(LicenseInfo, "IA") == 0
    assert effectifs_UE(LicenseInfo, "Microbio") == 0
    assert effectifs_UE(dict(), "Lambda") == 0

def test_q_2_2():
    assert etudiants(LicenseInfo) == {'Carole', 'Elise', 'Alice', 'Bob', 'David'}
    assert etudiants(dict()) == set()

def test_q_2_3():
    assert inscriptions_etu(LicenseInfo, "Bob") == {"BDD", "Lambda", "POO", "Compil"}
    assert inscriptions_etu(LicenseInfo, "Elise") == {"POO", "Lambda"}
    assert inscriptions_etu(LicenseInfo, "Fadia") == set()

def test_q_2_4():
    assert inscriptions_tous(LicenseInfo) == {"Alice": {"Compil", "BDD", "Lambda"},
                                              "Bob": {"BDD", "Lambda", "POO", "Compil"},
                                              "Carole": {"BDD", "Lambda"},
                                              "David": {"Compil", "Lambda"},
                                              "Elise": {"POO", "Lambda"}}

def test_q_2_5():
    assert doubles_licenses(Faculte2Science) == {"David", "Elise"}

def test_q_4_1():
    assert moyenne([0, 0, 0, 0]) == 0
    assert moyenne([255, 255, 0, 0]) == 127
    assert moyenne([100]) == 100

def test_q_4_2():
    assert est_noir((0,0,0)) == True
    assert est_noir((127, 127, 0)) == False

def test_q_4_3():
    assert listes_par_couleur([(0, 0, 0), (255, 255, 255), (0, 127, 255), (255, 127, 0)]) == ([0, 255, 0, 255], [0, 255, 127, 127], [0, 255, 255, 0])
    assert listes_par_couleur([(0, 127, 50)]) == ([0], [127], [50])
    assert listes_par_couleur([]) == ([], [], [])

def test_q_4_5():
    assert compression([[(0, 0, 0), (255, 0, 0)], [(148, 0, 101), (0, 128, 0)]]) == [[(100, 32, 25)]]
    assert compression([[(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 0)], [(0, 255, 0), (0, 0, 255), (255, 0, 0), (0, 255, 0)],[(0, 0, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)], [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 0)]]) == [[(63, 127, 63), (127, 63, 63)], [(127, 63, 63), (63, 63, 127)]]