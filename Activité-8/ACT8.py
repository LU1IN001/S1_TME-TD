# Wilhem Blondel
from typing import List, Tuple, Dict, Optional, TypeVar, Callable
T = TypeVar('T')

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
    return [enleve_guillemets_ligne(e) for e in [decompose_ligne(li, sep) for li in lis]]

assert lignes_propres(exemple1, ";") == [['sport', 'date', 'participants', 'vainqueur'], ['boxe', '2021-09-18', '12', 'Alice'], ['boxe', '2021-09-25', '10', 'Alice'], ['karate', '2021-09-26', '19', 'Carole'], ['boxe', '2021-10-02', '8', 'Bob'], ['karate', '2021-10-03', '20', 'Carole'], ['tennis', '2021-10-04', '3', 'Alice'], ['boxe', '2021-10-09', '5', 'Alice'], ['karate', '2021-10-10', '20', 'Damien'], ['boxe', '2021-10-16', '6', 'Carole'], ['echecs', '2021-09-17', '120', 'Bob'], ['echecs', '2021-09-24', '120', 'Bob'], ['echecs', '2021-10-01', '120', 'Carole']]

propres: List[List[str]] = lignes_propres(exemple1, ";")


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


assert dictionnaire_compte(propres , "vainqueur") == {'Alice': 4, 'Carole': 4, 'Bob': 3, 'Damien': 1} 
assert dictionnaire_compte(propres , "sport") == {'boxe': 5, 'karate': 3, 'tennis': 1, 'echecs': 3}

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

assert dictionnaire_somme(propres , "sport", "participants")  == {'boxe': 41, 'karate': 59, 'tennis': 3, 'echecs': 360}

# Suggestion 2

def diff_mois(ori: int, month: int) -> int:
    """Préconditions ori <= 12 and month <= 12
    Retourne la différence entre deux mois dernier mois non inclus"""
    if ori > month:
        return month + 12 - ori
    else:
        return month - ori

assert diff_mois(12, 3) == 3
assert diff_mois(3, 12) == 9
assert diff_mois(10, 1) == 3
assert diff_mois(1, 1) == 0

