#Exercice 9.6 : Traduction
Dict_Ang_Fra : Dict[str, str]
Dict_Ang_Fra = {'the': 'le', 'cat': 'chat','fish': 'poisson', 'catches': 'attrape'}
Dict_Fra_Ita : Dict[str, str]
Dict_Fra_Ita = {'le': 'il', 'chat': 'gatto','poisson': 'pesce', 'attrape': 'cattura'}



#Question 1
def traduction_mot_a_mot(l : List[str], dico : Dict[str, str]) -> List[str] :
    """Retourne la liste des mots de l traduits à partir du dico"""
    return [dico[c] for c in l]

assert traduction_mot_a_mot([], Dict_Ang_Fra) == []
assert traduction_mot_a_mot(['cat'], Dict_Ang_Fra) == ['chat']
assert traduction_mot_a_mot(['the', 'cat', 'catches', 'the', 'fish'], Dict_Ang_Fra) == ['le', 'chat', 'attrape', 'le', 'poisson']
assert traduction_mot_a_mot(['le', 'chat', 'attrape', 'le', 'poisson'], Dict_Fra_Ita) == ['il', 'gatto', 'cattura', 'il', 'pesce']



#Question 2
def dictionnaire_inverse(dico : Dict[str, str]) -> Dict[str, str] :
    """Retourne le dictionnaire inverse de dico"""
    return {v:k for (k,v) in dico.items()}
    
assert dictionnaire_inverse({"cat": "chat"}) == {'chat': 'cat'}
assert dictionnaire_inverse(Dict_Ang_Fra) == {'le': 'the', 'chat': 'cat', 'poisson': 'fish', 'attrape': 'catches'}
assert dictionnaire_inverse(Dict_Fra_Ita) == {'il': 'le', 'gatto': 'chat', 'pesce': 'poisson', 'cattura': 'attrape'}



#Question 3
def composition_dictionnaires(dico : Dict[str, str], dico2 : Dict[str, str]) -> Dict[str, str] :
    """Retourne le dictionnaire composé des deux dictionnaires"""
    return {k1:v2 for (k1,_) in dico.items() for (k2,v2) in dico2.items()}

assert composition_dictionnaires({"chat":"cat"}, {"cat":"gatto"}) == {'chat': 'gatto'}
assert composition_dictionnaires(Dict_Ang_Fra, Dict_Fra_Ita) == {'the': 'cattura', 'cat': 'cattura', 'fish': 'cattura', 'catches': 'cattura'}

