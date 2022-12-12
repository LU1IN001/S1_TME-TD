#Exercice 9.5
#Question 1
BDP : Dict[str, float] = {'Sabre Laser': 229.0, 'Mitendo DX': 127.30, 'Coussin Linux': 74.50, 'Slip Goldorak': 29.90, 'Station Nextpresso': 184.60}

#Question 2
def prix_moyen(d : Dict[str, float]) -> float :
    """Précondition : len(d) >= 1
    Retourne le prix moyen des produits disponibles"""
    res : float = 0
    e : float
    for _, e in d.items() :
        res = res + e
    return res/len(d)

assert abs(prix_moyen(BDP) - 129.06) < 10**-15


#Question 3
def fourchette_prix(mini : float, maxi : float, d : Dict[str, float]) -> Set[str] :
    """Retourne l'ensemble des noms de produits disponibles dans la fourchette choisi"""
    res : Set[str] = set()
    n : str
    for n in d :
        if d[n] > mini and d[n] < maxi :
            res.add(n)
    return res


assert fourchette_prix(50.0, 200.0, BDP) == {'Coussin Linux', 'Mitendo DX', 'Station Nextpresso'}

#Question 4
Panier : Dict[str, int] = {'Sabre Laser' : 3, 'Coussin Linux' : 2, 'Slip Goldorak' : 1}

#Question 5
def tous_disponibles(panier : Dict[str, int], bdp : Dict[str, float]) -> bool :
    """Précondition : len(panier) >=1 and len(bdp) >=1
    Retourne la disponibilité des articles dans la base de prix"""
    n : str
    for n in panier :
        if not (n in bdp) :
            return False
    return True

assert tous_disponibles(Panier, BDP) == True
