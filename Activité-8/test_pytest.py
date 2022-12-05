from ACT8 import *

def test_q_1():
    assert decompose_ligne(exemple1[0], ";") == ['"sport"', '"date"', '"participants"', '"vainqueur"']
    assert decompose_ligne(exemple1[3], ";") == ['"karate"', '2021-09-26', '19', '"Carole"']
    assert decompose_ligne(exemple1[3], ",") == ['"karate";2021-09-26;19;"Carole"']


def test_q_2():
    assert enleve_guillemets('"sport"') == 'sport'
    assert enleve_guillemets('sport') == 'sport'

def test_q_3():
    assert enleve_guillemets_ligne(['"sport"', '"date"', '"participants"', '"vainqueur"']) == ['sport', 'date', 'participants', 'vainqueur']
    assert enleve_guillemets_ligne(['"karate"', '2021-09-26', '19', '"Carole"']) == ['karate', '2021-09-26', '19', 'Carole']

def test_q_4():
    assert lignes_propres(exemple1, ";") == [['sport', 'date', 'participants', 'vainqueur'], ['boxe', '2021-09-18', '12', 'Alice'], ['boxe', '2021-09-25', '10', 'Alice'], ['karate', '2021-09-26', '19', 'Carole'], ['boxe', '2021-10-02', '8', 'Bob'], ['karate', '2021-10-03', '20', 'Carole'], ['tennis', '2021-10-04', '3', 'Alice'], ['boxe', '2021-10-09', '5', 'Alice'], ['karate', '2021-10-10', '20', 'Damien'], ['boxe', '2021-10-16', '6', 'Carole'], ['echecs', '2021-09-17', '120', 'Bob'], ['echecs', '2021-09-24', '120', 'Bob'], ['echecs', '2021-10-01', '120', 'Carole']]

def test_d_5():
    assert cherche_indice("sport", ['sport', 'date', 'participants', 'vainqueur'])  == 0
    assert cherche_indice("vainqueur", ['sport', 'date', 'participants', 'vainqueur'])  == 3
    assert cherche_indice("deces", ['sport', 'date', 'participants', 'vainqueur']) == None  

def test_q_6():
    assert dictionnaire_compte(propres , "vainqueur") == {'Alice': 4, 'Carole': 4, 'Bob': 3, 'Damien': 1} 
    assert dictionnaire_compte(propres , "sport") == {'boxe': 5, 'karate': 3, 'tennis': 1, 'echecs': 3}

def test_q_7():
    assert dictionnaire_somme(propres , "sport", "participants")  == {'boxe': 41, 'karate': 59, 'tennis': 3, 'echecs': 360}