import math

def moyenne_trois_nb(nb_1: float, nb_2: float, nb_3: float) -> float:
    """
    retourne la moyenne des 3 nombres indiqués en paramètres
    """
    return (nb_1 + nb_2 + nb_3)/3

assert moyenne_trois_nb(3, 6, -3) == 2
assert moyenne_trois_nb(3, 0, -3) == 0
assert moyenne_trois_nb(1.5, 2.5, 1.0) == 5/3

def moyenne_ponderee(a: float, pa: float, b: float, pb: float, c: float, pc: float) -> float:
    """
    Précodntions pa + pb + pc > 0
    retourne la moyenne pondérée des 3 nombres indiqués en paramètres
    """
    return (a*pa + b*pb + c*pc)/(pa+pb+pc)

assert moyenne_ponderee(3, 1, 6, 1, -3, 1) == 2
assert moyenne_ponderee(3, 1, 0, 1, -3, 1) == 0
assert moyenne_ponderee(1.5, 1, 2.5, 1, 1.0, 1) == 5/3


# ------- Exercice 2 -----------

def prix_ttc(prix_ht: float, tva: float) -> float:
    """
    Préconditions prix_ht > 0 et tva en pourcentage
    retounrne le prix TTC
    """
    return prix_ht*(1+(tva/100))

assert prix_ttc(100.0, 20.0) == 120.0
assert prix_ttc(100, 0) == 100.0
assert prix_ttc(100, 100) == 200.0
assert prix_ttc(0, 20.0) == 0.0
assert prix_ttc(200, 5.5) == 211.0

def prix_ht(prix_ttc: float, tva: float) -> float:
    """
    Préconditions prix_ttc > 0 et tva en pourcentage
    retounrne le prix HT
    """

    return prix_ttc/(1+(tva/100))

assert prix_ht(120.0, 20.0) == 100.0
assert prix_ht(100, 0) == 100.0
assert prix_ht(200, 100) == 100.0
assert prix_ht(0, 20.0) == 0.0
assert prix_ht(211.0, 5.5) == 200.0

# ----- Exercice 3 -----

def polynomiale(a: float, b: float, c: float, d:float,  x:float) -> float:
    """
    retourne la valeur du polynome ax**3+bx**2+cx+d
    """
    return d + x*(c+x*(b+a*x)) # pa bo


assert polynomiale(1,1,1,1,2) == 15
assert polynomiale(1,1,1,1,3) == 40

# ----- Exercice 4 -----

def aire_disque(r: float) -> float:
    """
    Préconditions: r >= 0
    retourne l'aire d'un disque avec la rayon indiqué
    """
    return math.pi * r**2

assert aire_disque(1) == math.pi
assert aire_disque(3) == math.pi * 9

def aire_couronne(r1: float, r2: float) -> float:
    """
    Préconditions r1 et r2 >= 0 et r2 >= r1
    retourne l'aire de la couronne avec les rayons indiqué
    """
    return aire_disque(r2)-aire_disque(r1)

assert aire_couronne(1,3) == math.pi * 8
assert aire_couronne(5, 5) == 0

# ----- Exercice 7 -----

def excursion(nb_personne: int) -> int:
    """
    Préconditions nb_personne >= 0
    retourne le prix à payer pour l'excursion
    """

    return 1200*(nb_personne//60 + 1 - 0**(nb_personne%60)) + 300*((nb_personne//18+1 - 0**(nb_personne%18)))

assert excursion(0) == 0
assert excursion(18) == 1500
assert excursion(60) == 2400


def excursion2(nb_adu: int, nb_enf: int) -> int:
    """
    Préconditions nb_adu et nb_enf >= 0
    retourne le prix à payer pour l'excursion
    """

    return 1200*((nb_adu+nb_enf)//60 + 1 - 0**((nb_adu+nb_enf)%60)) + 300*((nb_adu//18+1 - 0**(nb_adu%18))) + 250*((nb_enf//8+1 - 0**(nb_enf%8)))

assert excursion2(0, 0) == 0
assert excursion2(1, 0) == 1500
assert excursion2(0,1) == 1450


