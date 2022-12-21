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