def diff_mois_en_jour(ori: int, month: int) -> int:
    """Préconditions ori <= 12 and month <= 12
    Retourne la différence en jour des deux mois données dernier mois non inclus"""
    index_to_move: int = diff_mois(ori, month)
    # Listes des jours dans le mois
    month_to_day: List[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res: int = 0
    i: int
    for i in range(index_to_move):
        res = res + month_to_day[(ori-1+i)%12]
    return res

assert diff_mois_en_jour(11, 12) == 30
assert diff_mois_en_jour(1, 3) == 59
assert diff_mois_en_jour(1, 12) == 365-31 # On retire le dernier mois non inclus

def date_to_day(ori: str, date: str) -> int:
    """Précondtions, date a le format yyyy-mm-dd
    Retourne le nombre de jour qui sépare ori de date, derbier jour non inclus"""
    # Origine
    ldate_ori: List[str] = decompose_ligne(ori+"\n", '-')
    year_ori: int = int(ldate_ori[0])
    month_ori: int = int(ldate_ori[1])
    day_ori: int = int(ldate_ori[2])
    # Date 
    ldate: List[str] = decompose_ligne(date+"\n", '-')
    year: int = int(ldate[0])
    month: int = int(ldate[1])
    day: int = int(ldate[2])


    # Différence des deux dates
    nyear: int = year-year_ori
    diff_month_day: int = diff_mois_en_jour(month_ori, month)
    if year == year_ori and month == month_ori:
        return day - day_ori
    if month_ori > month:
        return int(nyear*365 - diff_month_day + day - day_ori - 3)
    else:
        return int(nyear*365 + diff_month_day + day - day_ori)

# Jeu de test avec https://www.timeanddate.com/date/
# On a retiré les jours des années bissextiles
assert date_to_day("2006-03-05", "2012-05-28") == 2274
assert date_to_day("1900-01-01", "1901-01-01") == 365
assert date_to_day("1900-01-01", "1900-01-01") == 0
assert date_to_day("2006-11-05", "2010-05-28") == 1299

def find_smallest_date_index(d: List[List[str]], date_name: str) -> Tuple[str, int]:
    """Préconditions cherche_indice(date_name) != None
    Retourne l'indice et la date de la colonne ayant la date la plus petite du dictionnaire"""
    indice_date: int = cherche_indice(date_name, d[0])
    index_min: int = 1
    date_min: str = d[1][indice_date]
    i: int = 1
    data: List[str]
    for data in d[2:]:
        date: str = data[indice_date]
        if date_to_day(date, date_min) > 0:
            date_min = date
            index_min = i+1
        i = i + 1
    return (date_min, index_min)

assert find_smallest_date_index(lignes_propres(exemple1, ";"), "date") == ("2021-09-17",10)

def remove_data_from_date(d: List[List[str]], date_name: str, date: str) -> List[List[str]]:
    """Renvoie une liste qui ne contient pas la première occurence de la date donnée"""
    res: List[List[str]] = []
    indice: int = cherche_indice(date_name, d[0])
    done: bool = False
    i: int
    for i in range(len(d)):
        if d[i][indice] == date and not done:
            done = True
        else:
            res.append(d[i])
    return res

assert remove_data_from_date(propres, "date", '2021-09-24') == [['sport', 'date', 'participants', 'vainqueur'], ['boxe', '2021-09-18', '12', 'Alice'], ['boxe', '2021-09-25', '10', 'Alice'], ['karate', '2021-09-26', '19', 'Carole'], ['boxe', '2021-10-02', '8', 'Bob'], ['karate', '2021-10-03', '20', 'Carole'], ['tennis', '2021-10-04', '3', 'Alice'], ['boxe', '2021-10-09', '5', 'Alice'], ['karate', '2021-10-10', '20', 'Damien'], ['boxe', '2021-10-16', '6', 'Carole'], ['echecs', '2021-09-17', '120', 'Bob'], ['echecs', '2021-10-01', '120', 'Carole']]

def organise_data_from_date(d: List[List[str]], date_name: str) -> List[List[str]]:
    """Réorganise la liste dans l'ordre des dates
    et Regroupe les éléments ayant une même date ensemble"""
    res: List[List[str]] = [d[0]]
    indice: int = cherche_indice(date_name, d[0])
    new_scan: List[List[str]] = d[:]
    for _ in range(len(d)-1):
        date, i = find_smallest_date_index(new_scan, date_name)
        res.append(new_scan[i])
        new_scan = remove_data_from_date(new_scan, date_name, date)
    return res

assert organise_data_from_date(propres, "date") == [['sport', 'date', 'participants', 'vainqueur'], ['echecs', '2021-09-17', '120', 'Bob'], ['boxe', '2021-09-18', '12', 'Alice'], ['echecs', '2021-09-24', '120', 'Bob'], ['boxe', '2021-09-25', '10', 'Alice'], ['karate', '2021-09-26', '19', 'Carole'], ['echecs', '2021-10-01', '120', 'Carole'], ['boxe', '2021-10-02', '8', 'Bob'], ['karate', '2021-10-03', '20', 'Carole'], ['tennis', '2021-10-04', '3', 'Alice'], ['boxe', '2021-10-09', '5', 'Alice'], ['karate', '2021-10-10', '20', 'Damien'], ['boxe', '2021-10-16', '6', 'Carole']]

def compte_date_clef(d: List[List[str]], clef: str, valeur: str, date_name: str) -> Dict[str, int]:
    """Précondtions clef est un élément de d
    Renvoie le dictionnaire comptant le nombre d'occurence de la valeur, dans la colonne clef donnée pour chaque date
    Les données sont dans l'ordre croissant des dates"""
    indice_date: int = cherche_indice(date_name, d[0])
    indice_val: int = cherche_indice(clef, d[0])
    data: List[List[str]] = organise_data_from_date(d, date_name)
    res: Dict[str, int] = dict()
    for e in data:
        if e[indice_val] == valeur:
            date: str = e[indice_date]
            if date not in res.keys():
                res[date] = 1
            else:
                res[date] = res[indice_date]+1
    return res


assert compte_date_clef(propres, "sport", "boxe", "date") == {'2021-09-18': 1, '2021-09-25': 1, '2021-10-02': 1, '2021-10-09': 1, '2021-10-16': 1}
assert compte_date_clef(propres, "sport", "echecs", "date") == {'2021-09-17': 1, '2021-09-24': 1, '2021-10-01': 1}

def somme_date_valeur(d: List[List[str]], clef: str, date_name: str) -> Dict[str, int]:
    """Précondtions clef est un élément de d et son contenu est quantifiable
    Renvoie le dictionnaire sommant toutes les valeurs de la colonne clef pour chaque jour"""
    indice_date: int = cherche_indice(date_name, d[0])
    indice_val: int = cherche_indice(clef, d[0])
    data: List[List[str]] = organise_data_from_date(d, date_name)
    res: Dict[str, int] = dict()
    for e in data[1:]:
        date: str = e[indice_date]
        if date not in res.keys():
            res[date] = 0
        res[date] = res[date] + int(e[indice_val])
    return res

assert somme_date_valeur(lignes_propres(exemple1, ";"), "participants", "date") == {'2021-09-17': 120, '2021-09-18': 12, '2021-09-24': 120, '2021-09-25': 10, '2021-09-26': 19, '2021-10-01': 120, '2021-10-02': 8, '2021-10-03': 20, '2021-10-04': 3, '2021-10-09': 5, '2021-10-10': 20, '2021-10-16': 6}

def convert_dic_duration(d: Dict[str, int]) -> Tuple[Dict[int, int], int]:
    """Convertit le dictionnaire fournit en un nouveau dictionnaire (durée, valeur) où la durée est déterminé par la première date du dictionnaire
    Renvoie également la valeur maximal de la durée dans le dictionnaire"""
    unset: bool = True
    res: Dict[int, int] = dict()
    date_ori: str
    duration_f: int = 0
    for date, v in d.items():
        if unset:
            date_ori = date
            res[0] = v
            unset = False
        else:
            duration_f = date_to_day(date_ori, date)
            res[duration_f] = v
    return res, duration_f
        

def max_min_values(dic: Dict[T, int]) -> Tuple[int, int]:
    """Retourne les valeurs maximales et minimales d'un dictionnaire"""
    v_min: int = 0
    v_max: int = 0
    unset: bool = True
    for _, v in dic.items(): # dic.values() inconnues ?
        if unset:
            # On évite de recréer une liste à partir du dictionnaire
            # Car celui-ci en outre provient normalement déjà d'une liste
            unset = False
            v_min = v
            v_max = v
            
        elif v_min > v:
            v_min = v
            
        elif v_max < v:
            v_max = v
            
    return (v_max, v_min)

assert max_min_values(somme_date_valeur(lignes_propres(exemple1, ";"), "participants", "date")) == (120, 3)

def x_y(x: int, y: int, x_min: int, x_max: int, y_min: int, y_max: int) -> Tuple[float, float]:
    """Retourne le couple x et y correspondant aux valeurs forunies"""
    x_res: float = (2*x/(x_max+x_min)) - 1

    y_res: float = (2*y/(y_max+y_min)) - 1
    return x_res, y_res
    

def image_courbe(csv: str, sep: str, date_name: str, clef: str, valeur: Optional[str] = None) -> Image:
    """Renvoie l'image de la courbe demandée selon les dates
    csv - Le nom du fichier CSV à ouvrir
    clef - La colonne du tableau comptée
    valeur - La valeur à trouver (optionnel, nécéssaire pour compter le nombre d'occurence de la valeur par jour)"""

    res: Image = draw_line(-2, -2, -2, -2) # Initialisation hors du cadre
    data: List[List[str]] = lignes_propres(ouvre_fichier(csv), sep)
    analyse: Dict[int, int]
    
    if valeur == None:
        # Les valeurs seront sommées
        analyse, max_duration = convert_dic_duration(somme_date_valeur(data, clef, date_name))
    else:
        # Les valeurs seront comptées
        analyse, max_duration = convert_dic_duration(compte_date_clef(data, clef, valeur, date_name))
    v_max, v_min = max_min_values(analyse)
    unset: bool = True
    d_prev: int = 0
    v_prev: int = 0
    for d, v in analyse.items():
        if unset:
            d_prev = d
            v_prev = v
            unset = False
        else:
            x_prev, y_prev = x_y(d_prev, v_prev, 0, max_duration, v_min, v_max)
            x, y = x_y(d, v, 0, max_duration, v_min, v_max)
            d_prev = d
            v_prev = v
            res = overlay(res, draw_line(x_prev, y_prev, x, y))
    return res

# show_image(image_courbe("tournois", ";", "date", "participants"))

# Suggestion 3

def retrieve_data_under_condition(csv: str, condition: Callable[[str], bool], skip_first: bool) -> List[str]:
    """Renvoie les lignes du csv validant la condition
    N'appliquera pas la condition d'ajout si skip_first est True pour la première ligne"""
    res: List[str] = []
    first: bool = True
    with open(csv+".csv", "r") as f:
        for l in f.readlines():
            if not first:
                if condition(l):
                    res.append(l)
            else:
                res.append(l)
                first = False

    return res

def construct_dic_with_no_sort(l: List[str], sep: str, clef: str, date_name: str) -> Tuple[Dict[int, float], float, float, float]:
    """
    Préconditions: len(l) > 1
    - la colonne de clef contient des données quantifiables
    - la colonne de date contient des dates de la forme yyyy-mm-dd

    Paramètre:
    l - la liste des lignes à analyser
    sep - le spérateur du fichier csv
    clef - la colonne contenant les valauers à sommer
    date-name - le nom de la colonne contenant les dates

    Que fait la fonction:
    
    Construit le dictionnaire de donnée pour le graphe sans s'occuper du tri en un seul jet
    L'objectif est de traiter de larges données efficacement
    Ainsi la fonction renvoie également les éléments suivants dans cette ordre:
    - Dictionnaire {durée: valeur}
    - durée_max
    - valeur_max
    - valeur_min
    """

    i: int
    # Permet de savoir si les premières informations cruciales ont été définies ou non
    # L'objectif est de compter le nombre de tour de boucle pour être sûr d'intialiser correctement les données intiales
    # Cela évite de sectionner l, qui peut être une liste très grande, et donc de consommer encore plus de mémoire
    analyse: List[str]
    res_dic: Dict[int, float] = dict()
    duree_max: int
    v_min: float
    v_max: float
    indice_val: int
    indice_date: int
    date_ori: str
    for i in range(len(l)):
        analyse = decompose_ligne(enleve_guillemets_ligne(l[i]), ";")
        if i == 0:
            # Analyse du premier index, l'objectif est de jamais recalculer les indices
            indice_val = cherche_indice(clef, analyse)
            indice_date = cherche_indice(date_name, analyse)
            duree_max = date_to_day(decompose_ligne(enleve_guillemets_ligne(l[1]),sep)[indice_date], decompose_ligne(enleve_guillemets_ligne(l[-1]), sep)[indice_date])
        if i == 1:
            date_ori = analyse[indice_date]
            v_min = int(analyse[indice_val])
            v_max = v_min
            res_dic[0] = v_min
            
        elif i > 1:
            date = analyse[indice_date] 
            v = int(analyse[indice_val])

            # Gestion du dictionnaire...
            duration: int = date_to_day(date_ori, date)
            if duration not in res_dic:
                res_dic[duration] = 0
            res_dic[duration] = res_dic[duration] + v
            # Gestion des valeurs max et min...
            if v_max < res_dic[duration]:
                v_max = res_dic[duration]
            elif v_min > res_dic[duration]:
                v_min = res_dic[duration]

                
    return res_dic, duree_max, v_max, v_min
    
    


def image_courbe_n(csv: str, sep: str, date_name: str, clef: str, ordonne: bool, condition: Optional[Callable[[str], bool]] = None) -> Image:
    """Renvoie l'image de la courbe demandée selon les dates
    csv - Le nom du fichier CSV à ouvrir
    clef - La colonne du tableau comptée
    condition - ne calculera pas le graphe pour les valauers ne respectants pas la condition
    ordonne - Faut-il ordonner (True) les données ou sont elles déjà ordonnées ? (False)"""

    res: Image = draw_line(-2, -2, -2, -2) # Initialisation hors du cadre
    data: List[str]
    if condition == None:
        data = ouvre_fichier(csv)
            

    else:
        data = retrieve_data_under_condition(csv, condition, True)
    
    if ordonne:
        # Les valeurs seront ordonnées et sommées
        analyse, max_duration = convert_dic_duration(somme_date_valeur(lignes_propres(data, sep), clef, date_name))
        v_max, v_min = max_min_values(analyse)
    else:
        analyse, max_duration, v_max, v_min = construct_dic_with_no_sort(data, sep, clef, date_name)
    
    unset: bool = True
    d_prev: int = 0
    for d, v in analyse.items():
        if unset:
            d_prev = d
            v_prev = v
            unset = False
        else:
            x_prev, y_prev = x_y(d_prev, v_prev, 0, max_duration, v_min, v_max)
            x, y = x_y(d, v, 0, max_duration, v_min, v_max)
            d_prev = d
            v_prev = v
            res = overlay(res, draw_line(x_prev, y_prev, x, y))
    return res

def selon_sexe(line: str) -> bool:
    l: List[str] = decompose_ligne(enleve_guillemets_ligne(line), ";")
    return l[1] == "0"



# show_image(image_courbe_n("covid19-20112021", ";", "jour", "dc",  False, selon_sexe))


