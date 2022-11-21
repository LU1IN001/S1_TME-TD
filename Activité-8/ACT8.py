# Wilhem Blondel
from typing import List, Tuple, Dict, Optional

def ouvre_fichier(nom: str) -> List[str]:
    """Renvoie la liste des lignes du fichier texte ./nom.csv"""
    with open("./"+nom+".csv", "r") as f:
        return f.readlines()

exemple1 : List[str] = ['"sport";"date";"participants";"vainqueur"\n',
                        '"boxe";2021-09-18;12;"Alice"\n',
                        '"boxe";2021-09-25;10;"Alice"\n',
                        '"karate";2021-09-26;19;"Carole"\n',
                        '"boxe";2021-10-02;8;"Bob"\n',
                        '"karate";2021-10-03;20;"Carole"\n',
                        '"tennis";2021-10-04;3;"Alice"\n',
                        '"boxe";2021-10-09;5;"Alice"\n',
                        '"karate";2021-10-10;20;"Damien"\n',
                        '"boxe";2021-10-16;6;"Carole"\n',
                        '"echecs";2021-09-17;120;"Bob"\n',
                        '"echecs";2021-09-24;120;"Bob"\n',
                        '"echecs";2021-10-01;120;"Carole"\n']


# Partie Guidée

def decompose_ligne(li: str, sep: str) -> List[str]:
    """Préconditions: len(sep) == 1, li doit contenir un chariot à la fin
    Retourne la liste d'éléments de li séparé par le sep"""
    res: List[str] = []
    c: str
    mot: str = ""
    for c in li:
        if(c == sep):
            res.append(mot)
            mot = ""
        else:
            mot = mot + c
    res.append(mot[:-1])
    return res

assert decompose_ligne(exemple1[0], ";") == ['"sport"', '"date"', '"participants"', '"vainqueur"']
assert decompose_ligne(exemple1[3], ";") == ['"karate"', '2021-09-26', '19', '"Carole"']
assert decompose_ligne(exemple1[3], ",") == ['"karate";2021-09-26;19;"Carole"']


def enleve_guillemets(s: str) -> str:
    """Retire les guillemets d'une chaîne de caractère"""
    res: str = ""
    e: str  
    for e in s:
        if not e == '"':
            res = res + e
    return res

assert enleve_guillemets('"sport"') == 'sport'
assert enleve_guillemets('sport') == 'sport'


def enleve_guillemets_ligne(li: List[str]) -> List[str]:
    """Retire tous les guillemets d'une liste de chaîne de caractères"""
    return [enleve_guillemets(e) for e in li]

assert enleve_guillemets_ligne(['"sport"', '"date"', '"participants"', '"vainqueur"']) == ['sport', 'date', 'participants', 'vainqueur']
assert enleve_guillemets_ligne(['"karate"', '2021-09-26', '19', '"Carole"']) == ['karate', '2021-09-26', '19', 'Carole']


def lignes_propres(lis: List[str], sep: str) -> List[List[str]]:
    """Préconditions: len(sep) == 1
    Retourne la liste d'éléments de li séparé par le sep
    Dans laquelle on a retiré les guillemens"""
    # return [enleve_guillemets_ligne(decompose_ligne(li, sep)) for li in lis]
    return [enleve_guillemets_ligne(e) for e in [decompose_ligne(li, sep) for li in lis]]

assert lignes_propres(exemple1, ";") == [['sport', 'date', 'participants', 'vainqueur'], ['boxe', '2021-09-18', '12', 'Alice'], ['boxe', '2021-09-25', '10', 'Alice'], ['karate', '2021-09-26', '19', 'Carole'], ['boxe', '2021-10-02', '8', 'Bob'], ['karate', '2021-10-03', '20', 'Carole'], ['tennis', '2021-10-04', '3', 'Alice'], ['boxe', '2021-10-09', '5', 'Alice'], ['karate', '2021-10-10', '20', 'Damien'], ['boxe', '2021-10-16', '6', 'Carole'], ['echecs', '2021-09-17', '120', 'Bob'], ['echecs', '2021-09-24', '120', 'Bob'], ['echecs', '2021-10-01', '120', 'Carole']]


