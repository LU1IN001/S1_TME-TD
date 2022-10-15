import random
def lancer_de6()-> int:
    """retourne la valeur du lancé de dé6"""
    s: float =random.random()
    if s <= 1/6 :
        return 1
    elif s <= 2/6 :
        return 2
    elif s <= 3/6 :
        return 3
    elif s <= 4/6 :
        return 4
    elif s <= 5/6 :
        return 5
    else : return 6
    
assert 1 <= lancer_de6() <= 6
assert 6 >= lancer_de6() >= 1

#Question 2
random.seed(42)
assert lancer_de6()==4
assert lancer_de6()==1
assert lancer_de6()==2

#Question 3
def moyenne_plusieurs_lancers(n: int) -> float:
    """Précondition n>0
    Retourne la moyenne obtenue en lançant n fois un dé 6"""
    i: int = 0
    s: int = 0
    while(i<=n):
        s = s + lancer_de6()
        i=i+1
    return s/i-1

#Question 4
def frequence_valeur(r: int, n: int) -> float:
    """ Précondition : r>=1 and r<=6 and n>0
    Retourne la fréquence d'apparition de la valeur r lors de n lancers de dé"""
    i: int = 0
    compt: int = 0
    while(i<=n):
        if lancer_de6()== r:
            compt = compt+1
        i=i+1
    return compt/n

#Question subsidiaire
#Plus le nombre de lancers effectué est grand et plus la frequence se rapproche de 1/6, donc la fonction lancer_de6 suit bien une loi uniforme

#Question 5
def lancer_deN(n: int) ->int:
    """Précondition : n>0
    Retourne une valeur comprise entre 1 et n"""
    s: float = random.random()
    i: int = 1
    while(i/n<=s):
        i=i+1
    return i
assert 1<= lancer_deN(20) <= 20
assert 1<= lancer_deN(30) <= 30
assert 1<= lancer_deN(40) <= 40
assert lancer_deN(1) == 1
