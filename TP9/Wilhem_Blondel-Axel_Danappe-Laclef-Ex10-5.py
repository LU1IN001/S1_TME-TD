Grandes_Lignes : Dict[str, Set[str]]
Grandes_Lignes = {'Paris': {'Strasbourg', 'Dijon', 'Toulouse',
'Lille', 'Lyon', 'Bordeaux'},
'Strasbourg':{'Paris', 'Dijon', 'München'},
'München': {'Strasbourg'},
'Dijon': {'Paris', 'Strasbourg', 'Lyon', 'Toulouse'},
'Lyon':{'Paris', 'Dijon', 'Toulouse'},
'Toulouse': {'Paris', 'Lyon', 'Dijon', 'Bordeaux'},
'Bordeaux': {'Nantes', 'Paris'},
'Nantes': {'Paris', 'Bordeaux','Quimper'},
'Quimper':{'Nantes'}, 'Ajaccio': {'Bastia'},
'Bastia': {'Ajaccio'}, 'Lille': {'Paris'}}

def trajet_direct(carte: Dict[str, Set[str]], st1: str, st2: str) -> bool:
    """Préconditions: st1 in carte
    Indique si le trajet direct est possible"""
    return st2 in carte[st1]

assert trajet_direct(Grandes_Lignes, 'Paris', 'Bordeaux') == True
assert trajet_direct(Grandes_Lignes, 'Paris', 'Ajaccio') == False

def ajout_station(station: str, correspondances: Set[str], carte: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
    """Précondition station not in carte
    Retourne la nouvelle carte avec la nouvelle station en ajoutant ses correspondances"""
    res: Dict[str, Set[str]] = {station: correspondances}
    k: str
    v: Set[str]
    for k, v in carte.items():
        set_copy: Set[str] = {e for e in v}
        if k in correspondances:
            set_copy.add(station)
        res[k] = set_copy
    return res

Nouvelles_Lignes : Dict[str, Set[str]]
Nouvelles_Lignes = ajout_station('Limoges', {'Paris', 'Toulouse', 'Bordeaux'}, Grandes_Lignes)
assert trajet_direct(Nouvelles_Lignes, 'Limoges', 'Paris') == True
assert trajet_direct(Nouvelles_Lignes, 'Bordeaux', 'Limoges') == True
assert trajet_direct(Nouvelles_Lignes, 'Limoges', 'Dijon') == False

def stations_atteignables(carte: Dict[str, Set[str]], depart: str, k: int) -> Set[str]:
    """Préconditions k > 0
    Retourne les stations qu'il est possible d'atteindre à partir du nombre exact de k correspondances"""
    res: Set[str] = { depart }
    i: int
    station: str
    for i in range(k):
        new_cor: Set[str] = set()
        for station in res:
            new_cor = new_cor | carte[station]
        res = new_cor
    return res

assert stations_atteignables(Grandes_Lignes, 'Paris', 0) == {'Paris'}
assert stations_atteignables(Grandes_Lignes, 'Paris', 1) == {'Bordeaux', 'Dijon', 'Lille', 'Lyon', 'Strasbourg', 'Toulouse'}
assert stations_atteignables(Grandes_Lignes, 'Paris', 2) == {'Bordeaux','Dijon','Lyon','München','Nantes','Paris','Strasbourg','Toulouse'}

def compteur_changements(carte: Dict[str, Set[str]], depart: str, arrivée: str) -> int:
    """Préconditions le départ et l'arrivée est un correspondance valide
    Retourne le nombre de correspondances nécéssaire pour partir du départ à l'arrivé"""
    i: int = 0
    while arrivée not in stations_atteignables(carte, depart, i):
        i=i+1
    return i


assert compteur_changements(Grandes_Lignes, 'Paris', 'Paris') == 0
assert compteur_changements(Grandes_Lignes, 'Paris', 'Dijon') == 1
assert compteur_changements(Grandes_Lignes, 'Paris', 'Quimper') == 3


def existence_trajet(carte: Dict[str, Set[str]], depart: str, arrivée: str) -> bool:
    """Indique si le départ est bien connecté à l'arrivée"""
    already_visited: Set[str] = set()
    i: int = 0
    while len(stations_atteignables(carte, depart, i) - already_visited) != 0:
        already_visited = already_visited | stations_atteignables(carte, depart, i)
        if arrivée in already_visited:
            return True
        i = i + 1
    return False


assert existence_trajet(Grandes_Lignes, 'Paris', 'München') == True
assert existence_trajet(Grandes_Lignes, 'Ajaccio', 'Bordeaux') == False