def cherche_indice(indice: str, li: List[str]) -> Optional[int]:
    """Renvoie l'index dans la liste li correspondant à l'indice indiqué"""
    i: int
    for i in range(len(li)):
        if li[i] == indice:
            return i
    return None

assert cherche_indice("sport", ['sport', 'date', 'participants', 'vainqueur'])  == 0
assert cherche_indice("vainqueur", ['sport', 'date', 'participants', 'vainqueur'])  == 3
assert cherche_indice("deces", ['sport', 'date', 'participants', 'vainqueur']) == None

def dictionnaire_compte(lis: List[List[str]], clef: str) -> Dict[str, int]:
    """Préconditions, la première liste de lis doit être une liste d'indexion contenant les clefs
    la valeur de la clef doit corespondre à un str dans la liste lis

    Renvoie le dictionnaire du nombre d'occurences de chaque élément donné par la clef"""
    res: Dict[str, int] = dict()
    index: Optional[int] = cherche_indice(clef, lis[0])
    if index == None:
        return res
    l: List[str]
    for l in lis[1:]:
        e: str = l[index]
        if not e in res:
            res[e] = 0
        res[e] = res[e] + 1
    return res


lignes_ex1 : List[List[str]] = lignes_propres(exemple1, ";")

assert dictionnaire_compte(lignes_ex1 , "vainqueur") == {'Alice': 4, 'Carole': 4, 'Bob': 3, 'Damien': 1} 
assert dictionnaire_compte(lignes_ex1 , "sport") == {'boxe': 5, 'karate': 3, 'tennis': 1, 'echecs': 3}

def dictionnaire_somme(lis: List[List[str]], clef: str, valeur: str) -> Dict[str, int]:
    """Préconditions, la valeur donnée doit être correspondre à un int et la clef à un str dans lis
    la première liste de lis doit être une liste d'indexion contenant les clefs
    
    Renvoie le dictionnaire qui a pour clé les éléments tiré de clef
    Et pour valeurs les éléments tirés de valeurs"""
    res: Dict[str, int] = dict()
    index_k: Optional[int] = cherche_indice(clef, lis[0])
    index_v: Optional[int] = cherche_indice(valeur, lis[0])
    if index_k == None or index_v == None:
        return res
    
    l: List[str]
    for l in lis[1:]:
        k: str = l[index_k]
        v: int = int(l[index_v])
        if not k in res:
            res[k] = 0
        res[k] = res[k] + v
    return res

assert dictionnaire_somme(lignes_ex1 , "sport", "participants")  == {'boxe': 41, 'karate': 59, 'tennis': 3, 'echecs': 360}

# Suggestion 2

def diff_mois(ori: int, month: int) -> int:
    """Préconditions ori <= 12 and month <= 12
    Retourne la différebce entre deux mois"""
    if month >= ori:
        return month - ori
    elif ori == 12:
        return (ori + month) % 12
    else:
        return ((ori + month) // 3)

def date_to_day(ori: str, date: str) -> int:
    """Précondtions, date a le format yyyy-mm-dd, date doit être plus lointain que ori
    Retourne le nombre de jour qui sépare ori de date"""
    # Initialisation des données
    # Listes des jours dans le mois
    month_to_day: List[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Origine
    ldate_ori: List[str] = decompose_ligne(ori, '-')
    year_ori: int = int(ldate_ori[0])
    month_ori: int = int(ldate_ori[1])
    day_ori: int = int(ldate_ori[2])
    # Date 
    ldate: List[str] = decompose_ligne(date, '-')
    year: int = int(ldate[0])
    month: int = int(ldate[1])
    day: int = int(ldate[2])


    # Différence des deux dates
    year = year-year_ori
    diff_month: int = diff_mois(month_ori, month)

    if diff_month == 0:
        # On se trouve dans le même mois
        day = day - day_ori

    else:
        for i in range(diff_month):
            index: int = ((month_ori + i)%12) - 1
    
    return 1
